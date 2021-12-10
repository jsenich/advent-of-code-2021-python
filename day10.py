from collections import deque

CLOSING_MAP = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

OPENING_CHARACTERS = CLOSING_MAP.keys()


def part_one(puzzle_input: str) -> int:
    score_map: dict[str, int] = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    score = 0
    for line in puzzle_input.splitlines():
        chars = list(line)
        opening_chars = deque()
        for i, c in enumerate(chars):
            if c in OPENING_CHARACTERS:
                opening_chars.append(c)
            else:
                if c != CLOSING_MAP[opening_chars[-1]]:
                    score += score_map[c]
                    break
                else:
                    opening_chars.pop()

    return score


def part_two(puzzle_input: str) -> int:
    score_map = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    scores = []
    puzzle_lines = puzzle_input.splitlines()
    for line in puzzle_lines:
        chars = list(line)
        opening_chars = deque()
        skip_line = False
        for i, c in enumerate(chars):
            if c in OPENING_CHARACTERS:
                opening_chars.append(c)
            else:
                if c != CLOSING_MAP[opening_chars[-1]]:
                    skip_line = True
                    break
                else:
                    opening_chars.pop()
        if not skip_line:
            closing = list(reversed([CLOSING_MAP[c] for c in opening_chars]))

            line_score = 0

            for c in closing:
                line_score = (line_score * 5) + score_map[c]

            scores.append(line_score)

    scores = sorted(scores)

    return scores[int((len(scores) - 1) / 2)]


if __name__ == '__main__':

    puzzle_input = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

    with open('data/day10_input.txt') as f:
        puzzle_input = f.read().strip()

    print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part two answer: {part_two(puzzle_input)}')

KNOWN_PATTERN_LENGTHS = [2, 4, 3, 7]

segment_lengths = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8],
}


def part_one(puzzle_input: str) -> int:
    easy_digits = 0
    for line in puzzle_input.split("\n"):
        _, outputs = line.split("|")

        easy_digits += sum(
            [1 for o in outputs.strip().split() if len(o) in KNOWN_PATTERN_LENGTHS]
        )

    return easy_digits


def resolve_segments(patterns: list[str], outputs: list[str]) -> int:
    digit_pattern = {}
    b_left = set()
    u_right = set()

    six_segments = []
    five_segments = []

    # known numbers
    for i, pattern in enumerate(patterns):
        pattern_len = len(pattern)
        if pattern_len in KNOWN_PATTERN_LENGTHS:
            digit_pattern[segment_lengths[pattern_len][0]] = set(pattern)
        elif pattern_len == 6:
            six_segments.append(pattern)
        elif pattern_len == 5:
            five_segments.append(pattern)

    # get patterns for 6 segments
    while len(six_segments):
        to_remove = None
        for pattern in six_segments:
            if 6 not in digit_pattern:
                diff = digit_pattern[8] - set(pattern)
                if len(diff & digit_pattern[1]) > 0:
                    #  this is a 6
                    digit_pattern[6] = set(pattern)
                    u_right = diff
                    to_remove = pattern
                    break
            elif 0 not in digit_pattern:
                diff = digit_pattern[6] - set(pattern)
                if len(diff & digit_pattern[4]) > 0:
                    digit_pattern[0] = set(pattern)
                    to_remove = pattern
                    break
            elif 6 in digit_pattern and 0 in digit_pattern:
                digit_pattern[9] = set(pattern)
                b_left = digit_pattern[8] - digit_pattern[9]
                to_remove = pattern
                break

        if to_remove:
            six_segments.remove(to_remove)
            to_remove = None

    while len(five_segments):
        to_remove = None
        for pattern in five_segments:
            diff = digit_pattern[8] - set(pattern)

            if len(diff - (u_right | b_left)) == 0:
                #  this is a five
                digit_pattern[5] = set(pattern)
                to_remove = pattern
                break
            elif len(diff & digit_pattern[1]) == 0:
                # this is a 3
                digit_pattern[3] = set(pattern)
                to_remove = pattern
                break
            else:
                # this is a 2
                digit_pattern[2] = set(pattern)
                to_remove = pattern
                break
        if to_remove:
            five_segments.remove(to_remove)
            to_remove = None

    pattern_lookup = {''.join(sorted(v)): str(k) for k, v in digit_pattern.items()}

    resolved_outputs = []
    for o in outputs:
        resolved_outputs.append(pattern_lookup.get(o))

    output = int(''.join(resolved_outputs))

    return output


def part_two(puzzle_input: str) -> int:
    all_outputs = []
    for line in puzzle_input.split("\n"):
        signal_patterns, output_values = line.split("|")
        signal_patterns = [''.join(sorted(p)) for p in signal_patterns.strip().split()]
        output_values = [''.join(sorted(o)) for o in output_values.strip().split()]
        all_outputs.append(resolve_segments(signal_patterns, output_values))

    return sum(all_outputs)


if __name__ == '__main__':
    # puzzle_input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

    with open('data/day08_input.txt') as f:
        puzzle_input = f.read().strip()

    print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part two answer: {part_two(puzzle_input)}')

    # part one: 321
    # part two: 1028926

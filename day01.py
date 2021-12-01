def part_one(puzzle_input: list[int]) -> int:
    increasedCount = 0
    for i, depth in enumerate(puzzle_input):
        if i > 0:
            if depth > puzzle_input[i - 1]:
                increasedCount += 1

    return increasedCount


def part_two(puzzle_input: list[int]) -> int:
    increasedCount = 0

    for i in range(len(puzzle_input)):
        if i > 0 and i + 2 < len(puzzle_input):
            if (
                sum([puzzle_input[i], puzzle_input[i + 1], puzzle_input[i + 2]]) >
                sum([puzzle_input[i - 1], puzzle_input[i], puzzle_input[i + 1]])
            ):
                increasedCount += 1

    return increasedCount


if __name__ == '__main__':

    with open('data/day01_input.txt') as f:
        puzzle_input = [int(n) for n in f.readlines() if n]

    print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part two answer: {part_two(puzzle_input)}')

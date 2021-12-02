def part_one(puzzle_input: list[tuple[str, int]]) -> int:
    horizontal = 0
    vertical = 0

    for line in puzzle_input:
        direction, distance = line

        if direction == 'forward':
            horizontal += distance
        elif direction == 'down':
            vertical += distance
        elif direction == 'up':
            vertical -= distance

    return horizontal * vertical


def part_two(puzzle_input: list[tuple[str, int]]) -> int:
    horizontal = 0
    vertical = 0
    aim = 0

    for line in puzzle_input:
        direction, distance = line

        if direction == 'forward':
            horizontal += distance
            vertical += aim * distance
        elif direction == 'down':
            aim += distance
        elif direction == 'up':
            aim -= distance

    return horizontal * vertical


if __name__ == '__main__':

    with open('data/day02_input.txt') as f:
        puzzle_input = []
        for line in f.readlines():
            if not line:
                continue
            line_parts = line.strip().split(" ")
            puzzle_input.append((line_parts[0], int(line_parts[1])))

    print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part two answer: {part_two(puzzle_input)}')

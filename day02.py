from timer import print_time


@print_time
def part_one(puzzle_input: list[tuple[str, int]]) -> int:
    horizontal_position = 0
    depth = 0

    for line in puzzle_input:
        direction, distance = line

        match direction:
            case 'forward':
                horizontal_position += distance
            case 'down':
                depth += distance
            case 'up':
                depth -= distance
            case _:
                pass

    return horizontal_position * depth


@print_time
def part_two(puzzle_input: list[tuple[str, int]]) -> int:
    horizontal_position = 0
    depth = 0
    aim = 0

    for line in puzzle_input:
        direction, distance = line

        match direction:
            case 'forward':
                horizontal_position += distance
                depth += aim * distance
            case 'down':
                aim += distance
            case 'up':
                aim -= distance
            case _:
                pass

    return horizontal_position * depth


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

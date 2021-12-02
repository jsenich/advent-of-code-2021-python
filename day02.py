def part_one(puzzle_input):
    horizontal = 0
    vertical = 0

    for line in puzzle_input:
        direction, distance = line

        if direction == 'forward':
            horizontal += int(distance)
        elif direction == 'down':
            vertical += int(distance)
        elif direction == 'up':
            vertical -= int(distance)

    return horizontal * vertical


def part_two(puzzle_input):
    horizontal = 0
    vertical = 0
    aim = 0

    for line in puzzle_input:
        direction, distance = line

        if direction == 'forward':
            horizontal += int(distance)
            vertical += aim * int(distance)
        elif direction == 'down':
            aim += int(distance)
        elif direction == 'up':
            aim -= int(distance)

    return horizontal * vertical


if __name__ == '__main__':

    with open('data/day02_input.txt') as f:
        puzzle_input = [l.strip().split(" ") for l in f.readlines() if l]

    print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part two answer: {part_two(puzzle_input)}')

from collections import Counter

from timer import print_time


def extract_line_points(puzzle_input: str) -> list[list[tuple[int, int]]]:
    coordinate_pairs = []
    for line in puzzle_input.split("\n"):
        pairs = line.split(" -> ")
        x1, y1 = pairs[0].split(",")
        x2, y2 = pairs[1].split(",")

        coordinate_pairs.append([(int(x1), int(y1)), (int(x2), int(y2))])

    return coordinate_pairs


@print_time
def part_one(puzzle_input: str) -> int:
    coordinates = extract_line_points(puzzle_input)
    touched_points = []

    for c in coordinates:
        x1, y1 = c[0]
        x2, y2 = c[1]

        if y1 != y2 and x1 != x2:
            # not a straight line
            continue

        if y1 == y2:
            if x1 > x2:
                for _, n in enumerate(range(x1-x2 + 1)):
                    touched_points.append((x2 + n, y2))
            else:
                for _, n in enumerate(range(x2-x1 + 1)):
                    touched_points.append((x1 + n, y1))
        else:
            if y1 > y2:
                for _, n in enumerate(range(y1-y2 + 1)):
                    touched_points.append((x2, y2 + n))
            else:
                for _, n in enumerate(range(y2-y1 + 1)):
                    touched_points.append((x1, y1 + n))

    overlapping_counts = Counter(touched_points)

    counter = sum(1 for c in overlapping_counts.values() if c > 1)

    return counter


@print_time
def part_two(puzzle_input: str) -> int:
    coordinates = extract_line_points(puzzle_input)
    touched_points = []

    for c in coordinates:
        x1, y1 = c[0]
        x2, y2 = c[1]

        if y1 != y2 and x1 != x2:
            if x1 > x2:
                x_range = range(x1, x2 - 1, -1)
            else:
                x_range = range(x1, x2 + 1)

            if y1 > y2:
                y_range = range(y1, y2 - 1, -1)
            else:
                y_range = range(y1, y2 + 1)

            for point in zip(x_range, y_range):
                touched_points.append(point)
        else:
            if x1 == x2:
                if y1 > y2:
                    y_range = range(y1, y2 - 1, -1)
                else:
                    y_range = range(y1, y2 + 1)

                for y in y_range:
                    touched_points.append((x1, y))
            else:
                if x1 > x2:
                    x_range = range(x1, x2 - 1, -1)
                else:
                    x_range = range(x1, x2 + 1)

                for x in x_range:
                    touched_points.append((x, y2))

    overlapping_counts = Counter(touched_points)
    counter = sum(1 for c in overlapping_counts.values() if c > 1)

    return counter


if __name__ == '__main__':
    with open('data/day05_input.txt') as f:
        puzzle_input = f.read().strip()

    print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part two answer: {part_two(puzzle_input)}')

# part one answer: 5576
# part two answer: 18144

from collections import Counter
# from math import atan2, degrees


def part_one(puzzle_input):

    coordinates = []
    touched_points = []

    for line in puzzle_input.split("\n"):
        pairs = line.split(" -> ")
        x1, y1 = pairs[0].split(",")
        x2, y2 = pairs[1].split(",")

        coordinates.append([(int(x1), int(y1)), (int(x2), int(y2))])

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

    counter = 0
    for c in overlapping_counts.values():
        if c >= 2:
            counter += 1

    return counter


def part_two(puzzle_input):

    coordinates = []
    touched_points = []

    grid = []
    for i in range(10):
        grid.append([])
        for _ in range(10):
            grid[i].append('.')

    for line in puzzle_input.split("\n"):
        pairs = line.split(" -> ")
        x1, y1 = pairs[0].split(",")
        x2, y2 = pairs[1].split(",")

        coordinates.append([(int(x1), int(y1)), (int(x2), int(y2))])

    for c in coordinates:
        x1, y1 = c[0]
        x2, y2 = c[1]

        if y1 != y2 and x1 != x2:
            # angle = degrees(atan2(y1-y2, x1-x2))
            # if abs(angle) != 45:
            #     # only consider 45 degree lines
            #     continue

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

    # for point in touched_points:
    #     if grid[point[1]][point[0]] == '.':
    #         grid[point[1]][point[0]] = 1
    #     else:
    #         grid[point[1]][point[0]] += 1

    # for row in grid:
    #     print(' '.join([str(n) for n in row]))
    # print("\n\n\n")

    counter = 0
    for c in overlapping_counts.values():
        if c >= 2:
            counter += 1

    return counter


if __name__ == '__main__':

    puzzle_input = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".strip()



    with open('data/day05_input.txt') as f:
        puzzle_input = f.read().strip()

    print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part two answer: {part_two(puzzle_input)}')

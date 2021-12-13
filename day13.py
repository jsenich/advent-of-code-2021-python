import numpy as np


def part_one(puzzle_input: str) -> int:
    coords, folds = puzzle_input.split("\n\n")

    max_y, max_x = 0, 0
    points = []

    for line in coords.splitlines():
        y, x = line.split(',')
        y = int(y)
        x = int(x)
        points.append((y, x))
        if y > max_y:
            max_y = y
        if x > max_x:
            max_x = x

    if max_x % 2 == 0:
        max_x += 1
    else:
        max_x += 2

    if max_y % 2 == 0:
        max_y += 1
    else:
        max_y += 2

    paper = np.full((max_x, max_y), '.', dtype=str)
    for y, x in points:
        paper[x][y] = '#'

    instructions = []
    for line in folds.splitlines():
        axis, position = line.replace('fold along ', '').split('=')
        instructions.append((axis, int(position)))

    axis_map = {'x': 1, 'y': 0}

    for f in instructions:
        # remove fold line
        paper = np.delete(paper, f[1], axis_map[f[0]])
        p1, p2 = np.split(paper, 2, axis_map[f[0]])
        if f[0] == 'y':
            p2 = np.flipud(p2)
        else:
            p2 = np.fliplr(p2)

        for i, row in enumerate(p2):
            for j, col in enumerate(row):
                if col != '.':
                    p1[i][j] = col
        paper = p1
        return np.count_nonzero(paper == '#')

    return 0


def part_two(puzzle_input: str) -> str:
    coords, folds = puzzle_input.split("\n\n")

    max_y, max_x = 0, 0
    points = []

    for line in coords.splitlines():
        y, x = line.split(',')
        y = int(y)
        x = int(x)
        points.append((y, x))
        if y > max_y:
            max_y = y
        if x > max_x:
            max_x = x

    if max_x % 2 == 0:
        max_x += 1
    else:
        max_x += 2

    if max_y % 2 == 0:
        max_y += 1
    else:
        max_y += 2

    paper = np.full((max_x, max_y), '.', dtype=str)
    for y, x in points:
        paper[x][y] = '#'

    instructions = []
    for line in folds.splitlines():
        axis, position = line.replace('fold along ', '').split('=')
        instructions.append((axis, int(position)))

    axis_map = {'x': 1, 'y': 0}

    for f in instructions:
        # remove fold line
        paper = np.delete(paper, f[1], axis_map[f[0]])
        p1, p2 = np.split(paper, 2, axis_map[f[0]])
        if f[0] == 'y':
            p2 = np.flipud(p2)
        else:
            p2 = np.fliplr(p2)

        for i, row in enumerate(p2):
            for j, col in enumerate(row):
                if col != '.':
                    p1[i][j] = col
        paper = p1

    answer = ''
    for row in paper:
        answer += ''.join(row) + "\n"

    return answer


if __name__ == '__main__':

    puzzle_input = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

    with open('data/day13_input.txt') as f:
        puzzle_input = f.read().strip()

    print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part two answer: \n{part_two(puzzle_input)}')

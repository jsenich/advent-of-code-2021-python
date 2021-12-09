import sys
from collections import defaultdict


import numpy as np


def part_one(puzzle_input: str) -> int:
    map_lines = puzzle_input.splitlines()
    height_map = np.full((len(map_lines) + 2, len(map_lines[0]) + 2), 9, dtype=np.int32)
    risk_levels = []
    for i, line in enumerate(map_lines):
        for j, num in enumerate(line):
            height_map[i+1][j+1] = int(num)

    for i, row in enumerate(height_map):
        if i == 0 or i == len(height_map) - 1:
            continue
        for j, col in enumerate(height_map[i]):
            curr_val = height_map[i][j]
            if j == 0 or j == len(height_map[i]) - 1:
                continue
            if (
                curr_val < height_map[i + 1][j] and
                curr_val < height_map[i - 1][j] and
                curr_val < height_map[i][j + 1] and
                curr_val < height_map[i][j - 1]
            ):
                risk_levels.append(curr_val + 1)

    return sum(risk_levels)


def part_two(puzzle_input):
    height_map = defaultdict(lambda: 9)
    for row, line in enumerate(puzzle_input.splitlines()):
        for col, num in enumerate(line):
            height_map[(row, col)] = int(num)

    basin_sizes = []

    for (row, col), height in tuple(height_map.items()):
        if (
            height_map[row, col + 1] > height and
            height_map[row, col - 1] > height and
            height_map[row + 1, col] > height and
            height_map[row - 1, col] > height
        ):
            basin_points = set()
            points_to_add = [(row, col)]
            while points_to_add:
                row, col = points_to_add.pop()
                basin_points.add((row, col))
                for point in (
                    (row, col + 1),
                    (row, col - 1),
                    (row + 1, col),
                    (row - 1, col),
                ):
                    if point not in basin_points and height_map[point] != 9:
                        points_to_add.append(point)

            basin_sizes.append(len(basin_points))

    basin_sizes_sorted = sorted(basin_sizes)

    return basin_sizes_sorted[-1] * basin_sizes_sorted[-2] * basin_sizes_sorted[-3]


if __name__ == '__main__':

    puzzle_input = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""

    with open('data/day09_input.txt') as f:
        puzzle_input = f.read().strip()

    # print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part two answer: {part_two(puzzle_input)}')

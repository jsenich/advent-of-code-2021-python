from collections import defaultdict
import numpy as np


def part_one(puzzle_input: str) -> int:
    flash_total = 0
    energy_levels = np.array([[int(i) for i in line] for line in puzzle_input.splitlines()])

    for step in range(100):
        flashed = []

        for r, row in enumerate(energy_levels):
            for c, _ in enumerate(row):
                energy_levels[r][c] += 1
                if energy_levels[r][c] > 9:
                    flashed.append((r, c))

        # for row in range(len(energy_levels) - 1):
        #     for col in range(len(energy_levels[row]) - 1):
        #         energy_levels[row][col] += 1
        #         if energy_levels[row][col] > 9:
        #             flashed.append((row, col))

        # increase_levels(energy_levels)

        # flashed.extend(zip(*np.where(energy_levels > 9)))

        while flashed:
            r, c = flashed.pop()
            if energy_levels[r][c] == 0:
                continue
            energy_levels[r][c] = 0
            flash_total += 1

            # if (r, c) not in already_flashed:
            #     already_flashed.add((r, c))
            #     energy_levels[r][c] = 0
            # else:
            #     continue

            # check adjacent
            for r2, c2 in (
                (r - 1, c),
                (r - 1, c - 1),
                (r - 1, c + 1),
                (r + 1, c + 1),
                (r + 1, c - 1),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
            ):
                if -1 in (r2, c2):
                    continue
                elif r2 == len(energy_levels) or c2 == len(energy_levels[0]):
                    continue
                # try:
                if energy_levels[r2][c2] != 0:
                    energy_levels[r2][c2] += 1
                    if energy_levels[r2][c2] > 9:
                        flashed.append((r2, c2))
                # except IndexError:
                #     pass

        # for row, col in already_flashed:
        #     energy_levels[row][col] = 0
        # flash_total += len(already_flashed)
        # already_flashed.clear()

    return flash_total


if __name__ == '__main__':

    puzzle_input = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

    with open('data/day11_input.txt') as f:
        puzzle_input = f.read().strip()

    print(f'part one answer: {part_one(puzzle_input)}')
    # print(f'part two answer: {part_two(puzzle_input)}')

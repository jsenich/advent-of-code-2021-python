import numpy as np
from copy import deepcopy


def part_one(puzzle_input: list[list[int]]) -> int:
    diagnostics_report = np.array(puzzle_input).T

    most_common = []
    least_common = []
    for line in diagnostics_report:
        line_most_common = np.bincount(line).argmax()
        most_common.append(line_most_common)
        least_common.append(abs(line_most_common - 1))

    gamma_rate = int(''.join(str(n) for n in most_common), 2)
    epsilon_rate = int(''.join(str(n) for n in least_common), 2)

    return gamma_rate * epsilon_rate


def part_two(puzzle_input: list[list[int]]) -> int:
    def get_diagnostics(raw_report: list[list[int]]) -> tuple[list[int], list[int]]:
        diagnostics_report = np.array(raw_report).T
        most_common = []
        least_common = []
        for line in diagnostics_report:
            _, bit_counts = np.unique(line, return_counts=True)
            if len(bit_counts) == 1:
                most_common.append(bit_counts[0])
            elif bit_counts[0] <= bit_counts[1]:
                most_common.append(1)
            else:
                most_common.append(0)

            if len(bit_counts) == 1:
                least_common.append(abs(bit_counts[0] - 1))
            elif bit_counts[0] <= bit_counts[1]:
                least_common.append(0)
            else:
                least_common.append(1)

        return most_common, least_common

    raw_report = deepcopy(puzzle_input)

    for i in range(len(raw_report[0])):
        if len(raw_report) == 1:
            break
        most_common, _ = get_diagnostics(raw_report)
        new_report = []
        for row in raw_report:
            if most_common[i] == row[i]:
                new_report.append(row)
        raw_report = new_report

    oxygen_rating = int(''.join(str(n) for n in raw_report[0]), 2)

    raw_report = deepcopy(puzzle_input)
    for i in range(len(raw_report[0])):
        if len(raw_report) == 1:
            break
        _, least_common = get_diagnostics(raw_report)
        new_report = []
        for row in raw_report:
            if least_common[i] == row[i]:
                new_report.append(row)
        raw_report = new_report

    co2_rating = int(''.join(str(n) for n in raw_report[0]), 2)

    return oxygen_rating * co2_rating


if __name__ == '__main__':
    with open('data/day03_input.txt') as f:
        puzzle_input = [[int(i) for i in n.strip()] for n in f.readlines() if n]

    print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part two answer: {part_two(puzzle_input)}')

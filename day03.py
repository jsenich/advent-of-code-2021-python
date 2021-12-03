import numpy as np
from collections import Counter
from copy import deepcopy


def part_one(puzzle_input):
    puzzle_matrix = np.flipud(np.rot90(np.array(puzzle_input)))

    most_common = []
    least_common = []
    for line in puzzle_matrix:
        m = Counter(line)
        line_most_common = m.most_common(1)[0][0]
        most_common.append(line_most_common)
        least_common.append(abs(line_most_common - 1))

    gamma = int(''.join(str(n) for n in most_common), 2)
    epsilon = int(''.join(str(n) for n in least_common), 2)


    return gamma * epsilon


def part_two(puzzle_input):
    def get_diagnostics(report):
        puzzle_matrix = np.flipud(np.rot90(np.array(report)))
        most_common = []
        least_common = []
        for line in puzzle_matrix:
            m = Counter(line)
            if m[0] == m[1]:
                line_most_common = 1
            else:
                line_most_common = m.most_common(1)[0][0]
            most_common.append(line_most_common)
            if m[0] == m[1]:
                least_common.append(0)
            else:
                least_common.append(abs(line_most_common - 1))

        return most_common, least_common

    diagnostic_report = deepcopy(puzzle_input)

    for i in range(len(diagnostic_report[0])):
        if len(diagnostic_report) == 1:
            break
        m, _ = get_diagnostics(diagnostic_report)
        new_report = []
        for row in diagnostic_report:
            if m[i] == row[i]:
                new_report.append(row)
        diagnostic_report = new_report

    oxygen_rating = int(''.join(str(n) for n in diagnostic_report[0]), 2)

    diagnostic_report = deepcopy(puzzle_input)
    for i in range(len(diagnostic_report[0])):
        if len(diagnostic_report) == 1:
            break
        _, l = get_diagnostics(diagnostic_report)
        new_report = []
        for row in diagnostic_report:
            if l[i] == row[i]:
                new_report.append(row)
        diagnostic_report = new_report

    co2_rating = int(''.join(str(n) for n in diagnostic_report[0]), 2)

    return oxygen_rating * co2_rating


if __name__ == '__main__':

    test_data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

    with open('data/day03_input.txt') as f:
        puzzle_input = [[int(i) for i in n.strip()] for n in f.readlines() if n]
        # puzzle_input = [[int(i) for i in n] for n in test_data.split()]

    print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part one answer: {part_two(puzzle_input)}')

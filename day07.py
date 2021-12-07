import numpy as np


def part_one(puzzle_input: str) -> int:
    crab_positions = np.fromstring(puzzle_input, dtype=np.int32, sep=',')
    crab_length = len(crab_positions)
    total_fuel_costs = np.zeros(crab_length, dtype=np.int32)

    for i, pos in enumerate(crab_positions):
        fuel_spent = np.zeros(crab_length, dtype=np.int32)

        for j, jpos in enumerate(crab_positions):
            if i == j:
                continue
            fuel_spent[j] = abs(pos - jpos)
        total_fuel_costs[i] = fuel_spent.sum()

    return np.min(total_fuel_costs)


def part_two(puzzle_input: str) -> int:
    crab_positions: np.ndarray = np.fromstring(puzzle_input, dtype=np.int32, sep=',')
    min_pos = crab_positions.min()
    max_pos = crab_positions.max()

    total_fuel_costs = np.zeros(max_pos - min_pos + 1, dtype=np.int32)
    for i, pos in enumerate(range(min_pos, max_pos + 1)):
        fuel_spent = np.zeros(max_pos - min_pos, dtype=np.int32)
        for j, jpos in enumerate(crab_positions):
            if pos == jpos:
                continue
            fuel_spent[j] = sum(range(1, abs(jpos - pos) + 1))
        total_fuel_costs[i] = fuel_spent.sum()

    # crab_length = len(crab_positions)
    # total_fuel_costs = np.zeros(crab_length, dtype=np.int32)


    # for i, pos in enumerate(crab_positions):
    #     fuel_spent = np.zeros(crab_length, dtype=np.int32)

    #     for j, jpos in enumerate(crab_positions):
    #         if i == j:
    #             continue
    #         fuel_spent[j] = sum(range(1, abs(jpos - 5) + 1))
    #     total_fuel_costs[i] = fuel_spent.sum()

    return np.min(total_fuel_costs)


if __name__ == '__main__':
    puzzle_input = "16,1,2,0,4,2,7,1,2,14"

    with open('data/day07_input.txt') as f:
        puzzle_input = f.read().strip()

    print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part two answer: {part_two(puzzle_input)}')

    # crab_positions = np.fromstring(puzzle_input, dtype=np.int32, sep=',')
    # for i, pos in enumerate(crab_positions):
    #     cost = sum(range(abs(pos - 5) + 1))
    #     print(cost)

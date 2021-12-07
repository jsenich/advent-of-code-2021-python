import numpy as np


def part_one(puzzle_input):
    fish_timers = [int(n) for n in puzzle_input.split(',')]

    for i, _ in enumerate(range(80), 1):
        timers = []
        new_fish = []
        for d in fish_timers:
            if d == 0:
                new_fish.append(8)
                timers.append(6)
            else:
                timers.append(d - 1)
        fish_timers = timers
        fish_timers.extend(new_fish)

    return len(fish_timers)


def part_two(puzzle_input):
    fish_timers = np.zeros(9, dtype=np.int64)
    np.add.at(fish_timers, np.fromstring(puzzle_input, dtype=np.int64, sep=','), 1)

    for _ in range(256):
        new_fish = 0
        for internal_timer, value_count in enumerate(fish_timers):
            if internal_timer == 0:
                new_fish = value_count
            else:
                fish_timers[internal_timer - 1] = value_count

        fish_timers[6] += new_fish
        fish_timers[8] = new_fish

    return fish_timers.sum()


if __name__ == '__main__':

    puzzle_input = "3,4,3,1,2"

    with open('data/day06_input.txt') as f:
        puzzle_input = f.read().strip()

    print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part two answer: {part_two(puzzle_input)}')

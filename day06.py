import numpy as np

from timer import print_time


def calculate_fish_population(spawn_timer_data: str, days: int) -> np.int64:
    fish_spawn_timers = np.zeros(9, dtype=np.int64)
    np.add.at(
        fish_spawn_timers,
        np.fromstring(puzzle_input, dtype=np.int64, sep=','),
        1
    )

    for _ in range(days):
        new_fish = 0
        for internal_timer, value_count in enumerate(fish_spawn_timers):
            if internal_timer == 0:
                new_fish = value_count
            else:
                fish_spawn_timers[internal_timer - 1] = value_count

        fish_spawn_timers[6] += new_fish
        fish_spawn_timers[8] = new_fish

    return fish_spawn_timers.sum()


@print_time
def part_one(puzzle_input):
    return calculate_fish_population(puzzle_input, 80)


@print_time
def part_two(puzzle_input):
    return calculate_fish_population(puzzle_input, 256)


if __name__ == '__main__':
    with open('data/day06_input.txt') as f:
        puzzle_input = f.read().strip()

    print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part two answer: {part_two(puzzle_input)}')

# part one answer: 355386
# part two answer: 1613415325809

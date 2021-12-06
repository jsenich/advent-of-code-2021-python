
def part_one(puzzle_input):
    internal_timers = [int(n) for n in puzzle_input.split(',')]

    for i, _ in enumerate(range(80), 1):
        timers = []
        new_fish = []
        for d in internal_timers:
            if d == 0:
                new_fish.append(8)
                timers.append(6)
            else:
                timers.append(d - 1)
        internal_timers = timers
        timers.extend(new_fish)

    return len(internal_timers)


if __name__ == '__main__':

    puzzle_input = "3,4,3,1,2"

    with open('data/day06_input.txt') as f:
        puzzle_input = f.read().strip()

    print(f'part one answer: {part_one(puzzle_input)}')
    # print(f'part two answer: {part_two(puzzle_input)}')

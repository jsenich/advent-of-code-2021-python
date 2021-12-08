import numpy as np


def part_one(puzzle_input: str) -> int:
    counter = 0
    for line in puzzle_input.split("\n"):
        _, outputs = line.split("|")
        for o in outputs.strip().split():
            if len(o) in (2, 4, 3, 7):
                counter += 1

    return counter

def part_two(puzzle_input):
    pass


if __name__ == '__main__':
    # puzzle_input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

    with open('data/day08_input.txt') as f:
        puzzle_input = f.read().strip()




    # pattern_positions = np.zeros(10, dtype=np.int32)

    # signal_patterns, output_values = puzzle_input.split("|")
    # signal_patterns = signal_patterns.strip().split()
    # output_values = output_values.strip().split()


    # signal_patterns = [sorted(p) for p in signal_patterns]
    # output_values = [sorted(p) for p in output_values]
    # pass


    unique_segment_lengths = {
        2: 1,
        4: 4,
        3: 7,
        7: 8,
    }

    # unique_segments = []

    # for i, pattern in enumerate(signal_patterns):
    #     if unique_num := unique_segment_lengths.get(len(pattern)):
    #         pattern_positions[i] = unique_num
    #         unique_segments.append(pattern)

    # counter = 0
    # for



    pass


    print(f'part one answer: {part_one(puzzle_input)}')
    # print(f'part two answer: {part_two(puzzle_input)}')

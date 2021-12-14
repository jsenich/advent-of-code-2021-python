import itertools
from collections import Counter


def part_one(puzzle_input: str) -> int:
    template, pairs = puzzle_input.split("\n\n")
    pair_map = {}
    for pair in pairs.splitlines():
        k, v = pair.split(" -> ")
        pair_map[k] = v

    for _ in range(10):
        pair_insertions = list(template)
        last_index = 0
        for i, comb in enumerate(itertools.pairwise(template)):
            insertion_char = pair_map[''.join(comb)]
            pair_insertions.insert(last_index + 1, insertion_char)
            last_index += 2
        template = ''.join(pair_insertions)

    element_counts = Counter(template)

    return max(element_counts.values()) - min(element_counts.values())


def part_two(puzzle_input: str) -> int:
    template, pairs = puzzle_input.split("\n\n")
    pair_map = {}
    for pair in pairs.splitlines():
        k, v = pair.split(" -> ")
        pair_map[k] = v


    for step in range(40):
        print(f'step {step + 1}')
        pair_insertions = list(template)
        last_index = 0
        for i, comb in enumerate(itertools.pairwise(template)):
            insertion_char = pair_map[''.join(comb)]
            pair_insertions.insert(last_index + 1, insertion_char)
            last_index += 2
        template = ''.join(pair_insertions)

    element_counts = Counter(template)

    return max(element_counts.values()) - min(element_counts.values())


if __name__ == '__main__':

    puzzle_input = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

    with open('data/day14_input.txt') as f:
        puzzle_input = f.read().strip()

    print(f'part one answer: {part_one(puzzle_input)}')
    # print(f'part two answer: {part_two(puzzle_input)}')

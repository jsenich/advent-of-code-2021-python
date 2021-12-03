from day03 import part_one, part_two

test_data = """
00100
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


def test_part_one():
    puzzle_input = [[int(i) for i in n] for n in test_data.split()]

    expected = 198
    actual = part_one(puzzle_input)

    assert actual == expected


def test_part_two():
    puzzle_input = [[int(i) for i in n] for n in test_data.split()]

    expected = 230
    actual = part_two(puzzle_input)

    assert actual == expected

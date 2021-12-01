from day01 import part_one, part_two

puzzle_input = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263
]


def test_part_one():
    expected = 7
    actual = part_one(puzzle_input)

    assert actual == expected


def test_part_two():
    expected = 5
    actual = part_two(puzzle_input)

    assert actual == expected

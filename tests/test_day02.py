from day02 import part_one, part_two

puzzle_input = [
    ('forward', 5),
    ('down', 5),
    ('forward', 8),
    ('up', 3),
    ('down', 8),
    ('forward', 2),
]


def test_part_one():
    expected = 150
    actual = part_one(puzzle_input)

    assert actual == expected


def test_part_two():
    expected = 900
    actual = part_two(puzzle_input)

    assert actual == expected

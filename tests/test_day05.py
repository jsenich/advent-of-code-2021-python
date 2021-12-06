from day05 import part_one, part_two, extract_line_points


test_input = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


def test_extract_line_points():
    point_data = """
7,0 -> 7,4
6,4 -> 2,0
""".strip()

    expected = [[(7, 0), (7, 4)], [(6, 4), (2, 0)]]
    actual = extract_line_points(point_data)

    assert actual == expected


def test_part_one():
    puzzle_input = test_input.strip()

    expected = 5
    actual = part_one(puzzle_input)

    assert actual == expected


def test_part_two():
    puzzle_input = test_input.strip()

    expected = 12
    actual = part_two(puzzle_input)

    assert actual == expected

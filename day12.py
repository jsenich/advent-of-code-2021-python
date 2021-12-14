def part_one(puzzle_input: str):
    cave_connections = {}
    for line in puzzle_input.splitlines():
        l, r = line.split("-")
        cave_connections.setdefault(l, set()).add(r)
        cave_connections.setdefault(r, set()).add(l)

    visited = set()


    path_points = [('start',)]
    while path_points:
        path = path_points.pop()

        if path[-1] == 'end':
            visited.add(path)
            continue

        for point in cave_connections[path[-1]]:
            if point.isupper() or point not in path:
                new_path = [p for p in path]
                new_path.append(point)
                path_points.append(tuple(new_path))

    return len(visited)


def part_two(puzzle_input: str):
    cave_connections = {}
    for line in puzzle_input.splitlines():
        l, r = line.split("-")
        cave_connections.setdefault(l, set()).add(r)
        cave_connections.setdefault(r, set()).add(l)

    visited = set()


    path_points = [('start',)]
    lowercase_visited = []
    while path_points:
        path = path_points.pop()

        if path[-1] == 'end':
            visited.add(path)
            continue

        for point in cave_connections[path[-1]]:
            if point == 'start':
                continue
            if point.isupper():
                new_path = [p for p in path]
                new_path.append(point)
                path_points.append(tuple(new_path))
            elif point.islower() and point not in lowercase_visited and path.count(point) == 1:
                new_path = [p for p in path]
                new_path.append(point)
                path_points.append(tuple(new_path))
                lowercase_visited.append(tuple(new_path))
            elif point not in path:
                new_path = [p for p in path]
                new_path.append(point)
                path_points.append(tuple(new_path))


    return len(visited)


if __name__ == '__main__':

    puzzle_input = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

    with open('data/day12_input.txt') as f:
        puzzle_input = f.read().strip()

    print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part two answer: {part_two(puzzle_input)}')

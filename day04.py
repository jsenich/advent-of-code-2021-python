import numpy as np

from timer import print_time


@print_time
def part_one(puzzle_input: str) -> int:
    numbers, boards = extract_puzzle_input(puzzle_input)

    winning_num, winning_board = play_bingo(numbers, boards)
    if winning_board is None:
        return 0

    unmarked_sum = winning_board[winning_board != -1].sum()

    result = unmarked_sum * winning_num

    return result


@print_time
def part_two(puzzle_input: str) -> int:
    numbers, boards = extract_puzzle_input(puzzle_input)

    winning_boards = play_bingo_last_winner(numbers, boards)

    last_winning_num, winning_board = winning_boards[-1]
    unmarked_sum = winning_board[winning_board != -1].sum()

    result = unmarked_sum * last_winning_num

    return result


def play_bingo(numbers: list[int], boards: np.ndarray) -> tuple[int | None, np.ndarray | None]:
    marked_boards = np.copy(boards)

    for i, num in enumerate(numbers):
        for x, board in enumerate(boards):
            for y, row in enumerate(board):
                for z, column in enumerate(row):
                    if column == num:
                        marked_boards[x][y][z] = -1

                        if is_winning_board(marked_boards[x]):
                            return num, marked_boards[x]

    return None, None


def play_bingo_last_winner(numbers: list[int], boards: np.ndarray):
    marked_boards = np.copy(boards)
    winning_boards = []
    seen_winners = set()

    for i, num in enumerate(numbers):
        for x, board in enumerate(boards):
            if x in seen_winners:
                continue
            for y, row in enumerate(board):
                for z, column in enumerate(row):
                    if column == num:
                        marked_boards[x][y][z] = -1

                        if is_winning_board(marked_boards[x]):
                            if x not in seen_winners:
                                seen_winners.add(x)
                                winning_boards.append((num, marked_boards[x]))

    return winning_boards


def is_winning_board(board) -> bool:
    return -5 in np.sum(board, 0) or -5 in np.sum(board, 1)


def extract_puzzle_input(puzzle_input: str) -> tuple[list[int], np.ndarray]:
    drawn_numbers = []
    boards = []

    board = []
    puzzle_lines = puzzle_input.split("\n")
    puzzle_lines.append('')
    for i, line in enumerate(puzzle_lines):
        if i == 0:
            drawn_numbers.extend(int(n) for n in line.split(",") if line)
            continue

        if not line:
            if board:
                boards.append(board)
                board = []
            continue

        board.append([int(n) for n in line.split()])

    return drawn_numbers, np.array(boards)


if __name__ == '__main__':
    with open('data/day04_input.txt') as f:
        puzzle_input = f.read().strip()

    print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part two answer: {part_two(puzzle_input)}')

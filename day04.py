import numpy as np


def part_one(puzzle_input):
    numbers, boards = extract_puzzle_input(puzzle_input)

    winning_num, winning_board = play_bingo(numbers, boards)

    unmarked_sum = 0
    for line in winning_board:
        unmarked_sum += sum(n for n in line if n != -1)

    result = unmarked_sum * winning_num

    return result

def part_two(puzzle_input):
    numbers, boards = extract_puzzle_input(puzzle_input)

    winning_boards = play_bingo_last_winner(numbers, boards)

    unmarked_sum = 0
    last_winning_num, winning_board = winning_boards[-1]
    for line in winning_board:
        unmarked_sum += sum(n for n in line if n != -1)

    result = unmarked_sum * last_winning_num

    return result



def play_bingo(numbers, boards):
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


def play_bingo_last_winner(numbers, boards):
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


def extract_puzzle_input(puzzle_input):
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

#     test_input = """
# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7

# """


    # puzzle_input = test_input.strip()
    with open('data/day04_input.txt') as f:
        puzzle_input = f.read().strip()

    print(f'part one answer: {part_one(puzzle_input)}')
    print(f'part two answer: {part_two(puzzle_input)}')

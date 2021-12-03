def solve(board):
    board_size = range(board)

    for row in board_size:
        for col in board_size:
            value = 1
            check_if_valid(value)

            if board[row][col] == 0:
                board[row][col] = value
            else:
                value += 1


# Checks if value is allowed to be in the current square (row/col)
def check_if_valid(value, row_of_value, col_of_value, board):

    # Check if number already exists in the same row
    for col in board[row_of_value]:
        if value == col:
            return False

    # Check if the number already exists in the same column
    for row in board:
        if value == row[col_of_value]:
            return False

    # TODO Check if number is already in the allowed square

    return True


test_board = [[5, 0, 7, 6, 1, 0, 0, 3, 4],
              [2, 8, 9, 0, 0, 4, 0, 0, 0],
              [3, 4, 6, 2, 0, 5, 0, 9, 0],
              [6, 0, 2, 0, 0, 0, 0, 1, 0],
              [0, 3, 8, 0, 0, 6, 0, 4, 7],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 9, 0, 0, 0, 0, 0, 7, 8],
              [7, 0, 3, 4, 0, 0, 5, 6, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(check_if_valid(1, 0, 4, test_board))
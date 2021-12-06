def solve(board):

    for row in range(len(board)):
        for col in range(len(board)):
            for number in range(1, 9):
                if check_if_valid(number, row, col, board):
                    board[row][col] = number


# Checks if value is allowed to be in the current square (row/col)
def check_if_valid(value, row_of_value, col_of_value, board):

    if board[row_of_value][col_of_value] != 0:
        return False

    # Check if number already exists in the same row
    for col in board[row_of_value]:
        if value == col:
            return False

    # Check if the number already exists in the same column
    for row in board:
        if value == row[col_of_value]:
            return False

    # Check if number is already in the allowed square
    start_row = row_of_value - (row_of_value % 3)
    start_col = col_of_value - (col_of_value % 3)
    for row in range(start_row, start_row + 3):
        for col in range(start_col, start_col + 3):
            if value == board[row][col]:
                return False

    return True


test_board = [[2, 9, 0, 0, 0, 0, 0, 7, 0],
              [3, 0, 6, 0, 0, 8, 4, 0, 0],
              [8, 0, 0, 0, 4, 0, 0, 0, 2],
              [0, 2, 0, 0, 3, 1, 0, 0, 7],
              [0, 0, 0, 0, 8, 0, 0, 0, 0],
              [1, 0, 0, 9, 5, 0, 0, 6, 0],
              [7, 0, 0, 0, 9, 0, 0, 0, 1],
              [0, 0, 1, 2, 0, 0, 3, 0, 6],
              [0, 3, 0, 0, 0, 0, 0, 5, 9]]

solve(test_board)
for row in test_board:
    print(row)

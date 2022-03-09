def get_next_empty_box(puzzle):
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == -1:
                return row, column
    return None, None


def is_valid(puzzle, row, column, guess):
    # Check the row to see if the number is already there
    for i in range(9):
        if puzzle[row][i] == guess:
            return False

    # Check the column to see if the number is already there
    for i in range(9):
        if puzzle[i][column] == guess:
            return False

    # Check if the guess is alerady in the box
    starting_row_index = (row // 3) * 3
    starting_column_index = (column // 3) * 3
    for r in range(3):
        for c in range(3):
            if puzzle[starting_row_index + r][starting_column_index + c] == guess:
                return False
    return True


def sudoku_solver(puzzle):
    row, column = get_next_empty_box(puzzle)

    # Sudoku is already solved
    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, row, column, guess):
            puzzle[row][column] = guess
            if sudoku_solver(puzzle):
                return True

        # The guess is not valid
        puzzle[row][column] = -1
    return False


def print_sudoku(board):
    print("-" * 37)
    for i, row in enumerate(board):
        print(
            ("|" + " {}   {}   {} |" * 3).format(*[x if x != -1 else " " for x in row])
        )
        if i == 8:
            print("-" * 37)
        elif i % 3 == 2:
            print("|" + "---+" * 8 + "---|")
        else:
            print("|" + "   +" * 8 + "   |")


if __name__ == "__main__":
    to_solve = [
        [-1, 4, 1, 2, 3, -1, -1, -1, -1],
        [-1, 3, 5, -1, -1, 1, -1, -1, 2],
        [-1, -1, -1, -1, 5, 6, 3, 7, -1],
        [8, 5, -1, 3, -1, -1, 6, -1, 9],
        [1, -1, 9, -1, -1, 5, -1, 8, 3],
        [3, -1, -1, 1, -1, 9, -1, -1, -1],
        [-1, -1, 7, 9, 6, -1, -1, -1, -1],
        [4, -1, -1, 8, 7, -1, 9, 2, -1],
        [9, -1, 3, -1, 1, -1, 4, -1, 7],
    ]
    print_sudoku(to_solve)
    print(sudoku_solver(to_solve))
    print_sudoku(to_solve)

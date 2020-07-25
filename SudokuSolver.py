"""
A python script to solve 9x9 Sudoku problems using the backtracking algorithm.
Author : Vedant Raghuwanshi
Contact : raghuvedant00@gmail.com | www.linkedin.com/in/vedantraghuwanshi

"""
from SudokuGenerator import sudoku_generator


def sudoku_solve(grid):
    """
    To solve sudoku problem using backtracking algorithm
    :param grid: 9x9 grid ( 2D list of integers)
    :return: solved grid

    """
    empty_cell = is_vacant(grid)
    if empty_cell:
        row, col = empty_cell
    else:
        return True

    for i in range(1, len(grid)+1):
        if is_valid(grid, (row, col), i):
            grid[row][col] = i

            if sudoku_solve(grid):  # using recursion
                return True

            grid[row][col] = 0  # backtracking for another solution

    return False


def is_valid(grid, cell, num):
    """
    Returns if the move is valid
    :param grid: 9x9 grid ( 2D list of integers)
    :param cell: (row, col)
    :param num: int
    :return: bool

    """

    # if valid in row
    for i in range(len(grid)):
        if grid[cell[0]][i] == num and cell[1] != i:
            return False

    # if valid in column
    for i in range(len(grid)):
        if grid[i][cell[1]] == num and cell[1] != i:
            return False

    # if valid for 3x3 box
    xgrid = cell[1] // 3
    ygrid = cell[0] // 3

    for i in range(ygrid * 3, ygrid * 3 + 3):
        for j in range(xgrid * 3, xgrid * 3 + 3):
            if grid[i][j] == num and (i, j) != cell:
                return False

    return True


def is_vacant(grid):
    """
    finds an empty cell in the grid
    :param grid: 9x9 grid ( 2D list of integers)
    :return: (int, int) row, col

    """

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return i, j

    return None


def pretty_print(grid):
    """
    prints solved grid in pretty manner
    :param grid: 9x9 grid ( 2D list of integers)
    :return: None

    """

    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("+ + + + + + + + + + + +")
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(f"{grid[i][j]} ", end="")


if __name__ == "__main__":
    # grid = [
    #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
    #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #     [0, 0, 0, 0, 8, 0, 0, 7, 9]
    # ]

    grid = sudoku_generator()

    sudoku_solve(grid)
    pretty_print(grid)













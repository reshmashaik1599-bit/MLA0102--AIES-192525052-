# Q2_NQueens.py
# AI & Expert Systems
# 12-Queens Problem using Backtracking

N = 12

board = [[0 for _ in range(N)] for _ in range(N)]


def is_safe(row, col):
    # Check left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve(col):
    if col >= N:
        return True

    for row in range(N):
        if is_safe(row, col):
            board[row][col] = 1

            if solve(col + 1):
                return True

            board[row][col] = 0

    return False


if solve(0):
    print("\n12-Queens Solution Found!\n")

    for row in board:
        for cell in row:
            if cell == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

    print("\nAll 12 Queens are placed successfully with no conflicts.")
else:
    print("No solution exists.")
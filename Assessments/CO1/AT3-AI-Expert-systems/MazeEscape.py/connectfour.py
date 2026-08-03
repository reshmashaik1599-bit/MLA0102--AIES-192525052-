import random

ROWS = 6
COLS = 7

# Create board
board = [[" " for _ in range(COLS)] for _ in range(ROWS)]


def print_board():
    print("\n 0 1 2 3 4 5 6")
    for row in board:
        print("|" + "|".join(row) + "|")
    print("-" * 15)


def is_valid(col):
    return board[0][col] == " "


def get_next_row(col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            return row


def drop_piece(row, col, piece):
    board[row][col] = piece


def check_winner(piece):

    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == piece for i in range(4)):
                return True

    # Vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r + i][c] == piece for i in range(4)):
                return True

    # Diagonal \
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True

    # Diagonal /
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True

    return False


def board_full():
    for c in range(COLS):
        if board[0][c] == " ":
            return False
    return True


print("========== CONNECT FOUR ==========")
print("Player = X")
print("Computer = O")

while True:

    print_board()

    # Player Move
    try:
        col = int(input("Enter column (0-6): "))
    except ValueError:
        print("Enter a valid number!")
        continue

    if col < 0 or col >= COLS or not is_valid(col):
        print("Invalid Move!")
        continue

    row = get_next_row(col)
    drop_piece(row, col, "X")

    if check_winner("X"):
        print_board()
        print("\nCongratulations! You Win!")
        break

    if board_full():
        print_board()
        print("\nGame Draw!")
        break

    # Computer Move
    valid_cols = [c for c in range(COLS) if is_valid(c)]
    ai_col = random.choice(valid_cols)

    ai_row = get_next_row(ai_col)
    drop_piece(ai_row, ai_col, "O")

    print(f"\nComputer chooses column {ai_col}")

    if check_winner("O"):
        print_board()
        print("\nComputer Wins!")
        break

    if board_full():
        print_board()
        print("\nGame Draw!")
        break
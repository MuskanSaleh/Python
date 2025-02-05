# Tic-Tac-Toe Game in Python

def print_board(board):
    """Function to print the Tic-Tac-Toe board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """Function to check if a player has won"""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Check rows
            return True
        if all(board[j][i] == player for j in range(3)):  # Check columns
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    """Check if the board is full (draw)"""
    return all(board[i][j] != " " for i in range(3) for j in range(3))


def tic_tac_toe():
    """Main function to play Tic-Tac-Toe"""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player = players[turn % 2]
        print(f"Player {player}'s turn. Enter row and column (0, 1, 2):")

        while True:
            try:
                row, col = map(int, input().split())
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("Cell already occupied! Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Enter row and column (0, 1, 2):")

        print_board(board)

        if check_winner(board, player):
            print(f"🎉 Player {player} wins! 🎉")
            break

        if is_full(board):
            print("It's a draw! 🤝")
            break

        turn += 1


# Run the game
tic_tac_toe()

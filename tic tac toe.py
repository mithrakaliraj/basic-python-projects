import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def player_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (row[1-3] column[1-3]): ")
        try:
            row, col = map(int, move.split())
            if 1 <= row <= 3 and 1 <= col <= 3 and board[row-1][col-1] == ' ':
                board[row-1][col-1] = player
                break
            else:
                print("Invalid move! Please try again.")
        except ValueError:
            print("Invalid input! Please enter row and column numbers separated by space.")

def computer_move(board, player):
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = player
            break

def play_game():
    board = [[' ']*3 for _ in range(3)]
    players = ['X', 'O']
    current_player = random.choice(players)

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        if current_player == 'X':
            player_move(board, current_player)
        else:
            computer_move(board, current_player)

        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        current_player = 'X' if current_player == 'O' else 'O'

if __name__ == "__main__":
    play_game()

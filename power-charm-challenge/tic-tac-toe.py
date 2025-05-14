def print_board(board):
    for r in board:
        print(" | ".join(r))
        print("-" * 5)


def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def board_full(board):
    return all(c != " " for r in board for c in r)


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Tic-Tac-Toe Game")
    print_board(board)
    for turn in range(9):
        current_player = players[turn % 2]
        r, c = get_player_move(current_player, board)
        board[r][c] = current_player
        print_board(board)
        if check_win(board, current_player):
            print_winner(current_player)
            return
        if board_full(board):
            print_winner(None)
            return
    print_winner(None)


def get_player_move(current_player, board):
    while True:
        try:
            r, c = map(int, input(f"P {current_player}, row col (0-2): ").split())
            if 0 <= r <= 2 and 0 <= c <= 2:
                if board[r][c] == " ":
                    return r, c
                else:
                    print("That spot is taken. Try again.")
            else:
                print("Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input. Enter two numbers between 0 and 2.")

def print_winner(winner):
    if winner:
        print(f"P {winner} wins!")
    else:
        print("Draw!")
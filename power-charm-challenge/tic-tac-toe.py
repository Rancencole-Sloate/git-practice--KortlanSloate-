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
        while 1:
            try:
                r, c = map(int, input(f"P {current_player}, row col (0-2): ").split())
                if board[r][c] == " ":
                    board[r][c] = current_player
                    break
                else:
                    print("Nope. Again.")
            except ValueError:
                print("Wrong. 0-2 pls.")
        print_board(board)
        if check_win(board, current_player):
            print(f"P {current_player} wins!")
            return
        if board_full(board):
            print("Draw!")
            return
    print("Draw!")


def get_player_move():
    print_winner()


def print_winner(player):
    handle_invalid_input()


def handle_invalid_input():
    play_game()


get_player_move()
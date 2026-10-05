
WINNING_COMBINATIONS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
def game_state(board):
    for combination in WINNING_COMBINATIONS:
        if all(board[i] == 1 for i in combination):
            return 1
        if all(board[i] == -1 for i in combination):
            return -1
    if 0 in board:
        return -2
    return 0
def search(board, player, turn):
    state = game_state(board)
    if state != -2:
        return state * player, -1
    best_moves = [-2]
    for cell in range(len(board)):
        if board[cell] == 0:
            board[cell] = player
            value = -search(board, -player, turn + 1)[0]
            if value > best_moves[0]:
                best_moves = [value, cell]
            elif value == best_moves[0]:
                best_moves.append(cell)
            board[cell] = 0
    return best_moves
def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])
board = [0] * 9
player = 1
result = search(board, player, 0)
winner = result[0] * player
if player == 1:
    print("Player 1 starts.")
elif player == -1:
    print("Player 2 starts.")
if winner == 0:
    print("It's a draw!")
else:
    winner_number = int(winner * -0.5 + 1.5)
    print("Player", winner_number, "wins!")
if winner != -player:
    print("You can play on cell", result[1] + 1)
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = -1
DRAW = 0
WINNING_COMBINATIONS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
def game_state(board):
    for combination in WINNING_COMBINATIONS:
        if board[combination[0]] == PLAYER_1 and \
           board[combination[1]] == PLAYER_1 and \
           board[combination[2]] == PLAYER_1:
            return PLAYER_1
        elif board[combination[0]] == PLAYER_2 and \
             board[combination[1]] == PLAYER_2 and \
             board[combination[2]] == PLAYER_2:
            return PLAYER_2
    if EMPTY in board:
        return -2
    return DRAW
def search(board, player, depth):
    state = game_state(board)
    if state != -2:
        return [state * player, -1]
    best_moves = [-2]
    for cell in range(len(board)):
        if board[cell] == EMPTY:
            board[cell] = player
            value = -search(board, -player, depth + 1)[0]
            if value > best_moves[0]:
                best_moves = [value, cell]
            elif value == best_moves[0]:
                best_moves.append(cell)
            board[cell] = EMPTY
    return best_moves
def print_winner_message(winner):
    if winner == DRAW:
        print("It's a draw!")
    else:
        winner_number = 1 if winner == PLAYER_1 else 2
        print(f"Player {winner_number} wins!")
def main():
    board = [EMPTY] * 9
    current_player = PLAYER_1
    print(f"Player {current_player} starts.")
    result = search(board, current_player, 0)
    winner = result[0] * current_player
    print_winner_message(winner)
    possible_moves = ', '.join(str(pos + 1) for pos in result[1:])
    print("You can play in position(s): " + possible_moves)
if __name__ == "__main__":
    main()
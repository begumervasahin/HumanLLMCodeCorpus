
board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]
current_player = 1
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
def evaluate_game_state(board):
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == 1:
            return 1
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == -1:
            return -1
    if 0 in board:
        return -2
    return 0
def search_best_move(board, player, depth):
    state = evaluate_game_state(board)
    if state != -2:
        return (state * player, -1)
    best_moves = [-2]
    for index in range(len(board)):
        if board[index] == 0:
            board[index] = player
            value = -search_best_move(board, -player, depth + 1)[0]
            if value > best_moves[0]:
                best_moves = [value, index]
            elif value == best_moves[0]:
                best_moves.append(index)
            board[index] = 0
    return best_moves
def main():
    result = search_best_move(board, current_player, 0)
    winner = result[0] * current_player
    if current_player == 1:
        print("Player 1 starts.")
    elif current_player == -1:
        print("Player 2 starts.")
    if winner == 0:
        print("It's a draw!")
    else:
        winner_number = 1 if winner == 1 else 2
        print(f"Player {winner_number} wins!")
    if winner != -current_player:
        possible_moves = ", ".join(str(move + 1) for move in result[1:])
        print(f"You can play at positions: {possible_moves}")
if __name__ == '__main__':
    main()
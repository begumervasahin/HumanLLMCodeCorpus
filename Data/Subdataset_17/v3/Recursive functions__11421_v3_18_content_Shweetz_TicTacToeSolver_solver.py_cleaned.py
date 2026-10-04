
board = [0] * 9
current_player = 1
winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]
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
    best_score = -2
    best_moves = []
    for index in range(len(board)):
        if board[index] == 0:
            board[index] = player
            score = -search_best_move(board, -player, depth + 1)[0]
            board[index] = 0
            if score > best_score:
                best_score = score
                best_moves = [index]
            elif score == best_score:
                best_moves.append(index)
    return (best_score, best_moves)
def main():
    print(f"Player {1 if current_player == 1 else 2} starts.")
    result = search_best_move(board, current_player, 0)
    winner = result[0] * current_player
    if winner == 0:
        print("It's a draw!")
    else:
        winner_number = 1 if winner == 1 else 2
        print(f"Player {winner_number} wins!")
    if winner == -2:
        possible_moves = ", ".join(str(move + 1) for move in result[1])
        print(f"You can play at positions: {possible_moves}")
if __name__ == '__main__':
    main()
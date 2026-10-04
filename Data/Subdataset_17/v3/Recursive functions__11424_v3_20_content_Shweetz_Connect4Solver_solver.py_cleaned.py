
board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 1, -1, 0, 0],
         [1, -1, 1, -1, 0]]
MAX_DEPTH = 15
MAX_LOG = 0
branch_count = 0
current_player = -1
def evaluate_game_state(board, cell_x, cell_y):
    player = board[cell_x][cell_y]
    if player == 0:
        return -2
    x, y = cell_x, cell_y
    while x > 0 and board[x - 1][y] == player:
        x -= 1
    vertical_count = 0
    while x < len(board) and board[x][y] == player:
        vertical_count += 1
        x += 1
    if vertical_count >= 4:
        return player
    x, y = cell_x, cell_y
    while y > 0 and board[x][y - 1] == player:
        y -= 1
    horizontal_count = 0
    while y < len(board[0]) and board[x][y] == player:
        horizontal_count += 1
        y += 1
    if horizontal_count >= 4:
        return player
    x, y = cell_x, cell_y
    while x < len(board) - 1 and y > 0 and board[x + 1][y - 1] == player:
        x += 1
        y -= 1
    diagonal1_count = 0
    while x >= 0 and y < len(board[0]) and board[x][y] == player:
        diagonal1_count += 1
        x -= 1
        y += 1
    if diagonal1_count >= 4:
        return player
    x, y = cell_x, cell_y
    while x > 0 and y > 0 and board[x - 1][y - 1] == player:
        x -= 1
        y -= 1
    diagonal2_count = 0
    while x < len(board) and y < len(board[0]) and board[x][y] == player:
        diagonal2_count += 1
        x += 1
        y += 1
    if diagonal2_count >= 4:
        return player
    if board[0][-1] == 0:
        return -2
    for row in board:
        if 0 in row:
            return -2
    return 0
def search_best_move(board, player, cell_x, cell_y, depth):
    state = evaluate_game_state(board, cell_x, cell_y)
    if state != -2:
        if depth < MAX_LOG:
            print("\t" * depth + "endState: " + str(state))
        return (state * player, -1, -1)
    if depth >= MAX_DEPTH:
        return (0, -1, -1)
    best_score = -2
    best_moves = []
    for y in range(len(board[0])):
        if board[0][y] != 0:
            continue
        x = len(board) - 1
        while board[x][y] != 0:
            x -= 1
        board[x][y] = player
        global branch_count
        branch_count += 1
        score = -search_best_move(board, -player, x, y, depth + 1)[0]
        board[x][y] = 0
        if score > best_score:
            best_score = score
            best_moves = [y]
        elif score == best_score:
            best_moves.append(y)
    return (best_score, best_moves)
def main():
    result = search_best_move(board, current_player, 0, 0, 0)
    winner = result[0] * current_player
    print(f"Number of branches explored: {branch_count}")
    if current_player == 1:
        print("Player 1 starts.")
    else:
        print("Player 2 starts.")
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
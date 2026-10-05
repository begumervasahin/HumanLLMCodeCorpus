
initial_board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, -1, 0, 0],
    [1, -1, 1, -1, 0]
]
max_depth = 15
max_log = 0
explored_branches = 0
player = -1
def check_game_state(board, cellx, celly):
    player = board[cellx][celly]
    if player == 0:
        return -2
    def check_line(dx, dy):
        count = 0
        while 0 <= cellx + dx < len(board) and 0 <= celly + dy < len(board[0]) and board[cellx + dx][celly + dy] == player:
            count += 1
            cellx += dx
            celly += dy
        return count
    for dx, dy in [(0, 1), (1, 0), (1, 1), (1, -1)]:
        line_count = 1 + check_line(dx, dy) + check_line(-dx, -dy)
        if line_count >= 4:
            return player
    if all(board[0][j] != 0 for j in range(len(board[0]))):
        return -1
    return 0
def search(board, player, cellx, celly, depth):
    state = check_game_state(board, cellx, celly)
    if state != -2:
        return (state * player, -1, -1)
    if depth == 0:
        return (0, -1, -1)
    best_score = float('-inf') if player == 1 else float('inf')
    best_moves = []
    for celly in range(len(board[0])):
        if board[0][celly] != 0:
            continue
        cellx = len(board) - 1
        while board[cellx][celly] != 0:
            cellx -= 1
        board[cellx][celly] = player
        global explored_branches
        explored_branches += 1
        score, _, _ = search(board, -player, cellx, celly, depth - 1)
        board[cellx][celly] = 0
        if player == 1:
            if score > best_score:
                best_score = score
                best_moves = [celly]
            elif score == best_score:
                best_moves.append(celly)
        else:
            if score < best_score:
                best_score = score
                best_moves = [celly]
            elif score == best_score:
                best_moves.append(celly)
    return best_score * player, best_moves[0], best_moves[1:]
score, best_move, other_moves = search(initial_board, player, 0, 0, max_depth)
print("Number of branches explored:", explored_branches)
if player == 1:
    print("Player 1 starts.")
elif player == -1:
    print("Player 2 starts.")
if score == 0:
    print("It's a draw!")
else:
    winner_number = 1 if score > 0 else 2
    print("Player", winner_number, "wins!")
    print("You can play", best_move + 1, end='')
    for move in other_moves:
        print(",", move + 1, end='')
    print()
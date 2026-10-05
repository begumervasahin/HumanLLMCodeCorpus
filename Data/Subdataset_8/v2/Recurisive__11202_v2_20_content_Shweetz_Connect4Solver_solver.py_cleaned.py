
game_board = [[0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 1, -1, 0, 0],
              [1, -1, 1, -1, 0]]
max_depth = 15
max_log = 0
branches_explored = 0
current_player = -1
def game_state(board, x, y):
    player = board[x][y]
    if player == 0:
        return -2
    vertical = 0
    for i in range(len(board)):
        if board[i][y] == player:
            vertical += 1
        else:
            vertical = 0
        if vertical >= 4:
            return player
    horizontal = 0
    for j in range(len(board[0])):
        if board[x][j] == player:
            horizontal += 1
        else:
            horizontal = 0
        if horizontal >= 4:
            return player
    diagonal1 = 0
    for i, j in zip(range(x, -1, -1), range(y, len(board[0]))):
        if board[i][j] == player:
            diagonal1 += 1
        else:
            diagonal1 = 0
        if diagonal1 >= 4:
            return player
    diagonal2 = 0
    for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
        if board[i][j] == player:
            diagonal2 += 1
        else:
            diagonal2 = 0
        if diagonal2 >= 4:
            return player
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return -2
    return 0
def minimax(board, player, x, y, depth):
    global branches_explored
    state = game_state(board, x, y)
    if state != -2:
        if depth < max_log:
            print("\t" * depth + "End State: " + str(state))
        return (state * player, -1, -1)
    if depth > max_depth - 1:
        return (0, -1, -1)
    best_moves = [-2]
    for y in range(len(board[0])):
        if board[0][y] != 0:
            continue
        x = len(board) - 1
        while board[x][y] != 0:
            x -= 1
        board[x][y] = player
        branches_explored += 1
        val = -minimax(board, -player, x, y, depth + 1)[0]
        if val > best_moves[0]:
            best_moves = [val, y]
        elif val == best_moves[0]:
            best_moves.append(y)
        board[x][y] = 0
    return best_moves
result = minimax(game_board, current_player, 0, 0, 0)
winner = result[0] * current_player
print("Number of Branches Explored: " + str(branches_explored))
if current_player == 1:
    print("Player 1 Starts.")
elif current_player == -1:
    print("Player 2 Starts.")
if winner == 0:
    print("It's a Draw!")
else:
    winner_number = int(winner * -0.5 + 1.5)
    print("Player " + str(winner_number) + " Wins!")
possible_moves_str = str(result[1] + 1)
for i in range(2, len(result)):
    possible_moves_str += ", " + str(result[i] + 1)
if winner != -current_player:
    print("You Can Play: " + possible_moves_str)
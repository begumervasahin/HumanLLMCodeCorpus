tab = [[0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 1, -1, 0, 0],
       [1, -1, 1, -1, 0]]
MAX_DEPTH = 15
MAX_LOG = 0
branch_count = 0
player = -1
def game_state(tab, cellx, celly):
    current_player = tab[cellx][celly]
    if current_player == 0:
        return -2
    def check_direction(dx, dy):
        x, y = cellx, celly
        count = 0
        while 0 <= x < len(tab) and 0 <= y < len(tab[0]) and tab[x][y] == current_player:
            count += 1
            x += dx
            y += dy
        return count
    if check_direction(1, 0) + check_direction(-1, 0) - 1 >= 4:
        return current_player
    if check_direction(0, 1) + check_direction(0, -1) - 1 >= 4:
        return current_player
    if check_direction(1, -1) + check_direction(-1, 1) - 1 >= 4:
        return current_player
    if check_direction(1, 1) + check_direction(-1, -1) - 1 >= 4:
        return current_player
    if all(cell != 0 for row in tab for cell in row):
        return 0
    return -2
def search(tab, player, cellx, celly, depth):
    state = game_state(tab, cellx, celly)
    if state != -2:
        if depth < MAX_LOG:
            print("\t" * depth + "endState: " + str(state))
        return state * player, -1, -1
    if depth >= MAX_DEPTH:
        return 0, -1, -1
    best_moves = [-2]
    for celly in range(len(tab[0])):
        if tab[0][celly] != 0:
            continue
        cellx = len(tab) - 1
        while tab[cellx][celly] != 0:
            cellx -= 1
        tab[cellx][celly] = player
        global branch_count
        branch_count += 1
        val = -search(tab, -player, cellx, celly, depth + 1)[0]
        if val > best_moves[0]:
            best_moves = [val, celly]
        elif val == best_moves[0]:
            best_moves.append(celly)
        tab[cellx][celly] = 0
    return best_moves
def main():
    res = search(tab, player, 0, 0, 0)
    winner = res[0] * player
    print(f"Number of branches explored: {branch_count}")
    if player == 1:
        print("Player 1 starts.")
    elif player == -1:
        print("Player 2 starts.")
    if winner == 0:
        print("It's a draw!")
    else:
        winner_number = int(winner * -0.5 + 1.5)
        print(f"Player {winner_number} wins!")
    if winner != -player:
        possible_moves = ", ".join(str(c + 1) for c in res[1:])
        print(f"You can play {possible_moves}")
if __name__ == "__main__":
    main()

tab = [0] * 9
player = 1
win = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]
def game_state(tab):
    for combo in win:
        if tab[combo[0]] == tab[combo[1]] == tab[combo[2]] == 1:
            return 1
        if tab[combo[0]] == tab[combo[1]] == tab[combo[2]] == -1:
            return -1
    if 0 in tab:
        return -2
    return 0
def search(tab, player, t):
    state = game_state(tab)
    if state != -2:
        return (state * player, -1)
    best_moves = [-2]
    for cell in range(len(tab)):
        if tab[cell] == 0:
            tab[cell] = player
            val = -search(tab, -player, t + 1)[0]
            if val > best_moves[0]:
                best_moves = [val, cell]
            elif val == best_moves[0]:
                best_moves.append(cell)
            tab[cell] = 0
    return best_moves
res = search(tab, player, 0)
winner = res[0] * player
if player == 1:
    print("Player 1 starts.")
else:
    print("Player 2 starts.")
if winner == 0:
    print("It's a draw!")
else:
    winner_number = int(winner * -0.5 + 1.5)
    print(f"Player {winner_number} wins!")
possible_moves = ", ".join(str(move + 1) for move in res[1:])
if winner != -player:
    print(f"You can play {possible_moves}")
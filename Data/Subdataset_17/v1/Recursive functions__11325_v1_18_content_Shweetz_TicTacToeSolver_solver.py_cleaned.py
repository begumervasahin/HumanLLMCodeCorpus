
tab = [0, 0, 0,
       0, 0, 0,
       0, 0, 0]
player = 1
win = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
       (0, 3, 6), (1, 4, 7), (2, 5, 8),
       (0, 4, 8), (2, 4, 6)]
def gameState(tab):
    for i in win:
        if tab[i[0]] == 1 and tab[i[1]] == 1 and tab[i[2]] == 1:
            return 1
        if tab[i[0]] == -1 and tab[i[1]] == -1 and tab[i[2]] == -1:
            return -1
    if tab[8] == 0:
        return -2
    for i in tab:
        if i == 0:
            return -2
    return 0
def search(tab, player, t):
    state = gameState(tab)
    if state != -2:
        return (state * player, -1)
    list_best = [-2]
    for cell in range(len(tab)):
        if tab[cell] == 0:
            tab[cell] = player
            val = -search(tab, -player, t + 1)[0]
            if val > list_best[0]:
                list_best = [val, cell]
            elif val == list_best[0]:
                list_best.append(cell)
            tab[cell] = 0
    return list_best
res = search(tab, player, 0)
winner = res[0] * player
if player == 1:
    print("Player 1 start.")
elif player == -1:
    print("Player 2 start.")
if winner == 0:
    print("It's a draw!")
else:
    winner_number = int(winner * -0.5 + 1.5)
    print("Player " + str(winner_number) + " wins!")
str_poss = str(res[1] + 1)
for i in range(2, len(res)):
    str_poss += ", " + str(res[i] + 1)
if winner != -player:
    print("You can play " + str_poss)
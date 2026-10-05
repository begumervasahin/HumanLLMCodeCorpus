from constantes import *
import random as r
def fonk1(player_grid, official_draw, win_history, gains):
    b1 = fonk2(player_grid, official_draw)
    b2 = player_grid[NB_BOULES_NORMALES] == official_draw[NB_BOULES_NORMALES]
    if b1 = = 5 and b2:
        win_history[0][1] += 1
        gains += win_history[0][0]
    elif b1 = = 5:
        win_history[1][1] += 1
        gains += win_history[1][0]
    elif b1 = = 4 and b2:
        win_history[2][1] += 1
        gains += win_history[2][0]
    elif b1 = = 4:
        win_history[3][1] += 1
        gains += win_history[3][0]
    elif b1 = = 3 and b2:
        win_history[4][1] += 1
        gains += win_history[4][0]
    elif b1 = = 3:
        win_history[5][1] += 1
        gains += win_history[5][0]
    elif b1 = = 2 and b2:
        win_history[6][1] += 1
        gains += win_history[6][0]
    elif b1 = = 2:
        win_history[7][1] += 1
        gains += win_history[7][0]
    elif b1 = = 1 and b2:
        win_history[8][1] += 1
        gains += win_history[8][0]
    elif b2:
        win_history[8][1] += 1
        gains += win_history[8][0]
    return win_history, gains
def fonk2(player_grid, official_draw):
    b1 = 0
    for g in range(NB_BOULES_NORMALES):
        for t in range(NB_BOULES_NORMALES):
            if player_grid[g] == official_draw[t]:
                b1 += 1
    return b1
def fonk3():
    return [
        [JACKPOT, 0],
        [100000, 0],
        [1000, 0],
        [500, 0],
        [50, 0],
        [20, 0],
        [10, 0],
        [5, 0],
        [MISE, 0],
    ]
def fonk4(official_draw, ball_history):
    for i in range(NB_BOULES_NORMALES):
        ball_history[0][official_draw[i] - 1][1] += 1
    ball_history[1][official_draw[NB_BOULES_NORMALES] - 1][1] += 1
    return ball_history
def fonk5():
    return [
        [[i, 0] for i in range(NUM_BOULE_MIN, NUM_BOULE_MAX_NORMAL + 1)],
        [[i, 0] for i in range(NUM_BOULE_MIN, NUM_BOULE_MAX_COMP + 1)]
    ]
def fonk6(ball_history):
    b3 = [
        sorted(ball_history[0], b4 = lambda x: x[1], reverse=True),
        sorted(ball_history[1], b4 = lambda x: x[1], reverse=True)
    ]
    return b3
def fonk7(b3):
    b5 = [item[0] for item in b3[0][:NB_BOULES_NORMALES]]
    b5.append(b3[1][0][0])
    b6 = [item[0] for item in b3[0][-NB_BOULES_NORMALES:][::-1]]
    b6.append(b3[1][-1][0])
    return b5, b6
def fonk8():
    b7 = []
    while len(b7) < NB_BOULES_NORMALES:
        b8 = r.randint(NUM_BOULE_MIN, NUM_BOULE_MAX_NORMAL)
        if b8 not in b7:
            b7.append(b8)
    b7.append(r.randint(NUM_BOULE_MIN, NUM_BOULE_MAX_COMP))
    return b7
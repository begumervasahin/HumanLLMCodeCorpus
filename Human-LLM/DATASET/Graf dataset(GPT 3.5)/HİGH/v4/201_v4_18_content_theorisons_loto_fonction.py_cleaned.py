from constantes import *
import random as r
def fonk1(player_grid, official_draw, b2, gains):
    a1 = 0
    b1 = False
    for g in range(NB_BOULES_NORMALES):
        for t in range(NB_BOULES_NORMALES):
            if player_grid[g] == official_draw[t]:
                a1 += 1
    if player_grid[NB_BOULES_NORMALES] == official_draw[NB_BOULES_NORMALES]:
        b1 = True
    if a1 = = 5 and b1:
        b2[0][1] += 1
        gains += b2[0][0]
    elif a1 = = 5:
        b2[1][1] += 1
        gains += b2[1][0]
    elif a1 = = 4 and b1:
        b2[2][1] += 1
        gains += b2[2][0]
    elif a1 = = 4:
        b2[3][1] += 1
        gains += b2[3][0]
    elif a1 = = 3 and b1:
        b2[4][1] += 1
        gains += b2[4][0]
    elif a1 = = 3:
        b2[5][1] += 1
        gains += b2[5][0]
    elif a1 = = 2 and b1:
        b2[6][1] += 1
        gains += b2[6][0]
    elif a1 = = 2:
        b2[7][1] += 1
        gains += b2[7][0]
    elif a1 = = 1 and b1:
        b2[8][1] += 1
        gains += b2[8][0]
    elif b1:
        b2[8][1] += 1
        gains += b2[8][0]
    return b2, gains
def fonk2():
    b2 = [
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
    return b2
def fonk3(official_draw, b3):
    for b10 in range(NB_BOULES_NORMALES):
        b3[0][official_draw[b10] - 1][1] += 1
    b3[1][official_draw[NB_BOULES_NORMALES] - 1][1] += 1
    return b3
def fonk4():
    b3 = [
        [[b10, 0] for b10 in range(NUM_BOULE_MIN, NUM_BOULE_MAX_NORMAL + 1)],
        [[b10, 0] for b10 in range(NUM_BOULE_MIN, NUM_BOULE_MAX_COMP + 1)]
    ]
    return b3
def fonk5(b3):
    b4 = []
    b4 += [[[b10[0], b10[1]] for b10 in b3[0]]]
    b4 += [[[b10[0], b10[1]] for b10 in b3[1]]]
    b4[0].sort(b5 = sort_by_occurrence, reverse=True)
    b4[1].sort(b5 = sort_by_occurrence, reverse=True)
    return b4
def fonk6(val):
    return val[1]
def fonk7(b4):
    b6 = []
    b7 = []
    for b10 in range(NB_BOULES_NORMALES):
        b6.append(b4[0][b10][0])
    b6.append(b4[1][0][0])
    for b10 in range(NUM_BOULE_MAX_NORMAL - 1, NUM_BOULE_MAX_NORMAL - 1 - NB_BOULES_NORMALES, -1):
        b7.append(b4[0][b10][0])
    b7.append(b4[1][NUM_BOULE_MAX_COMP - 1][0])
    return b6, b7
def fonk8():
    b8 = []
    for b10 in range(NB_BOULES_NORMALES):
        b9 = r.randint(NUM_BOULE_MIN, NUM_BOULE_MAX_NORMAL)
        while fonk9(b8, b9):
            b9 = r.randint(NUM_BOULE_MIN, NUM_BOULE_MAX_NORMAL)
        b8.append(b9)
    b8.append(r.randint(NUM_BOULE_MIN, NUM_BOULE_MAX_COMP))
    return b8
def fonk9(grid, number):
    for b10 in grid:
        if b10 = = number:
            return True
    return False

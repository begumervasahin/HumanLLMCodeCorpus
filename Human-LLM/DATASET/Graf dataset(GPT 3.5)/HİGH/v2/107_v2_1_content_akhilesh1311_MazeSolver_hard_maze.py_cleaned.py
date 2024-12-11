import random
import copy
def fonk1(b15, b1 = False):
    b2 = []
    b3 = []
    b4 = set()
    b3.append((0, 0))
    b4.add((0, 0))
    b5 = {}
    while b3:
        cur_i, b6 = b3.pop(0)
        if b15[cur_i][b6] == 'G':
            a1 = 0
            while cur_i + b6:
                b2.append((cur_i, b6))
                cur_i, b6 = b5[(cur_i, b6)]
                a1 += 1
            if b1:
                for p, q in b2:
                    if b15[p][q] in ['O', 'X']:
                        b15[p][q] = ' '
                fonk3(b15)
                return
            else:
                return a1
        for i, j in [(cur_i - 1, b6), (cur_i + 1, b6), (cur_i, b6 - 1), (cur_i, b6 + 1)]:
            if 0 <= i < len(b15) and 0 <= j < len(b15) and b15[i][j] != 'X' and (i, j) not in b4:
                b3.append((i, j))
                b5[(i, j)] = (cur_i, b6)
                b4.add((i, j))
    return -1
def fonk2(b14):
    b7 = []
    for b16, b12 in enumerate(b14):
        b8 = fonk1(b12)
        b7.append((b8, random.random(), b16))
    b7.sort(b9 = True)
    return b7[0][-1]
def fonk3(b12):
    for row in b12:
        print(*row, b10 = ' ')
    print('\n')
if b11 = = '__main__':
    a2 = 15
    a3 = 0.3
    a4 = 100
    b12 = [['X' if random.random() < a3 else 'O' for _ in range(a2)] for _ in range(a2)]
    b12[0][0] = 'S'
    b12[a2 - 1][a2 - 1] = 'G'
    print("Displaying initial b12:")
    fonk3(b12)
    print("Displaying initial b12 with the shortest b2:")
    fonk1(b12, True)
    for i in range(a2):
        for j in range(a2):
            if b12[i][j] == ' ':
                b12[i][j] = 'O'
    x, b13 = random.randint(0, a2 - 1), random.randint(0, a2 - 1)
    for _ in range(a4):
        b14 = [b12]
        for i, j in [(x - 1, b13), (x + 1, b13), (x, b13 - 1), (x, b13 + 1)]:
            if 0 <= i < a2 and 0 <= j < a2 and b12[i][j] in ['O', 'X']:
                b15 = copy.deepcopy(b12)
                b15[i][j] = 'O' if b15[i][j] == 'X' else 'X'
                b14.append(b15)
        b16 = fonk2(b14)
        b12 = b14[b16]
        if b16:
            x, b13 = [(x - 1, b13), (x + 1, b13), (x, b13 - 1), (x, b13 + 1)][b16 - 1]
        else:
            x, b13 = random.randint(0, a2 - 1), random.randint(0, a2 - 1)
    print("Displaying b12 after hill climbing:")
    fonk3(b12)
    print("Displaying b12 with the shortest b2 after hill climbing:")
    fonk1(b12, True)
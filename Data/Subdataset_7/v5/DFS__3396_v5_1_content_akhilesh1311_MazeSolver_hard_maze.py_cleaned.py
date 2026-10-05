import random
import copy
def fonk1(b13, b1 = False):
    b2 = [(0, 0)]
    b3 = set(b2)
    b4 = {}
    b5 = []
    while b2:
        cur_i, b6 = b2.pop(0)
        if b13[cur_i][b6] == 'G':
            a1 = 0
            while (cur_i, b6) in b4:
                b5.append((cur_i, b6))
                cur_i, b6 = b4[(cur_i, b6)]
                a1 += 1
            if b1:
                for p, q in b5:
                    if b13[p][q] in ['O', 'X']:
                        b13[p][q] = ' '
                fonk3(b13)
                return
            else:
                return a1
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_i, b7 = cur_i + di, b6 + dj
            if 0 <= next_i < len(b13) and 0 <= b7 < len(b13[0]) and b13[next_i][b7] != 'X' and (next_i, b7) not in b3:
                b2.append((next_i, b7))
                b3.add((next_i, b7))
                b4[(next_i, b7)] = (cur_i, b6)
    return -1
def fonk2(b15):
    b8 = []
    for b17, b13 in enumerate(b15):
        b9 = fonk1(b13)
        b8.append((b9, random.random(), b17))
    b8.sort(b10 = True)
    return b8[0][-1]
def fonk3(b13):
    for row in b13:
        print(*row, b11 = ' ')
    print()
if b12 = = '__main__':
    a2 = 15
    a3 = 0.3
    a4 = 100
    b13 = [['X' if random.random() < a3 else 'O' for _ in range(a2)] for _ in range(a2)]
    b13[0][0] = 'S'
    b13[a2 - 1][a2 - 1] = 'G'
    print("Initial b13:")
    fonk3(b13)
    print("Shortest b5 in initial b13:")
    fonk1(b13, True)
    for i in range(a2):
        for j in range(a2):
            if b13[i][j] == ' ':
                b13[i][j] = 'O'
    x, b14 = random.randint(0, a2 - 1), random.randint(0, a2 - 1)
    for _ in range(a4):
        b15 = [b13]
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_i, b7 = x + di, b14 + dj
            if 0 <= next_i < a2 and 0 <= b7 < a2 and b13[next_i][b7] in ['O', 'X']:
                b16 = copy.deepcopy(b13)
                b16[next_i][b7] = 'O' if b16[next_i][b7] == 'X' else 'X'
                b15.append(b16)
        b17 = fonk2(b15)
        b13 = b15[b17]
        if b17:
            x, b14 = x + [-1, 1, 0, 0][b17 - 1], b14 + [0, 0, -1, 1][b17 - 1]
        else:
            x, b14 = random.randint(0, a2 - 1), random.randint(0, a2 - 1)
    print("Final b13 after hill climbing:")
    fonk3(b13)
    print("Shortest b5 in final b13 after hill climbing:")
    fonk1(b13, True)
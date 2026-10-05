import random
import copy
def fonk1(b16, b1 = False):
    b2 = []
    b3 = []
    b4 = set()
    b3.append((0, 0))
    b4.add((0, 0))
    b5 = {}
    while b3:
        cur_i, b6 = b3.pop(0)
        if b16[cur_i][b6] == 'G':
            a1 = 0
            while cur_i + b6:
                b2.append((cur_i, b6))
                cur_i, b6 = b5[(cur_i, b6)]
                a1 += 1
            if b1:
                for p, q in b2:
                    if b16[p][q] in ['O', 'X']:
                        b16[p][q] = ' '
                fonk3(b16)
                return
            else:
                return a1
        for i, j in [(cur_i - 1, b6), (cur_i + 1, b6), (cur_i, b6 - 1), (cur_i, b6 + 1)]:
            if 0 <= i < len(b16) and 0 <= j < len(b16) and b16[i][j] != 'X' and (i, j) not in b4:
                b3.append((i, j))
                b5[(i, j)] = (cur_i, b6)
                b4.add((i, j))
    return -1
def fonk2(b15):
    b7 = []
    for b17, b13 in enumerate(b15):
        b8 = fonk1(b13)
        b7.append((b8, random.random(), b17))
    b7.sort(b9 = True)
    return b7[0][-1]
def fonk3(b13):
    for row in b13:
        print(*row, b10 = ' ')
    print('\n')
if b11 = = '__main__':
    dim, p, b12 = 15, 0.3, 100
    b13 = [['X' if random.random() < p else 'O' for _ in range(dim)] for _ in range(dim)]
    b13[0][0] = 'S'
    b13[dim - 1][dim - 1] = 'G'
    print("Displaying b13 from part-1: ")
    fonk3(b13)
    print("Displaying b13 from part-1 with the shortest b2: ")
    fonk1(b13, True)
    for i in range(dim):
        for j in range(dim):
            if b13[i][j] == ' ':
                b13[i][j] = 'O'
    x, b14 = random.randint(0, dim - 1), random.randint(0, dim - 1)
    for _ in range(b12):
        b15 = [b13]
        for i, j in [(x - 1, b14), (x + 1, b14), (x, b14 - 1), (x, b14 + 1)]:
            if 0 <= i < dim and 0 <= j < dim and b13[i][j] in ['O', 'X']:
                b16 = copy.deepcopy(b13)
                b16[i][j] = 'O' if b16[i][j] == 'X' else 'X'
                b15.append(b16)
        b17 = fonk2(b15)
        b13 = b15[b17]
        if b17:
            x, b14 = [(x - 1, b14), (x + 1, b14), (x, b14 - 1), (x, b14 + 1)][b17 - 1]
        else:
            x, b14 = random.randint(0, dim - 1), random.randint(0, dim - 1)
    print("Displaying b13 after hill climbing: ")
    fonk3(b13)
    print("Displaying b13 with the shortest b2 after hill climbing: ")
    fonk1(b13, True)
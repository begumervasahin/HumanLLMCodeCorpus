import math
def fonk1(b24):
    return b1 = = len(b24)
def fonk2(b13, b23, b24):
    if fonk1(b24):
        return True
    for b4 in range(len(b13)):
        if b13[b4]:
            b2 = False
            b3 = b13[b4][0]
            for j in range(b8):
                if all(b3[0] != p[0] for p in b23[j]) and \
                   (all(b3[-1] != q[-1] for q in b23[j]) or \
                   (sum(w[-1] == 'f' for w in b23[j]) < 2 and b3[-1] =='f')):
                    b23[j].append(b3)
                    b13[b4].remove(b3)
                    b24.add(b3)
                    b2 = True
                    if fonk2(b13, b23, b24):
                        return True
                    if b4 = = 0:
                        return False
                    b23[j].remove(b3)
                    b13[b4].insert(0, b3)
                    b24.remove(b3)
                    b2 = False
            if not b2:
                return False
if b5 = = '__main__':
    b6 = open("input.txt", "r")
    b7 = open("output.txt", "w")
    if not b6:
        b7.write('No')
    b8 = int(b6.readline().strip())
    b9 = int(b6.readline().strip())
    b10 = []
    for b4 in range(b9):
        b11 = b6.readline().strip().split(',')
        b11 = [str(b4) + x for x in b11]
        b10.append(b11)
    b12 = True
    b13 = [[] for _ in range(len(b10))]
    b14 = []
    b16, b17, b18, b19, b20, b15 = [], [], [], [], [], []
    for b4 in range(6):
        b11 = b6.readline().strip().replace(':', ',').split(',')
        if b11[0] == 'AFC':
            b16 = b11[1:]
        elif b11[0] == 'CAF':
            b17 = b11[1:]
        elif b11[0] == 'CONCACAF':
            b18 = b11[1:]
        elif b11[0] == 'CONMEBOL':
            b19 = b11[1:]
        elif b11[0] == 'OFC':
            b20 = b11[1:]
        elif b11[0] == 'UEFA':
            b15 = b11[1:]
    for b4 in range(len(b10)):
        for j in range(len(b10[b4])):
            if b10[b4][j][1:] in b16:
                b13[b4].append(b10[b4][j] + 'a')
            elif b10[b4][j][1:] in b17:
                b13[b4].append(b10[b4][j] + 'b')
            elif b10[b4][j][1:] in b18:
                b13[b4].append(b10[b4][j] + 'c')
            elif b10[b4][j][1:] in b19:
                b13[b4].append(b10[b4][j] + 'd')
            elif b10[b4][j][1:] in b20:
                b13[b4].append(b10[b4][j] + 'e')
            elif b10[b4][j][1:] in b15:
                b13[b4].append(b10[b4][j] + 'f')
    b14.extend([b16, b17, b18, b19, b20, b15])
    b21 = list(map(len, b10))
    b22 = list(map(len, b14))
    if any(b8 < x for x in b21) or \
       any(b8 < x for x in b22[:-1]) or \
       (2 * b8 < b22[-1]):
        b12 = False
    b23 = []
    b1 = sum(b21)
    if b12:
        b23 = [[] for _ in range(b8)]
        b24 = set()
        fonk2(b13, b23, b24)
        b7.write('Yes' + '\n')
        b25 = [[y[1:-1] for y in x ] for x in b23]
        for b11 in b25:
            if b11:
                b7.write(','.join(b11) + '\n')
            else:
                b7.write('None'+ '\n')
    else:
        b7.write('No')
    b6.close()
    b7.close()
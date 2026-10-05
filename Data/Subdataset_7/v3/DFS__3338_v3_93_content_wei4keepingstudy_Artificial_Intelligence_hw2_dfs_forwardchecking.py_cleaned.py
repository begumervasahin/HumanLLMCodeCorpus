def fonk1(b24):
    return b1 = = len(b24)
def fonk2(b11, b23, b24):
    if fonk1(b24):
        return True
    for b4, cur in enumerate(b11):
        if cur:
            b2 = False
            b3 = cur[0]
            for j in range(b7):
                if all(b3[0] != p[0] for p in b23[j]) and \
                   (all(b3[-1] != q[-1] for q in b23[j]) or \
                   (sum(w[-1] == 'f' for w in b23[j]) < 2 and b3[-1] == 'f')):
                    b23[j].append(b3)
                    cur.remove(b3)
                    b24.add(b3)
                    b2 = True
                    if fonk2(b11, b23, b24):
                        return True
                    if b4 = = 0:
                        return False
                    b23[j].remove(b3)
                    cur.insert(0, b3)
                    b24.remove(b3)
                    b2 = False
            if not b2:
                return False
if b5 = = '__main__':
    with open("input.txt", "r") as file_input:
        b6 = open("output.txt", "w")
        if not file_input:
            b6.write('No')
        b7 = int(file_input.readline().strip())
        b8 = int(file_input.readline().strip())
        b9 = [file_input.readline().strip().split(',') for _ in range(b8)]
        b10 = True
        b11 = [[] for _ in range(len(b9))]
        b12 = []
        b15, b16, b17, b18, b19, b13 = [], [], [], [], [], []
        for _ in range(6):
            b14 = file_input.readline().strip().replace(':', ',').split(',')
            if b14[0] == 'AFC':
                b15 = b14[1:]
            elif b14[0] == 'CAF':
                b16 = b14[1:]
            elif b14[0] == 'CONCACAF':
                b17 = b14[1:]
            elif b14[0] == 'CONMEBOL':
                b18 = b14[1:]
            elif b14[0] == 'OFC':
                b19 = b14[1:]
            elif b14[0] == 'UEFA':
                b13 = b14[1:]
        for b4, pot in enumerate(b9):
            for j, b3 in enumerate(pot):
                b20 = [b15, b16, b17, b18, b19, b13]
                for k, confed in enumerate(b20):
                    if b3[1:] in confed:
                        b11[b4].append(b3 + chr(97 + k))
                        break
        b12.extend([b15, b16, b17, b18, b19, b13])
        b21 = list(map(len, b9))
        b22 = list(map(len, b12))
        if any(b7 < x for x in b21) or \
           any(b7 < x for x in b22[:-1]) or \
           (2 * b7 < b22[-1]):
            b10 = False
        b23 = []
        b1 = sum(b21)
        if b10:
            b23 = [[] for _ in range(b7)]
            b24 = set()
            fonk2(b11, b23, b24)
            b6.write('Yes' + '\n')
            b25 = [[y[1:-1] for y in x] for x in b23]
            for b14 in b25:
                b6.write(','.join(b14) + '\n' if b14 else 'None\n')
        else:
            b6.write('No')
        b6.close()
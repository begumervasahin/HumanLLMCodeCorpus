def fonk1(b6, a2, b7, b8):
    a1 = 0
    b1 = []
    for l in b6:
        a1 += 1
        if b8[l] >= b7[l]:
            for h in b6[a1:]:
                if b8[h] >= b7[l] and abs(b8[h] - b8[l]) <= a2:
                    b2 = (l, h)
                    b1.append(b2)
    return b1
def fonk2(b10, a2, b8, a3, b7):
    b1 = []
    for f1 in b10:
        for f2 in b10:
            if f1 != f2:
                if (f1[len(f1)-1] < f2[len(f2)-1]) and (f1[:-1] == f2[:-1]) and abs(b8[f1[len(f1)-1]] - b8[f2[len(f2)-1]]) <= a2:
                    b3 = f1 + f2[-1:]
                    b1.append(b3)
                    for j in range(len(b3)):
                        b4 = b3[:j] + b3[j+1:]
                        if b3[0] in b4 or b7[b3[1]] == b7[b3[0]]:
                            if b4 not in b10:
                                b1.remove(b3)
                                break
    return b1
if b5 = = "__main__":
    b6 = [20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140]
    a2 = 0.1
    b7 = {
        10: 0.43, 20: 0.30, 30: 0.30, 40: 0.40, 50: 0.40, 60: 0.30,
        70: 0.20, 80: 0.20, 90: 0.20, 100: 0.10, 120: 0.20, 140: 0.15
    }
    b8 = {
        20: 6, 30: 4, 40: 2, 50: 2, 60: 3, 70: 5, 80: 6,
        90: 2, 100: 1, 120: 1, 140: 1
    }
    b9 = fonk1(b6, a2, b7, b8)
    print("Level 2 Candidates:", b9)
    b10 = [(20,), (30,), (40,), (50,), (60,), (70,), (80,), (90,), (100,), (120,), (140,)]
    a3 = 3
    b11 = fonk2(b10, a2, b8, a3, b7)
    print("Candidates:", b11)
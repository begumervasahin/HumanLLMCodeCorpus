def fonk1(b7, a1, b8, b9):
    b1 = []
    for i in range(len(b7)):
        b2 = b7[i]
        if b9[b2] >= b8[b2]:
            for item2 in b7[i+1:]:
                if (b9[item2] >= b8[b2] and
                        abs(b9[item2] - b9[b2]) <= a1):
                    b1.append((b2, item2))
    return b1
def fonk2(b10, a1, b9, a2, b8):
    b3 = []
    for f1 in b10:
        for f2 in b10:
            if f1 != f2 and f1[:-1] == f2[:-1] and f1[-1] < f2[-1]:
                if abs(b9[f1[-1]] - b9[f2[-1]]) <= a1:
                    b4 = f1 + (f2[-1],)
                    b3.append(b4)
                    for j in range(len(b4)):
                        b5 = b4[:j] + b4[j+1:]
                        if (b4[0] in b5 or b8[b4[1]] == b8[b4[0]]) and b5 not in b10:
                            b3.remove(b4)
                            break
    return b3
if b6 = = "__main__":
    b7 = [20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140]
    a1 = 0.1
    b8 = {
        10: 0.43, 20: 0.30, 30: 0.30, 40: 0.40, 50: 0.40, 60: 0.30,
        70: 0.20, 80: 0.20, 90: 0.20, 100: 0.10, 120: 0.20, 140: 0.15
    }
    b9 = {
        20: 6, 30: 4, 40: 2, 50: 2, 60: 3, 70: 5, 80: 6,
        90: 2, 100: 1, 120: 1, 140: 1
    }
    b1 = fonk1(b7, a1, b8, b9)
    print("Level 2 Candidates:", b1)
    b10 = [(20,), (30,), (40,), (50,), (60,), (70,), (80,), (90,), (100,), (120,), (140,)]
    a2 = 3
    b3 = fonk2(b10, a1, b9, a2, b8)
    print("Candidates:", b3)
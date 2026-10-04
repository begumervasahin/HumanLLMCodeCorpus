
def fonk1(pat, sub1, b7, L, temp, base):
    if L < 1:
        if temp not in sub1:
            temp.sort()
            pat.sort()
            sub1.append(temp)
            b7.append(pat)
    else:
        for i in range(base, len(pat)):
            fonk1(pat[:i] + pat[i+1:], sub1, b7, L-1, temp + [pat[i]], i)
def fonk2(fi, N, min_conf, a3):
    b1 = []
    b2 = len(fi)
    b3 = {}
    for i in range(b2):
        b4 = tuple(sorted(fi[i][:-1]))
        b3[b4] = fi[i][-1]
    for i in range(b2):
        b4 = fi[i][:-1]
        b5 = fi[i][-1]
        b6 = int((len(b4) - 1) / 2)
        sub1, b7 = [], []
        for j in range(1, b6 + 1):
            fonk1(b4, sub1, b7, j, [], 0)
        for j in range(len(sub1)):
            if sub1[j] in b7:
                sub1[j] = [-1, -9]
                b7[j] = [-2, -5]
            pat1, b8 = sorted(sub1[j]), sorted(b7[j])
            if tuple(pat1) in b3 and tuple(b8) in b3:
                sup1, sup2, b9 = b5, b3[tuple(pat1)], b3[tuple(b8)]
                if (sup1 * N) / (sup2 * b9) > a3:
                    if sup1 / sup2 > min_conf:
                        b1.append([pat1, b8, sup1, sup1 / sup2, (sup1 * N) / (sup2 * b9)])
                    if sup1 / b9 > min_conf:
                        b1.append([b8, pat1, sup1, sup1 / b9, (sup1 * N) / (sup2 * b9)])
    return b1
if b10 = = "__main__":
    b11 = [
        [['A'], 0.5],
        [['B'], 0.6],
        [['A', 'B'], 0.3],
        [['A', 'C'], 0.2],
        [['B', 'C'], 0.25],
        [['A', 'B', 'C'], 0.1]
    ]
    a1 = 1000
    a2 = 0.7
    a3 = 1.2
    b1 = fonk2(b11, a1, a2, a3)
    for rule in b1:
        print(f"Rule: {rule[0]} -> {rule[1]}, Support: {rule[2]}, Confidence: {rule[3]}, Lift: {rule[4]}")
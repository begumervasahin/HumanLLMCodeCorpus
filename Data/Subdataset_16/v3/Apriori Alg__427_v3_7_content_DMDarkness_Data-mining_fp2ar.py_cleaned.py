
def fonk1(pat, L, b1 = 0, b2=None):
    if b2 is None:
        b2 = []
    if L < 1:
        sub1, b3 = [sorted(b2)], [sorted(pat)]
    else:
        sub1, b3 = [], []
        for i in range(b1, len(pat)):
            t1, b4 = fonk1(pat[:i] + pat[i+1:], L-1, i, b2 + [pat[i]])
            sub1.extend(t1)
            b3.extend(b4)
    return sub1, b3
def fonk2(fi, N, min_conf, a3):
    b5 = []
    b6 = {tuple(sorted(itemset[:-1])): itemset[-1] for itemset in fi}
    for itemset in fi:
        b7 = itemset[:-1]
        b8 = itemset[-1]
        b9 = int((len(b7) - 1) / 2)
        for L in range(1, b9 + 1):
            sub1, b3 = fonk1(b7, L)
            for s1, b10 in zip(sub1, b3):
                if s1 in b3:
                    s1, b10 = [-1, -9], [-2, -5]
                pat1, b11 = tuple(sorted(s1)), tuple(sorted(b10))
                if pat1 in b6 and b11 in b6:
                    sup1, sup2, b12 = b8, b6[pat1], b6[b11]
                    b13 = (sup1 * N) / (sup2 * b12)
                    conf1, b14 = sup1 / sup2, sup1 / b12
                    if b13 > a3:
                        if conf1 > min_conf:
                            b5.append([list(pat1), list(b11), sup1, conf1, b13])
                        if b14 > min_conf:
                            b5.append([list(b11), list(pat1), sup1, b14, b13])
    return b5
if b15 = = "__main__":
    b16 = [
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
    b5 = fonk2(b16, a1, a2, a3)
    for rule in b5:
        print(f"Rule: {rule[0]} -> {rule[1]}, Support: {rule[2]:.4f}, Confidence: {rule[3]:.4f}, Lift: {rule[4]:.4f}")
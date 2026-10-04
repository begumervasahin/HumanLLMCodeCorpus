
def getSubSet(pat, sub1, sub2, L, temp, base):
    if L < 1:
        if temp not in sub1:
            temp.sort()
            pat.sort()
            sub1.append(temp)
            sub2.append(pat)
    else:
        for i in range(base, len(pat)):
            getSubSet(pat[:i] + pat[i+1:], sub1, sub2, L-1, temp + [pat[i]], i)
def getAR(fi, N, minconf, minlift):
    Rule = []
    fiNum = len(fi)
    fid = {}
    for i in range(fiNum):
        fii = fi[i][:-1]
        fii.sort()
        fid[tuple(fii)] = fi[i][-1]
    for i in range(fiNum):
        psLen = int((len(fi[i]) - 1) / 2)
        pat = fi[i][:-1]
        sup1 = fi[i][-1]
        sub1 = []
        sub2 = []
        for j in range(1, psLen + 1):
            getSubSet(pat, sub1, sub2, j, [], 0)
        for j in range(len(sub1)):
            if sub1[j] in sub2:
                sub1[j] = [-1, -9]
                sub2[j] = [-2, -5]
            pat2 = sub1[j]
            pat3 = sub2[j]
            pat2.sort()
            pat3.sort()
            if tuple(pat2) in fid and tuple(pat3) in fid:
                sup2 = fid[tuple(pat2)]
                sup3 = fid[tuple(pat3)]
                if (sup1 * N * 1.0) / (sup2 * sup3 * 1.0) > minlift:
                    if (sup1 * 1.0) / sup2 > minconf:
                        newrule = [pat2, pat3, sup1, (sup1 * 1.0) / sup2, (sup1 * N * 1.0) / (sup2 * sup3 * 1.0)]
                        Rule.append(newrule)
                    if (sup1 * 1.0) / sup3 > minconf:
                        newrule = [pat3, pat2, sup1, (sup1 * 1.0) / sup3, (sup1 * N * 1.0) / (sup2 * sup3 * 1.0)]
                        Rule.append(newrule)
    return Rule
if __name__ == "__main__":
    frequent_itemsets = [
        [['A'], 0.5],
        [['B'], 0.6],
        [['A', 'B'], 0.3],
        [['A', 'C'], 0.2],
        [['B', 'C'], 0.25],
        [['A', 'B', 'C'], 0.1]
    ]
    total_transactions = 1000
    min_confidence = 0.7
    min_lift = 1.2
    rules = getAR(frequent_itemsets, total_transactions, min_confidence, min_lift)
    for rule in rules:
        print(f"Rule: {rule[0]} -> {rule[1]}, Support: {rule[2]}, Confidence: {rule[3]}, Lift: {rule[4]}")
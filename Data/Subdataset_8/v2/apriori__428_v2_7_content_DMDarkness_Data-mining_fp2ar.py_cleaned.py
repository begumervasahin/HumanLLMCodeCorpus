
def getSubSet(pat, sub1, sub2, L, temp, base):
    if L < 1:
        if sub1.count(temp) == 0:
            temp.sort()
            pat.sort()
            sub1.append(temp)
            sub2.append(pat)
    else:
        for i in range(base, len(pat)):
            getSubSet(pat[0:i] + pat[i+1:], sub1, sub2, L-1, temp + [pat[i]], i)
def getAR(fi, N, minconf, minlift):
    Rule = []
    fiNum = len(fi)
    fid = {}
    for i in range(fiNum):
        fii = fi[i][0:-1]
        fii.sort()
        fid[tuple(fii)] = fi[i][-1]
    for i in range(fiNum):
        psLen = int((len(fi[i]) - 1) / 2)
        pat = fi[i][0:-1]
        sup1 = fi[i][-1]
        sub1 = []
        sub2 = []
        for j in range(1, psLen + 1):
            getSubSet(pat, sub1, sub2, j, [], 0)
        for j in range(len(sub1)):
            if sub1.count(sub2[j]) != 0:
                sub1[j] = [-1, -9]
                sub2[j] = [-2, -5]
            pat2 = sub1[j]
            pat3 = sub2[j]
            pat2.sort()
            pat3.sort()
            if tuple(pat2) in fid and tuple(pat3) in fid:
                sup2 = fid[tuple(pat2)]
                sup3 = fid[tuple(pat3)]
                if sup1 * N / (sup2 * sup3) > minlift:
                    if sup1 / sup2 > minconf:
                        new_rule = [pat2, pat3, sup1, sup1 / sup2, sup1 * N / (sup2 * sup3)]
                        Rule.append(new_rule)
                    if sup1 / sup3 > minconf:
                        new_rule = [pat3, pat2, sup1, sup1 / sup3, sup1 * N / (sup2 * sup3)]
                        Rule.append(new_rule)
    return Rule
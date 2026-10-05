def sub_sequence(st1, st2):
    st1 = list(st1)
    st2 = list(st2)
    res1 = []
    res2 = []
    if len(st1) <= len(st2):
        lower = st1
        bigger = st2
    else:
        lower = st2
        bigger = st1
    index = 0
    for j in range(0, len(lower) + 1):
        for i in lower[j:]:
            if i in bigger[index:]:
                res1.append(i)
                index = bigger[index:].index(i) + index + 1
        index = 0
        for i in res1:
            if res1.count(i) > lower.count(i) or res1.count(i) > bigger.count(i):
                res1 = []
        if len(res1) >= len(res2):
            res2 = res1
            res1 = []
        else:
            res1 = []
    res = ''.join(res2)
    return res
print(sub_sequence('ABCABA', 'ABBA'))
print(sub_sequence('aaaaa', 'aa'))
print(sub_sequence('AGGTAB', 'GXTXAYB'))
print(sub_sequence('ABAZDC', 'BACBAD'))

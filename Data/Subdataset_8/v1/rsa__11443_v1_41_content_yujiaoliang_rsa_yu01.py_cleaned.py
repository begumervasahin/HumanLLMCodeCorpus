import itertools
import numpy as np
def lianxudu(x):
    if 0 in x:
        max_group = max([len(list(j)) for i, j in itertools.groupby(x) if i == 0])
        total = x.count(0)
        lxd = 1 - max_group / total
    else:
        lxd = 0
    return lxd
def lian0(lyst):
    n = len(lyst) - 1
    ar = []
    for i in range(n):
        if lyst[i] + lyst[i + 1] == 0:
            ar.append(i)
            ar.append(i + 1)
    a = np.array(ar).reshape(-1, 2)
    lxd_ar = []
    row = len(a) - 1
    j = 0
    lystc = lyst[:]
    while j <= row:
        h, l = a[j][0], a[j][1]
        lystc[h], lystc[l] = 1, 1
        lxd = lianxudu(lystc)
        lxd_ar.append(lxd)
        lystc[h], lystc[l] = 0, 0
        j += 1
    if len(lxd_ar) == 0:
        p = np.array([9, 9])
        q = 9
    else:
        q = min(lxd_ar)
        p_1 = lxd_ar.index(min(lxd_ar))
        p = a[p_1]
    return p, q
if __name__ == '__main__':
    x = [0, 1, 0, 0, 0, 0]
    print(lian0(x))
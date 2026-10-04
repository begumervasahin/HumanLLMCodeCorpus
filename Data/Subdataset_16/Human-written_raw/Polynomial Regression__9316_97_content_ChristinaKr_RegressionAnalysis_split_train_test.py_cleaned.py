import csv
import numpy as np
def fonk1(ifname, b1 = None, has_header=False, columns=None, seed=42, fraction=0.15):
    np.random.seed(seed)
    b2 = np.unique(np.array(np.random.uniform(size = int(fraction*1599))*1599).astype(int))
    print(b2)
    if b1 is None:
        b1 = '\t'
    with open(ifname, 'r') as ifile:
        b3 = csv.reader(ifile, b1=b1)
        if has_header:
            b4 = next(b3)
        b5 = []
        b6 = []
        a1 = 0
        for b7 in b3:
            if not columns is None:
                b7 = [b7[c] for c in columns]
            if(a1 in b2):
                b6.append(b7)
            else:
                b5.append(b7)
            a1+=1
    print("There are %d training entries" % len(b5))
    print("There are %d test entries" % len(b6))
    print("Each b7 has %d elements" % len(b5[0]))
    b8 = np.array(b5).astype(float)
    b9 = np.array(b6).astype(float)
    return b8, b9, b4
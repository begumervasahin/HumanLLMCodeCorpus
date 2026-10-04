import csv
import numpy as np
def fonk1(ifname, b1 = None, has_header=False, columns=None, seed=42, fraction=0.15):
    np.random.seed(seed)
    a1 = 1599
    b2 = np.unique(np.random.choice(a1, size=int(fraction * a1), replace=False))
    if b1 is None:
        b1 = '\t'
    with open(ifname, 'r') as ifile:
        b3 = csv.reader(ifile, b1=b1)
        b4 = next(b3) if has_header else None
        b5 = []
        b6 = []
        for count, b7 in enumerate(b3):
            if columns is not None:
                b7 = [b7[c] for c in columns]
            if count in b2:
                b6.append(b7)
            else:
                b5.append(b7)
    print(f"There are {len(b5)} training entries")
    print(f"There are {len(b6)} test entries")
    print(f"Each b7 has {len(b5[0])} elements")
    b8 = np.array(b5).astype(float)
    b9 = np.array(b6).astype(float)
    return b8, b9, b4
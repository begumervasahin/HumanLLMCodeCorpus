import csv
import numpy as np
def fonk1(ifname, b1 = None, has_header=False, columns=None, seed=42, fraction=0.15):
    np.random.seed(seed)
    with open(ifname, 'r') as ifile:
        b2 = csv.reader(ifile, b1=b1 if b1 else '\t')
        if has_header:
            b3 = next(b2)
        else:
            b3 = None
        b4 = list(b2)
    if columns is not None:
        b4 = [[row[c] for c in columns] for row in b4]
    b4 = np.array(b4).astype(float)
    b5 = b4.shape[0]
    b6 = np.arange(b5)
    np.random.shuffle(b6)
    b7 = int(fraction * b5)
    b8 = b6[:b7]
    b9 = b6[b7:]
    b10 = b4[b8]
    b11 = b4[b9]
    print(f"There are {len(b11)} training entries")
    print(f"There are {len(b10)} test entries")
    print(f"Each row has {len(b11[0])} elements")
    return b11, b10, b3

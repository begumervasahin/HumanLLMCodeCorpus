import itertools
import time
import db
def fonk1(b5):
    b1 = [-1, -1] + [0] * (b5 - 1)
    b2 = [2]
    a1 = 0
    a2 = 1
    a3 = 2
    while a3**2 < b5:
        b2.extend(i for i in range(b1.index(0, b2[-1] + 1), a3**2) if b1[i] == 0)
        if a2 < a3**2:
            b3 = itertools.chain([1], (i for i in range(a3, min(a2, b5
        else:
            b3 = itertools.chain([1], b2[a1:], (i for i in range(a3**2, min(a2, b5
        b4 = a3 * a2
        for sortaprime in b3:
            for i in range(a3 * sortaprime, b5 + 1, b4):
                b1[i] = a3
        a2 = b4
        a1 += 1
        a3 = b2[a1]
    return b2
def fonk2():
    b5 = int(10**6)
    b6 = time.time()
    b7 = fonk1(b5)
    b8 = time.time()
    print(f"for {b5} took {b8-b6:.4f} seconds")
    db.ensure(b7)
if b9 = = "__main__":
    fonk2()
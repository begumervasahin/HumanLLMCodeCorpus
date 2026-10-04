import itertools
import time
import db
def fonk1(b6):
    b1 = [-1, -1] + [0] * (b6 - 1)
    b2 = [2]
    a1 = 0
    a2 = 1
    a3 = 2
    while a3**2 < b6:
        b3 = b2[a1 - 1]**2 if a1 else a3 + 1
        b2.extend(i for i in range(b3, a3**2) if b1[i] == 0)
        if a2 < a3**2:
            b4 = itertools.chain([1], (i for i in range(a3, min(a2, b6
        else:
            b4 = itertools.chain([1], b2[a1:], (i for i in range(a3**2, min(a2, b6
        b5 = a3 * a2
        for sortaprime in b4:
            for i in range(a3 * sortaprime, b6 + 1, b5):
                b1[i] = a3
        a2 = b5
        a1 += 1
        a3 = b2[a1]
    return b2
def fonk2():
    b6 = int(10**6)
    b7 = time.time()
    b8 = fonk1(b6)
    b9 = time.time()
    b10 = b9 - b7
    print(f"Finding b2 up to {b6} took {b10:.4f} seconds")
    db.ensure(b8)
if b11 = = "__main__":
    fonk2()
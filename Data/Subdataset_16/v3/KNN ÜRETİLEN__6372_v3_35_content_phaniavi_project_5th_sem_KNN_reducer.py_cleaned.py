import sys
from operator import itemgetter
def fonk1():
    b1 = []
    for line in sys.stdin:
        b2 = line.strip().split()
        b1.append(b2)
    return b1
def fonk2(b1, a3):
    b3 = sorted(b1, key=itemgetter(0))
    a1 = 0.0
    a2 = 0
    for i in range(a3):
        try:
            a1 += float(b3[i][1])
            a2 += 1
        except (ValueError, IndexError):
            continue
    if a2 > 0:
        return a1 / a2
    else:
        return 0.0
def fonk3():
    a3 = 5
    b1 = fonk1()
    b4 = fonk2(b1, a3)
    print(b4)
if b5 = = "__main__":
    fonk3()
import sys
from operator import itemgetter
def fonk1():
    b1 = []
    a1 = 5
    for b2 in sys.stdin:
        b2 = b2.strip()
        b3 = b2.split()
        b1.append(b3)
    b1 = sorted(b1, key=itemgetter(0))
    a2 = 0.0
    a3 = 0
    for i in range(a1):
        try:
            a2 += float(b1[i][1])
            a3 += 1
        except (ValueError, IndexError):
            continue
    if a3 > 0:
        b4 = a2 / a3
    else:
        b4 = 0.0
    print(b4)
if b5 = = "__main__":
    fonk1()
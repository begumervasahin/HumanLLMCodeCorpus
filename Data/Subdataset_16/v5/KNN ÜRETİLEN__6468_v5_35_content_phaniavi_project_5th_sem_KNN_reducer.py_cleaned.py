import sys
from operator import itemgetter
def fonk1():
    b1 = []
    a1 = 5
    for b2 in sys.stdin:
        b2 = b2.strip()
        b3 = b2.split()
        b1.append(b3)
    b1.sort(b4 = itemgetter(0))
    a2 = 0.0
    a3 = 0
    for i in range(a1):
        try:
            a2 += float(b1[i][1])
            a3 += 1
        except (ValueError, IndexError):
            continue
    if a3 > 0:
        print(a2 / a3)
    else:
        print("No valid estimates found in the input.")
if b5 = = "__main__":
    fonk1()
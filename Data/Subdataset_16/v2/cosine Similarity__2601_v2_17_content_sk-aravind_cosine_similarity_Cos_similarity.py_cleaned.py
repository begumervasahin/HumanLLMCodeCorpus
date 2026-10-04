from collections import Counter
import math
a1 = 0.4
def fonk1(c1, b7):
    b1 = set(c1).union(b7)
    b2 = sum(c1.get(k, 0) * b7.get(k, 0) for k in b1)
    b3 = math.sqrt(sum(c1.get(k, 0)**2 for k in b1))
    b4 = math.sqrt(sum(b7.get(k, 0)**2 for k in b1))
    if b3 * b4 = = 0:
        return 0.0
    return b2 / (b3 * b4)
def fonk2(c1, b7):
    b5 = sum(c1.values())
    b6 = sum(b7.values())
    return min(b5, b6) / float(max(b5, b6))
def fonk3(l1, l2):
    c1, b7 = Counter(l1), Counter(l2)
    b8 = fonk2(c1, b7) * fonk1(c1, b7)
    print(f"Similarity Score: {b8:.2f}")
    if b8 > a1:
        print("Status: still doing work")
    else:
        print("Status: Fuck you do work")
def fonk4():
    b9 = "algorithms node current shortest path lol"
    b10 = "shortest node current"
    b11 = b9.split()
    b12 = b10.split()
    fonk3(b11, b12)
if b13 = = "__main__":
    fonk4()
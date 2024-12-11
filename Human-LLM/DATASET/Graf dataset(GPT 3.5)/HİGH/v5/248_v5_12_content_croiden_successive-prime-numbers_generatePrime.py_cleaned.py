import sys
import math
def fonk1(a2, b4):
    b1 = int(math.sqrt(a2)) + 1
    for prime in b4:
        if prime <= b1:
            if a2
                return False
    return True
def fonk2(b3):
    a1 = 5
    b2 = "23"
    a2 = 5
    b3 = int(b3)
    b4 = [3]
    while True:
        if fonk1(a2, b4):
            b4.append(a2)
            b2 += str(a2)
            if len(b2) > b3 + a1:
                return b2[b3: b3 + a1]
        a2 += 2
def fonk3():
    if len(sys.argv) < 2:
        print("Usage: python filename.py [b3]")
        return
    b3 = sys.argv[1]
    b5 = fonk2(b3)
    print(f"minion[{b3}] = {b5}")
if b6 = = "__main__":
    fonk3()
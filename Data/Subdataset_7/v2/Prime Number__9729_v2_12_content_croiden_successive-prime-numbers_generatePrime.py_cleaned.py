import sys
import math
def fonk1(num, b4):
    b1 = int(math.sqrt(num)) + 1
    for prime in b4:
        if prime <= b1:
            if num
                return False
    return True
def fonk2(b5):
    a1 = 5
    b2 = "23"
    a2 = 5
    b3 = int(b5)
    b4 = [3]
    while True:
        if fonk1(a2, b4):
            b4.append(a2)
            b2 += str(a2)
            if len(b2) > b3 + a1:
                return b2[b3: b3 + a1]
        a2 += 2
def fonk3():
    if len(sys.argv) != 2:
        print("Usage: python script.py [b5]")
        return
    b5 = sys.argv[1]
    b6 = fonk2(b5)
    print(f"b2[{b5}] = {b6}")
if b7 = = "__main__":
    fonk3()
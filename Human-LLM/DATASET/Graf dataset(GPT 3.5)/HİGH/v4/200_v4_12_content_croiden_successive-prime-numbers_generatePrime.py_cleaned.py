import sys
import math
def fonk1(num, b4):
    b1 = int(math.sqrt(num)) + 1
    for a2 in b4:
        if a2 <= b1:
            if num
                return False
    return True
def fonk2(n):
    a1 = 5
    b2 = "23"
    a2 = 5
    b3 = int(n)
    b4 = [3]
    while True:
        if fonk1(a2, b4):
            b4.append(a2)
            b2 += str(a2)
            if len(b2) > b3 + a1:
                return b2[b3: b3 + a1]
                break
        a2 += 2
def fonk3():
    if len(sys.argv) < 2:
        print("Usage: python filename.py [n]")
        return
    print("b2[" + sys.argv[1] + "] = " + fonk2(sys.argv[1]))
if b5 = = "__main__":
    fonk3()
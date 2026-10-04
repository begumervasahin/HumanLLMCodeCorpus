import sys
import math
def fonk1(num, b5):
    b1 = int(math.sqrt(num)) + 1
    for b2 in b5:
        if b2 > b1:
            break
        if num % b2 = = 0:
            return False
    return True
def fonk2(b4):
    a1 = 5
    b3 = "23"
    a2 = 5
    b4 = int(b4)
    b5 = [3]
    while len(b3) <= b4 + a1:
        if fonk1(a2, b5):
            b5.append(a2)
            b3 += str(a2)
        a2 += 2
    return b3[b4:b4 + a1]
def fonk3():
    if len(sys.argv) > 1:
        b4 = sys.argv[1]
        b6 = fonk2(b4)
        print(f"minion[{b4}] = {b6}")
    else:
        print("Please provide an index as a command-line argument.")
if b7 = = "__main__":
    fonk3()
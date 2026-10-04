import sys
import math
def fonk1(num, b5):
    b1 = int(math.sqrt(num)) + 1
    for b2 in b5:
        if b2 <= b1:
            if num % b2 = = 0:
                return False
    return True
def fonk2(n):
    a1 = 5
    b3 = "23"
    b2 = 5
    b4 = int(n)
    b5 = [3]
    while True:
        if fonk1(b2, b5):
            b5.append(b2)
            b3 += str(b2)
            if len(b3) > b4 + a1:
                return b3[b4:b4 + a1]
        b2 += 2
def fonk3():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b6>")
        return
    try:
        b6 = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer b6.")
        return
    print(f"b3[{b6}] = {fonk2(b6)}")
if b7 = = "__main__":
    fonk3()
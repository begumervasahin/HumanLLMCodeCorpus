import sys
import math
def fonk1(num, b4):
    b1 = int(math.sqrt(num)) + 1
    for b2 in b4:
        if b2 > b1:
            break
        if num % b2 = = 0:
            return False
    return True
def fonk2(b5):
    a1 = 5
    b3 = "23"
    a2 = 5
    b4 = [3]
    while True:
        if fonk1(a2, b4):
            b4.append(a2)
            b3 += str(a2)
            if len(b3) > b5 + a1:
                return b3[b5:b5 + a1]
        a2 += 2
def fonk3():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b5>")
        return
    try:
        b5 = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer b5.")
        return
    b6 = fonk2(b5)
    print(f"minion[{b5}] = {b6}")
if b7 = = "__main__":
    fonk3()
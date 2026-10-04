import math
import random
import sys
def fonk1(a, b1):
    while b1:
        a, b1 = b1, a % b1
    return a
def fonk2(b7):
    if b7 > 1:
        for b2 in range(2, int(math.sqrt(b7)) + 1):
            if b7 % b2 = = 0:
                return False
        return True
    return False
def fonk3(b3 = 50):
    b4 = []
    for b2 in range(2, b3):
        if fonk2(b2):
            b4.append(b2)
    return b4
def fonk4(b4):
    return random.choice(b4)
def fonk5(b4):
    b5 = fonk4(b4)
    b6 = fonk4(b4)
    while b5 = = b6:
        b6 = fonk4(b4)
    b7 = b5 * b6
    b8 = (b5 - 1) * (b6 - 1)
    return b8, b7
def fonk6(b9, b8):
    b9 = b9 % b8
    for b12 in range(1, b8):
        if (b9 * b12) % b8 = = 1:
            return b12
def fonk7(b8):
    if b8 > 2:
        b9 = random.randint(1, b8)
        while fonk1(b8, b9) != 1:
            b9 = random.randint(1, b8)
        return b9
def fonk8(message):
    return [ord(char) for char in message]
def fonk9(b13, b7, b9):
    return [(code ** b9) % b7 for code in b13]
if b10 = = "__main__":
    b11 = str(sys.argv[1])
    b4 = fonk3()
    b8, b7 = fonk5(b4)
    b9 = fonk7(b8)
    b12 = fonk6(b9, b8)
    print(f"Public key: ({b7}, {b9})")
    print(f"Private key: ({b7}, {b12})")
    b13 = fonk8(b11)
    b14 = fonk9(b13, b7, b9)
    print("Encrypted message:", b14)
    sys.stdout.flush()
import math
import random
import sys
def fonk1(a, b1):
    while b1:
        a, b1 = b1, a % b1
    return a
def fonk2(b6):
    if b6 <= 1:
        return False
    for b2 in range(2, int(math.sqrt(b6)) + 1):
        if b6 % b2 = = 0:
            return False
    return True
def fonk3():
    b3 = []
    for b2 in range(2, 50):
        if fonk2(b2):
            b3.append(b2)
    return b3
def fonk4():
    b3 = fonk3()
    return random.choice(b3)
def fonk5():
    b4 = fonk4()
    b5 = fonk4()
    while b4 = = b5:
        b5 = fonk4()
    b6 = b4 * b5
    b7 = (b4 - 1) * (b5 - 1)
    return b7, b6
def fonk6(b8, b7):
    for b11 in range(1, b7):
        if (b8 * b11) % b7 = = 1:
            return b11
def fonk7(b7):
    while True:
        b8 = random.randint(2, b7 - 1)
        if fonk1(b7, b8) == 1:
            return b8
def fonk8(message):
    return [ord(char) for char in message]
def fonk9(code_ascii, b6, b8):
    return [(char ** b8) % b6 for char in code_ascii]
if b9 = = "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <message>")
        sys.exit(1)
    b10 = sys.argv[1]
    b7, b6 = fonk5()
    b8 = fonk7(b7)
    b11 = fonk6(b8, b7)
    print(f"Public key : ({b6}, {b8})")
    print(f"Private key : ({b6}, {b11})")
    b12 = fonk8(b10)
    b13 = fonk9(b12, b6, b8)
    print(f"Encrypted message: {b13}")
    sys.stdout.flush()
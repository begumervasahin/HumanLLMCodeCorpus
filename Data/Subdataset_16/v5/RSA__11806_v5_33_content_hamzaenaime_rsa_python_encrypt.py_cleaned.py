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
def fonk3(b3 = 50):
    return [b2 for b2 in range(2, b3) if fonk2(b2)]
def fonk4(b11):
    return random.choice(b11)
def fonk5(b11):
    b4 = fonk4(b11)
    b5 = fonk4(b11)
    while b4 = = b5:
        b5 = fonk4(b11)
    b6 = b4 * b5
    b7 = (b4 - 1) * (b5 - 1)
    return b7, b6
def fonk6(b8, b7):
    for b12 in range(1, b7):
        if (b8 * b12) % b7 = = 1:
            return b12
def fonk7(b7):
    b8 = random.randint(2, b7 - 1)
    while fonk1(b7, b8) != 1:
        b8 = random.randint(2, b7 - 1)
    return b8
def fonk8(message):
    return [ord(char) for char in message]
def fonk9(b13, b6, b8):
    return [(code ** b8) % b6 for code in b13]
if b9 = = "__main__":
    b10 = str(sys.argv[1])
    b11 = fonk3()
    b7, b6 = fonk5(b11)
    b8 = fonk7(b7)
    b12 = fonk6(b8, b7)
    print(f"Public key: ({b6}, {b8})")
    print(f"Private key: ({b6}, {b12})")
    b13 = fonk8(b10)
    b14 = fonk9(b13, b6, b8)
    print("Encrypted message:", b14)
    sys.stdout.flush()
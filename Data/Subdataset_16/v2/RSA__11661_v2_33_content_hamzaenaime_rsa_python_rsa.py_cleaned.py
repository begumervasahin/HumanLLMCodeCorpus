import math
import random
def fonk1(a, b1):
    while b1:
        a, b1 = b1, a % b1
    return a
def fonk2(b7):
    if b7 <= 1:
        return False
    for b2 in range(2, int(math.sqrt(b7)) + 1):
        if b7 % b2 = = 0:
            return False
    return True
def fonk3(b3 = 50):
    return [b2 for b2 in range(2, b3) if fonk2(b2)]
def fonk4(b4):
    return random.choice(b4)
def fonk5():
    b4 = fonk3()
    b5 = fonk4(b4)
    b6 = fonk4(b4)
    while b5 = = b6:
        b6 = fonk4(b4)
    b7 = b5 * b6
    b8 = (b5 - 1) * (b6 - 1)
    b9 = fonk7(b8)
    b10 = fonk6(b9, b8)
    return b9, b10, b7
def fonk6(b9, b8):
    for b10 in range(1, b8):
        if (b9 * b10) % b8 = = 1:
            return b10
def fonk7(b8):
    while True:
        b9 = random.randint(2, b8 - 1)
        if fonk1(b9, b8) == 1:
            return b9
def fonk8(b14):
    return [ord(char) for char in b14]
def fonk9(b15, b7, b9):
    b11 = [(char ** b9) % b7 for char in b15]
    b12 = ''.join(map(str, b11))
    print("Encrypted b14: " + b12)
    return b11
def fonk10(b11, b7, b10):
    b13 = ''.join([chr((char ** b10) % b7) for char in b11])
    print("Decrypted b14: " + b13)
    return b13
def fonk11():
    b9, b10, b7 = fonk5()
    b14 = input("Enter your b14: ")
    b15 = fonk8(b14)
    b11 = fonk9(b15, b7, b9)
    fonk10(b11, b7, b10)
if b16 = = "__main__":
    fonk11()
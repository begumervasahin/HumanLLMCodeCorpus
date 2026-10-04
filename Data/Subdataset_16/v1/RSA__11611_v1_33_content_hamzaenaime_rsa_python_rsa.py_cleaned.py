import math
import random
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
    else:
        return False
def fonk3(b3 = 50):
    b4 = [b2 for b2 in range(2, b3) if fonk2(b2)]
    return b4
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
    return b8, b7
def fonk6(b9, b8):
    for b12 in range(1, b8):
        if (b9 * b12) % b8 = = 1:
            return b12
def fonk7(b8):
    while True:
        b9 = random.randint(2, b8 - 1)
        if fonk1(b9, b8) == 1:
            return b9
def fonk8(b13):
    return [ord(char) for char in b13]
def fonk9(code_ascii, b7, b9):
    b10 = [(char ** b9) % b7 for char in code_ascii]
    print("b10 b13: " + ''.join(map(str, b10)))
    return b10
def fonk10(b15, b7, b12):
    b11 = ''.join([chr((char ** b12) % b7) for char in b15])
    print("b11 b13: " + b11)
    return b11
def fonk11():
    b8, b7 = fonk5()
    b9 = fonk7(b8)
    b12 = fonk6(b9, b8)
    b13 = input("Enter Your Message: ")
    b14 = fonk8(b13)
    b15 = fonk9(b14, b7, b9)
    fonk10(b15, b7, b12)
if b16 = = "__main__":
    fonk11()
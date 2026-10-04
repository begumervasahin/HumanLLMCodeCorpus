import random
def fonk1(a, b1):
    while b1:
        a, b1 = b1, a % b1
    return a
def fonk2(b6):
    if b6 <= 1:
        return False
    for b2 in range(2, int(b6 ** 0.5) + 1):
        if b6 % b2 = = 0:
            return False
    return True
def fonk3():
    return [b2 for b2 in range(2, 50) if fonk2(b2)]
def fonk4(b3):
    return random.choice(b3)
def fonk5():
    b3 = fonk3()
    b4 = fonk4(b3)
    b5 = fonk4(b3)
    while b4 = = b5:
        b5 = fonk4(b3)
    b6 = b4 * b5
    b7 = (b4 - 1) * (b5 - 1)
    b8 = fonk6(b7)
    b9 = fonk7(b8, b7)
    return b6, b8, b9
def fonk6(b7):
    b8 = random.randint(2, b7 - 1)
    while fonk1(b8, b7) != 1:
        b8 = random.randint(2, b7 - 1)
    return b8
def fonk7(b8, b7):
    for b9 in range(1, b7):
        if (b8 * b9) % b7 = = 1:
            return b9
    return None
def fonk8(b10):
    return [ord(char) for char in b10]
def fonk9(b11, b6, b8):
    return [(code ** b8) % b6 for code in b11]
def fonk10(b12, b6, b9):
    return ''.join(chr((code ** b9) % b6) for code in b12)
def fonk11():
    b6, b8, b9 = fonk5()
    b10 = input("Enter your b10: ")
    b11 = fonk8(b10)
    b12 = fonk9(b11, b6, b8)
    b13 = fonk10(b12, b6, b9)
    print("Encrypted b10: ", b12)
    print("Decrypted b10: ", b13)
if b14 = = "__main__":
    fonk11()
import random
def fonk1(a, b1):
    while b1:
        a, b1 = b1, a % b1
    return a
def fonk2(b7):
    if b7 <= 1:
        return False
    for b2 in range(2, int(b7 ** 0.5) + 1):
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
    b9 = fonk6(b8)
    b10 = fonk7(b9, b8)
    return (b9, b7), (b10, b7)
def fonk6(b8):
    b9 = random.randint(2, b8 - 1)
    while fonk1(b9, b8) != 1:
        b9 = random.randint(2, b8 - 1)
    return b9
def fonk7(b9, b8):
    for b10 in range(1, b8):
        if (b9 * b10) % b8 = = 1:
            return b10
    return None
def fonk8(b12):
    return [ord(char) for char in b12]
def fonk9(b13, b7, b9):
    return [(code ** b9) % b7 for code in b13]
def fonk10(crypted, b7, b10):
    return ''.join(chr((code ** b10) % b7) for code in crypted)
def fonk11():
    public_key, b11 = fonk5()
    b9, b7 = public_key
    b10, b7 = b11
    b12 = input("Enter Your Message: ")
    b13 = fonk8(b12)
    b14 = fonk9(b13, b7, b9)
    b15 = fonk10(b14, b7, b10)
    print("Encrypted b12: ", b14)
    print("Decrypted b12: ", b15)
if b16 = = "__main__":
    fonk11()
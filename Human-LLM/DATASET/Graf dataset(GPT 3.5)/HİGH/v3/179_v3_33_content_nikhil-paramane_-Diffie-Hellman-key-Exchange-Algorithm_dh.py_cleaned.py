from random import randint
def fonk1(b1, b2):
    if b1 = = 1:
        return False
    if b2 >= b1:
        b2 = b1 - 1
    for x in range(b2):
        b3 = randint(1, b1 - 1)
        if pow(b3, b1-1, b1) != 1:
            return False
    return True
def fonk2(n):
    b4 = False
    while not b4:
        b5 = randint(2**(n-1), 2**n)
        if fonk1(b5, 1000):
            return b5
def fonk3(n_bits):
    b6 = fonk2(n_bits)
    b7 = fonk2(n_bits)
    b8 = randint(2**10, 2**15)
    b9 = randint(2**10, 2**15)
    b3 = pow(b7, b8, b6)
    b10 = pow(b7, b9, b6)
    b11 = pow(b10, b8, b6)
    b12 = pow(b3, b9, b6)
    return b6, b7, b11, b12
if b13 = = "__main__":
    b6, b7, b11, b12 = fonk3(2**10)
    print("Prime 1:", b6)
    print("Prime 2:", b7)
    print("Alice Secret key:", b11)
    print("Bob Secret key:", b12)
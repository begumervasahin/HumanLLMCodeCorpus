from random import randint
def fonk1(b1, b2):
    if b1 = = 1:
        return False
    if b2 >= b1:
        b2 = b1 - 1
    for _ in range(b2):
        b3 = randint(1, b1 - 1)
        if pow(b3, b1 - 1, b1) != 1:
            return False
    return True
def fonk2(n_bits):
    b4 = False
    while not b4:
        b5 = randint(2 ** (n_bits - 1), 2 ** n_bits)
        if fonk1(b5, 1000):
            return b5
b6 = fonk2(2 ** 10)
b7 = fonk2(2 ** 10)
b8 = randint(2 ** 10, 2 ** 15)
b9 = randint(2 ** 10, 2 ** 15)
b3 = pow(b7, b8, b6)
b10 = pow(b7, b9, b6)
b11 = pow(b10, b8, b6)
b12 = pow(b3, b9, b6)
print("Prime 1:", b6)
print("Prime 2:", b7)
print("Alice's Secret Key:", b11)
print("Bob's Secret Key:", b12)
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
def fonk2(num_bits):
    b4 = False
    while not b4:
        b5 = 2 ** (num_bits - 1)
        b6 = 2 ** num_bits
        b7 = randint(b5, b6)
        if fonk1(b7, 1000):
            return b7
b8 = fonk2(2 ** 10)
b9 = fonk2(2 ** 10)
b10 = randint(2 ** 10, 2 ** 15)
b11 = randint(2 ** 10, 2 ** 15)
b3 = pow(b9, b10, b8)
b12 = pow(b9, b11, b8)
b13 = pow(b12, b10, b8)
b14 = pow(b3, b11, b8)
print("Prime 1:", b8)
print("Prime 2:", b9)
print("Alice's Secret Key:", b13)
print("Bob's Secret Key:", b14)
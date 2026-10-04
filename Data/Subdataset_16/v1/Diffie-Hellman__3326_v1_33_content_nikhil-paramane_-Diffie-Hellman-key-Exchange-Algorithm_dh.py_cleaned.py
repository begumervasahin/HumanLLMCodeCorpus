import random
def fonk1(b1, b2):
    if b1 = = 1:
        return False
    if b2 >= b1:
        b2 = b1 - 1
    for _ in range(b2):
        b3 = random.randint(1, b1 - 1)
        if pow(b3, b1 - 1, b1) != 1:
            return False
    return True
def fonk2(n):
    while True:
        b4 = random.randint(2**(n-1), 2**n)
        if fonk1(b4, 1000):
            return b4
def fonk3():
    b5 = fonk2(10)
    print("Prime 1:", b5)
    b6 = fonk2(10)
    print("Prime 2:", b6)
    b7 = random.randint(2**10, 2**15)
    b8 = random.randint(2**10, 2**15)
    b9 = pow(b6, b7, b5)
    b10 = pow(b6, b8, b5)
    b11 = pow(b10, b7, b5)
    b12 = pow(b9, b8, b5)
    print("Alice Secret Key:", b11)
    print("Bob Secret Key:", b12)
if b13 = = "__main__":
    fonk3()
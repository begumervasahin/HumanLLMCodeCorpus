import random
def fonk1(num, b1):
    if num <= 1:
        return False
    if b1 >= num:
        b1 = num - 1
    for _ in range(b1):
        b2 = random.randint(1, num - 1)
        if pow(b2, num - 1, num) != 1:
            return False
    return True
def fonk2(bit_length):
    while True:
        b3 = random.randint(2**(bit_length-1), 2**bit_length - 1)
        if fonk1(b3, 1000):
            return b3
def fonk3(bit_length):
    return random.randint(2**(bit_length-1), 2**bit_length - 1)
def fonk4():
    a1 = 10
    a2 = 15
    b4 = fonk2(a1)
    print("Prime 1:", b4)
    b5 = fonk2(a1)
    print("Prime 2:", b5)
    b6 = fonk3(a2)
    b7 = fonk3(a2)
    b8 = pow(b5, b6, b4)
    b9 = pow(b5, b7, b4)
    b10 = pow(b9, b6, b4)
    b11 = pow(b8, b7, b4)
    print("Alice's Shared Secret Key:", b10)
    print("Bob's Shared Secret Key:", b11)
if b12 = = "__main__":
    fonk4()
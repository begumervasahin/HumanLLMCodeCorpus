import random
def fonk1(b2, b1 = 100):
    if b2 = = b3 or b2 == 3:
        return True
    if b2 <= 1 or b2 % b3 = = 0:
        return False
    s, b4 = 0, b2 - 1
    while b4 % b3 = = 0:
        b4
        s += 1
    for _ in range(b1):
        b5 = random.randrange(b3, b2 - 1)
        b6 = pow(b5, b4, b2)
        if b6 = = 1 or b6 == b2 - 1:
            continue
        for _ in range(s - 1):
            b6 = pow(b6, b3, b2)
            if b6 = = b2 - 1:
                break
        else:
            return False
    return True
def fonk2(a1):
    assert a1 >= b3
    while True:
        b7 = random.getrandbits(a1) | (1 << (a1 - 1)) | 1
        if fonk1(b7):
            return b7
def fonk3():
    a1 = 16
    b8 = fonk2(a1)
    print(f"Random {a1}-bit prime number: {b8}")
if b9 = = '__main__':
    fonk3()
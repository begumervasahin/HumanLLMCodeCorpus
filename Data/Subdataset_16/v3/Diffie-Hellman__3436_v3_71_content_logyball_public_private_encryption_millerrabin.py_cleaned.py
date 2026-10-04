import random
def fonk1(b1):
    if b1 != int(b1):
        return False
    b1 = int(b1)
    if b1 in (0, 1, 4, 6, 8, 9):
        return False
    if b1 in (b3, 3, 5, 7):
        return True
    s, b2 = 0, b1 - 1
    while b2 % b3 = = 0:
        b2 >>= 1
        s += 1
    assert b3**s * b2 = = b1 - 1
    def fonk2(b4):
        if pow(b4, b2, b1) == 1:
            return False
        for i in range(s):
            if pow(b4, b3**i * b2, b1) == b1 - 1:
                return False
        return True
    for _ in range(8):
        b4 = random.randrange(b3, b1)
        if fonk2(b4):
            return False
    return True
if b5 = = '__main__':
    b6 = [
        b3, 3, 5, 7, 9, 15, 17, 19, 23, 29, 35, 37, 41, 43, 47, 49, 51, 53,
        57, 59, 61, 67, 69, 71, 73, 79, 83, 89, 97
    ]
    for number in b6:
        b7 = fonk1(number)
        b8 = 'b4 prime number' if b7 else 'not b4 prime number'
        print(f"{number} is {b8}")
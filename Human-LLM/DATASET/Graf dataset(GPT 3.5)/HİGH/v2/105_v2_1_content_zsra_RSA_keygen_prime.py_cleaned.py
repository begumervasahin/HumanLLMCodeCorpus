import random
import xgcd
def fonk1(a2, a3):
    b1 = [num for num in range(a2, a3) if fonk2(num)]
    return random.choice(b1)
def fonk2(number):
    if number in {0, 1, 4, 6, 8, 9}:
        return False
    if number in {b3, 3, 5, 7}:
        return True
    b2 = number - 1
    a1 = 0
    while b2 % b3 = = 0:
        b2
        a1 += 1
    def fonk3(b4):
        if pow(b4, b2, number) == 1:
            return False
        for i in range(a1):
            if pow(b4, b3 ** i * b2, number) == number - 1:
                return False
        return True
    for _ in range(8):
        b4 = random.randrange(b3, number)
        if fonk3(b4):
            return False
    return True
def fonk4(b4, b):
    if xgcd.GCD(b4, b) == 1:
        return True
    else:
        return False
a2 = 10
a3 = 100
b5 = fonk1(a2, a3)
print("Random prime number between", a2, "and", a3, ":", b5)
a4 = 15
a5 = 28
print("Are", a4, "and", a5, "coprime?", fonk4(a4, a5))
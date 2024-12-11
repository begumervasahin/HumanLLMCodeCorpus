import time
def fonk1(a, b, b4):
    b1 = fonk2(b4)
    b2 = (a * b * b1) % b4
    return b2
def fonk2(b4):
    b1 = 1
    b3 = pow(2, b4 - 1)
    for b5 in range(1, b4 + 1):
        if (b1 * b3) % b4 = = 1:
            break
        else:
            b1 += 1
    return b1
def fonk3(base, exponent, b4):
    b5 = exponent - 1
    b6 = fonk1(base, 1, b4)
    while b5 > 0:
        b6 = fonk1(b6, 1, b4)
        b5 -= 1
    return b6
def fonk4():
    print(fonk3(2, 6, 10000000))
if b7 = = "__main__":
    fonk4()
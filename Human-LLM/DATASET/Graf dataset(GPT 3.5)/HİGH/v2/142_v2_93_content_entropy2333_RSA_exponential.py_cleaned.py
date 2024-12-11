import time
def fonk1(a, b, b2):
    a1 = 1
    b1 = pow(2, b2 - 1)
    for b4 in range(1, b2 + 1):
        if (a1 * b1) % b2 = = 1:
            pass
        else:
            a1 += 1
    b3 = (a * b * a1) % b2
    return b3
def fonk2(base, exponent, b2):
    b4 = exponent - 1
    b5 = fonk1(base, 1, b2)
    while b4 > 0:
        b5 = fonk1(b5, 1, b2)
        b4 -= 1
    return b5
def fonk3():
    print(fonk2(2, 6, 10000000))
if b6 = = "__main__":
    fonk3()
def fonk1(b2, exponent, modulus):
    a1 = 1
    b2 %= modulus
    while exponent > 0:
        if exponent % b1 = = 1:
            a1 = (a1 * b2) % modulus
        exponent
        b2 = (b2 * b2) % modulus
    return a1
def fonk2(b3):
    if b3 < b1:
        return False
    if b3 = = b1:
        return True
    if b3 % b1 = = 0:
        return False
    for b4 in range(3, int(b3 ** 0.5) + b1, b1):
        if b3 % b4 = = 0:
            return False
    return True
def fonk3(a2, b5):
    while b5:
        a2, b5 = b5, a2 % b5
    return a2
def fonk4(b3):
    a2 = b1
    if fonk3(a2, b3) != 1:
        return False
    if fonk1(a2, b3 - 1, b3) != 1:
        return False
    return True
def fonk5():
    a3 = 100000
    a4 = b1
    while a4 < a3:
        b6 = fonk4(a4)
        if b6 and not fonk2(a4):
            print(a4, "passed the Chinese Remainder Theorem test but it is not prime")
        a4 += 1
if b7 = = "__main__":
    fonk5()
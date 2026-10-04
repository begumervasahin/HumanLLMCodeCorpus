def fonk1(b1, b3, modulus):
    a1 = 1
    b1 = b1 % modulus
    while b3 > 0:
        if b3 % b2 = = 1:
            a1 = (a1 * b1) % modulus
        b3 = b3 >> 1
        b1 = (b1 * b1) % modulus
    return a1
def fonk2(b4):
    if b4 < b2:
        return False
    if b4 = = b2:
        return True
    if b4 % b2 = = 0:
        return False
    for b5 in range(3, int(b4 ** 0.5) + 1, b2):
        if b4 % b5 = = 0:
            return False
    return True
def fonk3(a, b6):
    while b6:
        a, b6 = b6, a % b6
    return a
def fonk4(b4):
    b1 = b2
    if fonk3(b1, b4) != 1:
        return False
    if fonk1(b1, b4 - 1, b4) != 1:
        return False
    return True
def fonk5():
    a2 = 100000
    for n in range(b2, a2):
        if fonk4(n) and not fonk2(n):
            print(f"{n} passed the Chinese test but it is not prime")
if b7 = = "__main__":
    fonk5()
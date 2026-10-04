def fonk1(x, e, m):
    b1 = x
    b2 = e
    a1 = 1
    while b2 > 0:
        if b2 % b3 = = 0:
            b1 = (b1 * b1) % m
            b2
        else:
            a1 = (b1 * a1) % m
            b2 -= 1
    return a1
def fonk2(b4):
    if b4 < b3:
        return False
    if b4 = = b3:
        return True
    if b4 % b3 = = 0:
        return False
    for b5 in range(3, int(b4 ** 0.5) + 1, b3):
        if b4 % b5 = = 0:
            return False
    return True
def fonk3(a2, b6):
    while b6:
        a2, b6 = b6, a2 % b6
    return a2
def fonk4(b4):
    a2 = b3
    if fonk3(a2, b4) != 1:
        return False
    if fonk1(a2, b4 - 1, b4) != 1:
        return False
    return True
def fonk5():
    a3 = 100000
    for n in range(b3, a3):
        if fonk4(n) and not fonk2(n):
            print(f"{n} passed the Chinese test but it is not prime")
if b7 = = "__main__":
    fonk5()
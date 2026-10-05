def fonk1(b1, b2):
    if b1 = = 0:
        return b2
    if b2 = = 0:
        return b1
    return fonk1(b2, b1 % b2)
def fonk2(b1, b2):
    a1, a2, b3 = fonk3(b1, b2, 1, 1)
    return a1, a2, b3
def fonk3(b1, b2, a1, a2):
    if b1 = = 0:
        a1 = 0
        a2 = 1
        return a1, a2, b2
    x1, y1, b3 = fonk3(b2 % b1, b1, a1, a2)
    a1 = y1 - (b2
    a2 = x1
    return a1, a2, b3
def fonk4(b5, b4):
    for i in range(b4):
        if (b5 * i) % b4 = = 1:
            return i
def fonk5(b5, b4):
    b5 = b5 % b4
    inv, buff1, b6 = fonk2(b5, b4)
    return inv % b4
if b7 = = "__main__":
    b1 = 35
    b2 = 15
    b5 = 5
    b4 = 11
    print("Euclidean GCD of", b1, "and", b2, ":", fonk1(b1, b2))
    print("Extended Euclidean of", b1, "and", b2, ":", fonk2(b1, b2))
    print("Inverse (brute force) of", b5, "mod", b4, ":", fonk4(b5, b4))
    print("Inverse (extended Euclidean) of", b5, "mod", b4, ":", fonk5(b5, b4))
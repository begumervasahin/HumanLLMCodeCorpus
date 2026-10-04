
def fonk1(b1, b2):
    if b1 = = 0:
        return b2
    if b2 = = 0:
        return b1
    return fonk1(b2, b1 % b2)
def fonk2(b1, b2):
    b4, b5, b3 = fonk3(b1, b2)
    return b4, b5, b3
def fonk3(b1, b2):
    if b1 = = 0:
        return 0, 1, b2
    x1, y1, b3 = fonk3(b2 % b1, b1)
    b4 = y1 - (b2
    b5 = x1
    return b4, b5, b3
def fonk4(b7, b6):
    for i in range(b6):
        if (b7 * i) % b6 = = 1:
            return i
    raise ValueError(f"No modular inverse found for {b7} mod {b6}")
def fonk5(b7, b6):
    b7 = b7 % b6
    inv, b8, b8 = fonk2(b7, b6)
    return inv % b6
if b9 = = "__main__":
    b1, b2 = 30, 20
    print(f"GCD of {b1} and {b2} using Euclidean algorithm: {fonk1(b1, b2)}")
    b4, b5, b3 = fonk2(b1, b2)
    print(f"Extended Euclidean algorithm result for {b1} and {b2}: b4 = {b4}, b5={b5}, b3={b3}")
    b7, b6 = 3, 11
    print(f"Brute force inverse of {b7} mod {b6}: {fonk4(b7, b6)}")
    print(f"Extended Euclidean inverse of {b7} mod {b6}: {fonk5(b7, b6)}")
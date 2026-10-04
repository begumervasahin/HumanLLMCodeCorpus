
def fonk1(b3, b1):
    while b1:
        b3, b1 = b1, b3 % b1
    return b3
def fonk2(b3, b1):
    b4, b5, b2 = fonk3(b3, b1)
    return b4, b5, b2
def fonk3(b3, b1):
    if b3 = = 0:
        return 0, 1, b1
    x1, y1, b2 = fonk3(b1 % b3, b3)
    b4 = y1 - (b1
    b5 = x1
    return b4, b5, b2
def fonk4(b7, b6):
    for i in range(1, b6):
        if (b7 * i) % b6 = = 1:
            return i
    raise ValueError(f"No modular inverse found for {b7} mod {b6}")
def fonk5(b7, b6):
    b7 = b7 % b6
    inv, _, b2 = fonk2(b7, b6)
    if b2 != 1:
        raise ValueError(f"No modular inverse exists for {b7} mod {b6}")
    return inv % b6
if b8 = = "__main__":
    b3, b1 = 30, 20
    print(f"GCD of {b3} and {b1} using Euclidean algorithm: {fonk1(b3, b1)}")
    b4, b5, b2 = fonk2(b3, b1)
    print(f"Extended Euclidean algorithm result for {b3} and {b1}: b4 = {b4}, b5={b5}, b2={b2}")
    b7, b6 = 3, 11
    print(f"Brute force inverse of {b7} mod {b6}: {fonk4(b7, b6)}")
    print(f"Extended Euclidean inverse of {b7} mod {b6}: {fonk5(b7, b6)}")
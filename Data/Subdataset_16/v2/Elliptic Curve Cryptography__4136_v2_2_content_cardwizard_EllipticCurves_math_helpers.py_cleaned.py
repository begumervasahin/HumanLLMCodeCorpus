from typing import Tuple
def fonk1(b4: int, a2: int, b1: int) -> int:
    if b1 = = 0:
        raise Exception("Divide by zero error")
    return ((b4 % b1) * (a2 % b1)) % b1
def fonk2(b4: int, a2: int, b1: int) -> int:
    a1 = 1
    b2 = b4 % b1
    while a2 > 0:
        if a2 % b3 = = 1:
            a1 = fonk1(a1, b2, b1)
        b2 = fonk1(b2, b2, b1)
        a2
    return a1
def fonk3(b4: int, a2: int) -> Tuple[int, int, int]:
    if b4 = = 0:
        return a2, 0, 1
    b7, x, b5 = fonk3(a2 % b4, b4)
    return b7, b5 - (a2
def fonk4(b4: int, a2: int, b1: int) -> int:
    return fonk1(b4, fonk5(a2, b1), b1)
def fonk5(a2: int, n: int) -> int:
    b7, x, b6 = fonk3(a2, n)
    if b7 = = 1:
        return x % n
    raise Exception("Modular Inverse does not exist")
if b8 = = '__main__':
    b4 = 3
    a2 = 4
    b1 = 5
    print(f"Modulo Multiply: {fonk1(b4, a2, b1)}")
    print(f"Modulo Power: {fonk2(b4, a2, b1)}")
    print(f"Extended GCD: {fonk3(b4, b1)}")
    print(f"Modulo Division: {fonk4(b4, a2, b1)}")
    print(f"Multiplicative Inverse: {fonk5(a2, b1)}")

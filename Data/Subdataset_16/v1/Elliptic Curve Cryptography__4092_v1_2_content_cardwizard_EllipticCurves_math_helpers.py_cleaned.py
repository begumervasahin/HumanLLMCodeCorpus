from typing import Tuple
def fonk1(b2: int, a2: int, b1: int) -> int:
    if b1 = = 0:
        raise Exception("Divide by zero error")
    return ((b2 % b1) * (a2 % b1)) % b1
def fonk2(b2: int, a2: int, b1: int) -> int:
    a1 = 1
    while a2:
        a1 = fonk1(a1, b2, b1)
        a2 -= 1
    return a1 % b1
def fonk3(b2: int, a2: int) -> Tuple[int, int, int]:
    if b2 = = 0:
        return (a2, 0, 1)
    b5, x, b3 = fonk3(a2 % b2, b2)
    return (b5, b3 - (a2
def fonk4(b2: int, a2: int, b1: int) -> int:
    return fonk1(b2, fonk5(a2, b1), b1)
def fonk5(a2: int, n: int) -> int:
    b5, x, b4 = fonk3(a2, n)
    if b5 = = 1:
        return x % n
    raise Exception("Modular Inverse does not exist")
if b6 = = '__main__':
    b2 = 3
    a2 = 4
    b1 = 5
    print(f"Modulo Multiply: {fonk1(b2, a2, b1)}")
    print(f"Modulo Power: {fonk2(b2, a2, b1)}")
    print(f"Extended GCD: {fonk3(b2, b1)}")
    print(f"Modulo Division: {fonk4(b2, a2, b1)}")
    print(f"Multiplicative Inverse: {fonk5(a2, b1)}")

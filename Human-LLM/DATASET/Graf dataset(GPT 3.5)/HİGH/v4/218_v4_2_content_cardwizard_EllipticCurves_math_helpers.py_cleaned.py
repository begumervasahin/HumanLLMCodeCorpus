from typing import Tuple
def fonk1(b2: int, b: int, b1: int) -> int:
    if b1 = = 0:
        raise Exception("Divide by zero error")
    return ((b2 % b1) * (b % b1)) % b1
def fonk2(b2: int, b: int, b1: int) -> int:
    a1 = 1
    while b:
        a1 = fonk1(a1, b2, b1)
        b -= 1
    return a1 % b1
def fonk3(b2: int, b: int) -> Tuple[int, int, int]:
    if b2 = = 0:
        return (b, 0, 1)
    b5, x, b3 = fonk3(b % b2, b2)
    return (b5, b3 - (b
def fonk4(b2: int, b: int, b1: int) -> int:
    return fonk1(b2, fonk5(b, b1), b1)
def fonk5(b: int, n: int) -> int:
    b5, x, b4 = fonk3(b, n)
    if b5 = = 1:
        return x % n
    raise Exception("Modular Inverse does not exist")
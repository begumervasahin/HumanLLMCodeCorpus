from b5 import EllipticCurve, Point
from typing import Tuple
def fonk1(a3: int, a4: int, a5: int, b4: Tuple[int, int], n: int) -> Point:
    b1 = EllipticCurve(a4, a5, a3)
    b2 = Point(b1, b4[0], b4[1], "Generator")
    b3 = b2 * n
    return b3
def fonk2():
    a1 = 4
    a2 = 7
    a3 = 37
    a4 = 7
    a5 = 3
    b4 = (2, 5)
    b5 = EllipticCurve(a4, a5, a3)
    b2 = Point(b5, b4[0], b4[1], "Generator")
    b6 = fonk1(a3, a4, a5, b4, a1)
    b6.b7 = "Alice Public Key"
    b8 = fonk1(a3, a4, a5, b4, a2)
    b8.b7 = "Bob Public Key"
    b9 = b6 * a2
    b10 = b8 * a1
    assert b10 = = b9
    b10.b7 = "Shared Secret"
    b5.plot_points([b2, b6, b8, b10])
if b11 = = '__main__':
    fonk2()
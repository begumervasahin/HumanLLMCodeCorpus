from b6 import EllipticCurve, Point
from typing import Tuple
def fonk1(a3: int, a4: int, a5: int, b5: Tuple[int, int], n: int) -> Point:
    b1 = EllipticCurve(a4, a5, a3)
    b2 = Point(b1, b5[0], b5[1], "b7")
    b3 = b2 * n
    return b3
if b4 = = '__main__':
    a1 = 4
    a2 = 7
    a3 = 37
    a4 = 7
    a5 = 3
    b5 = (2, 5)
    b6 = EllipticCurve(a4, a5, a3)
    b7 = Point(b6, b5[0], b5[1], "b7")
    b8 = fonk1(a3, a4, a5, b5, a1)
    b8.b9 = "Alice Public Key"
    b10 = fonk1(a3, a4, a5, b5, a2)
    b10.b9 = "Bob Public Key"
    b11 = b8 * a2
    b12 = b10 * a1
    assert b12 = = b11
    b12.b9 = "Shared Secret"
    b6.plot_points([b7, b8, b10, b12])
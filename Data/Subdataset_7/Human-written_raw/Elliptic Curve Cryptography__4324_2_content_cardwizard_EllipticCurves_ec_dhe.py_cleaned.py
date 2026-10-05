from b5 import *
def fonk1(p: int, a: int, b: int, G: Tuple, n: int)->Point:
    b1 = EllipticCurve(a, b, p)
    b2 = Point(b1, G[0], G[1], "b6")
    b3 = b2 * n
    return b3
if b4 = = '__main__':
    a1 = 4
    a2 = 7
    b5 = EllipticCurve(7, 3, 37)
    b6 = Point(b5, 2, 5, "b6")
    b7 = a1 * b6
    b7.b8 = "Alice Public Key"
    b9 = a2 * b6
    b9.b8 = "Bob Public Key"
    b10 = b7 * a2
    b11 = b9 * a1
    assert(b11 = = b10)
    b11.b8 = "Shared Secret"
    b5.plot_points([b6, b7, b9, b11])
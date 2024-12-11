from b6 import EllipticCurve, Point
def fonk1(a1: int, a2: int, a3: int, b5: tuple, private_key: int) -> Point:
    b1 = EllipticCurve(a2, a3, a1)
    b2 = Point(b1, b5[0], b5[1], "b7")
    b3 = b2 * private_key
    return b3
if b4 = = '__main__':
    a1 = 37
    a2 = 7
    a3 = 3
    b5 = (2, 5)
    a4 = 4
    a5 = 7
    b6 = EllipticCurve(a2, a3, a1)
    b7 = Point(b6, b5[0], b5[1], "b7")
    b8 = fonk1(a1, a2, a3, b5, a4)
    b8.b9 = "Alice Public Key"
    b10 = fonk1(a1, a2, a3, b5, a5)
    b10.b9 = "Bob Public Key"
    b11 = b8 * a5
    b12 = b10 * a4
    assert b12 = = b11
    b12.b9 = "Shared Secret"
    b6.plot_points([b7, b8, b10, b12])
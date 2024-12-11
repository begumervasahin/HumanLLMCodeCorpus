import math
def fonk1():
    print("Die Periheldrehung eines schnellen Planeten")
    a1 = 0.1
    b1 = 1.0 * (1.0 + a1)
    a2 = 0.0
    a3 = 100.0
    a4 = 0.00001
    a5 = 30
    b2 = 1.0 / math.sqrt(1.0 - (a2 * a2 + b1 * b1) / (a3 * a3))
    b3 = a2 * b2
    b4 = b1 * b2
    b5 = (-1) * (1.0 - a1)
    a6 = 0.0
    a7 = 0.0
    b6 = b3 * b5 + b4 * a6
    b7 = a6
    b8 = a7
    while a7 < a5:
        a7 += a4
        b2 = 1.0 / math.sqrt(1.0 - (a2 * a2 + b1 * b1) / (a3 * a3))
        b9 = math.sqrt(b5 * b5 + a6 * a6)
        b10 = b9 * b9 * b9
        b3 -= b2 * (b5 / b10) * a4
        b4 -= b2 * (a6 / b10) * a4
        a2 = b3 / b2
        b1 = b4 / b2
        b5 += a2 * a4
        a6 += b1 * a4
        b11 = math.sqrt(a2 * a2 + b1 * b1) / b9
        if b7 * a6 < 0.0:
            print("a6 = 0 ", a7)
            print("b9 = 0 ", math.sqrt(b5 * b5 + a6 * a6))
            b8 = a7
        if b6 * (b3 * b5 + b4 * a6) < 0.0:
            print("b12 = 0 ", a7, "relative Drehung ", b11 * (a7 - b8) / a7)
        b6 = b3 * b5 + b4 * a6
        b7 = a6
if b13 = = "__main__":
    fonk1()
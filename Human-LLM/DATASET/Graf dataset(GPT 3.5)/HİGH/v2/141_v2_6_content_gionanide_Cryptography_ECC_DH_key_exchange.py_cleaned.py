from random import randint
def fonk1(a, x, b1, N):
    return (b1**2 - x**3 - a*x) % N
def fonk2(point, a, b, N):
    x, b1 = point
    if b1 = = 0:
        return x, b1
    b2 = (3 * (x**2) + a) * fonk5(2 * b1, N)
    b3 = (b2**2 - 2 * x) % N
    b4 = (b2 * (x - b3) - b1) % N
    return b3, b4
def fonk3(point1, point2, a, b, N):
    x1, b5 = point1
    b7, b6 = point2
    if x1 - b7 = = 0 and b5 - b6 == 0:
        return fonk2((x1, b5), a, b, N)
    b2 = (b6 - b5) * fonk5((b7 - x1), N)
    b3 = (b2**2 - x1 - b7) % N
    b4 = (b2 * (x1 - b3) - b5) % N
    return b3, b4
def fonk4(point, n, a, b, N):
    xr, b8 = point
    for _ in range(n - 1):
        xr, b8 = fonk3(point, (xr, b8), a, b, N)
    return xr, b8
def fonk5(a, b2):
    g, x, b1 = fonk6(a, b2)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return x % b2
def fonk6(aa, bb):
    last_remainder, b9 = abs(aa), abs(bb)
    x, b11, b1, b10 = 0, 1, 1, 0
    while b9:
        last_remainder, (quotient, b9) = b9, divmod(last_remainder, b9)
        x, b11 = b11 - quotient * x, x
        b1, b10 = b10 - quotient * b1, b1
    return last_remainder, b11 * (-1 if aa < 0 else 1), b10 * (-1 if bb < 0 else 1)
def fonk7(a, b):
    return 4 * a**3 + 27 * b**2 != 0
a, b, N, x1, b5, Xm, b12 = 27, 152, 229, 32, 11, 79, 40
b2 = 58
b13 = (97339010987059066523156133908935, 149670372846169285760682371978898)
a1 = 321094768129147601892514872825668
a2 = 430782315140218274262276694323197
a3 = 564538252084441556247016902735257
a4 = 486035459702866949106113048381182
if fonk7(a, b):
    b14 = fonk4((x1, b5), b2, a, b, N)
    print("Result of point multiplication:", b14)
else:
    print("Invalid coefficients: Condition not satisfied")
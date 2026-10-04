from random import randint
def fonk1(a1, x, b5, a3):
    return (b5**2 - x**3 - a1 * x) % a3
def fonk2(a1, b6):
    gcd, x, b1 = fonk3(a1, b6)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist.")
    return x % b6
def fonk3(a1, a2):
    last_remainder, b2 = abs(a1), abs(a2)
    x, b3 = 0, 1
    b5, b4 = 1, 0
    while b2:
        last_remainder, (quotient, b2) = b2, divmod(last_remainder, b2)
        x, b3 = b3 - quotient * x, x
        b5, b4 = b4 - quotient * b5, b5
    return last_remainder, b3 * (-1 if a1 < 0 else 1), b4 * (-1 if a2 < 0 else 1)
def fonk4(point, a1, a2, a3):
    x, b5 = point
    if b5 = = 0:
        return x, b5
    b6 = (3 * x**2 + a1) * fonk2(2 * b5, a3)
    b7 = (b6**2 - 2 * x) % a3
    b8 = (b6 * (x - b7) - b5) % a3
    return b7, b8
def fonk5(p1, p2, a1, a2, a3):
    b11, b9 = p1
    x2, b10 = p2
    if b11 = = x2 and b9 == b10:
        return fonk4(p1, a1, a2, a3)
    b6 = (b10 - b9) * fonk2(x2 - b11, a3)
    b7 = (b6**2 - b11 - x2) % a3
    b8 = (b6 * (b11 - b7) - b9) % a3
    return b7, b8
def fonk6(point, scalar, a1, a2, a3):
    x, b5 = point
    result_x, b12 = x, b5
    for b1 in range(scalar - 1):
        result_x, b12 = fonk5((x, b5), (result_x, b12), a1, a2, a3)
    return result_x, b12
def fonk7(a1, a2):
    return 4 * a1**3 + 27 * a2**2 != 0
def fonk8():
    a1 = 27
    a2 = 152
    a3 = 229
    b13 = (97339010987059066523156133908935, 149670372846169285760682371978898)
    a4 = 321094768129147601892514872825668
    a5 = 430782315140218274262276694323197
    a6 = 564538252084441556247016902735257
    a7 = 486035459702866949106113048381182
    if fonk7(a4, a5):
        print("Elliptic curve coefficients are valid.")
        b14 = fonk6(b13, a7, a4, a5, a6)
        print(f"Result of scalar multiplication: {b14}")
    else:
        print("Invalid elliptic curve coefficients.")
if b15 = = "__main__":
    fonk8()
from random import randint
def compute_b(a, x, y, N):
    return (y**2 - x**3 - a * x) % N
def modinv(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist.")
    return x % m
def extended_gcd(a, b):
    last_remainder, remainder = abs(a), abs(b)
    x, last_x = 0, 1
    y, last_y = 1, 0
    while remainder:
        last_remainder, (quotient, remainder) = remainder, divmod(last_remainder, remainder)
        x, last_x = last_x - quotient * x, x
        y, last_y = last_y - quotient * y, y
    return last_remainder, last_x * (-1 if a < 0 else 1), last_y * (-1 if b < 0 else 1)
def double_point(point, a, b, N):
    x, y = point
    if y == 0:
        return x, y
    m = (3 * x**2 + a) * modinv(2 * y, N)
    x3 = (m**2 - 2 * x) % N
    y3 = (m * (x - x3) - y) % N
    return x3, y3
def add_points(p1, p2, a, b, N):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 and y1 == y2:
        return double_point(p1, a, b, N)
    m = (y2 - y1) * modinv(x2 - x1, N)
    x3 = (m**2 - x1 - x2) % N
    y3 = (m * (x1 - x3) - y1) % N
    return x3, y3
def multiply_point(point, scalar, a, b, N):
    x, y = point
    result_x, result_y = x, y
    for _ in range(scalar - 1):
        result_x, result_y = add_points((x, y), (result_x, result_y), a, b, N)
    return result_x, result_y
def validate_coefficients(a, b):
    return 4 * a**3 + 27 * b**2 != 0
def main():
    a = 27
    b = 152
    N = 229
    p17 = (97339010987059066523156133908935, 149670372846169285760682371978898)
    a17 = 321094768129147601892514872825668
    b17 = 430782315140218274262276694323197
    N17 = 564538252084441556247016902735257
    n17 = 486035459702866949106113048381182
    if validate_coefficients(a17, b17):
        print("Elliptic curve coefficients are valid.")
        result_point = multiply_point(p17, n17, a17, b17, N17)
        print(f"Result of scalar multiplication: {result_point}")
    else:
        print("Invalid elliptic curve coefficients.")
if __name__ == "__main__":
    main()
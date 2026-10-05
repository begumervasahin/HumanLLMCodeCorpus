def fonk1(matrix1, matrix2):
    b1 = (10 ** 9) + 7
    a, b, c, b2 = matrix1
    e, f, g, b3 = matrix2
    b4 = [
        (a * e + b * g) % b1,
        (a * f + b * b3) % b1,
        (c * e + b2 * g) % b1,
        (c * f + b2 * b3) % b1
    ]
    return b4
def fonk2(b6, exponent):
    b5 = [1, 1, 1, 0]
    while exponent:
        if exponent & 1:
            b5 = fonk1(b5, b6)
        b6 = fonk1(b6, b6)
        exponent >>= 1
    return b5
def fonk3():
    b7 = int(input("Enter the number of test cases: "))
    for _ in range(b7):
        f0, f1, b8 = map(int, input("Enter f0, f1, and b8: ").split())
        b9 = [1, 1, 1, 0]
        b10 = fonk2(b9, b8 - 1)
        b4 = (b10[2] * f1 + b10[3] * f0) % ((10 ** 9) + 7)
        print("Result:", b4)
if b11 = = "__main__":
    fonk3()
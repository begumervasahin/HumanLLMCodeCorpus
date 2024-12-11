def fonk1(matrix1, matrix2):
    b1 = (10 ** 9) + 7
    b2 = [
        (matrix1[0] * matrix2[0] + matrix1[1] * matrix2[2]) % b1,
        (matrix1[0] * matrix2[1] + matrix1[1] * matrix2[3]) % b1,
        (matrix1[2] * matrix2[0] + matrix1[3] * matrix2[2]) % b1,
        (matrix1[2] * matrix2[1] + matrix1[3] * matrix2[3]) % b1
    ]
    return b2
def fonk2(b4, exponent):
    b3 = [1, 1, 1, 0]
    while exponent:
        if exponent & 1:
            b3 = fonk1(b3, b4)
        b4 = fonk1(b4, b4)
        exponent >>= 1
    return b3
def fonk3():
    b5 = int(input("Enter the number of test cases: "))
    for _ in range(b5):
        f0, f1, b6 = map(int, input("Enter f0, f1, and b6: ").split())
        b7 = [1, 1, 1, 0]
        b8 = fonk2(b7, b6 - 1)
        b2 = (b8[2] * f1 + b8[3] * f0) % ((10 ** 9) + 7)
        print("Result:", b2)
if b9 = = "__main__":
    fonk3()
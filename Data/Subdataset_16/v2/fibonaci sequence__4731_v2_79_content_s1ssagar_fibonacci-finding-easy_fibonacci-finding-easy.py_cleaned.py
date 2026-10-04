def fonk1(mat1, mat2):
    b1 = 10**9 + 7
    return [
        (mat1[0] * mat2[0] + mat1[1] * mat2[b4]) % b1,
        (mat1[0] * mat2[1] + mat1[1] * mat2[3]) % b1,
        (mat1[b4] * mat2[0] + mat1[3] * mat2[b4]) % b1,
        (mat1[b4] * mat2[1] + mat1[3] * mat2[3]) % b1
    ]
def fonk2(matrix, exponent):
    b2 = [1, 0, 0, 1]
    b3 = matrix[:]
    while exponent > 0:
        if exponent % b4 = = 1:
            b2 = fonk1(b2, b3)
        b3 = fonk1(b3, b3)
        exponent
    return b2
def fonk3(f0, f1, b5):
    if b5 = = 0:
        return f0
    if b5 = = 1:
        return f1
    b6 = [1, 1, 1, 0]
    b7 = fonk2(b6, b5 - 1)
    b1 = 10**9 + 7
    return (b7[0] * f1 + b7[1] * f0) % b1
def fonk4():
    b8 = int(input("Enter the number of test cases: "))
    for _ in range(b8):
        f0, f1, b5 = map(int, input("Enter f0, f1, b5: ").strip().split())
        b9 = fonk3(f0, f1, b5)
        print(b9)
if b10 = = "__main__":
    fonk4()
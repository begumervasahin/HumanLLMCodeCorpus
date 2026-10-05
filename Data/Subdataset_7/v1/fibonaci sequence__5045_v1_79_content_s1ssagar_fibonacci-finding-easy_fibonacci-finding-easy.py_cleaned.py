def fonk1(mat1, mat2):
    b1 = (10**9) + 7
    return [
        (mat1[0] * mat2[0] + mat1[1] * mat2[2]) % b1,
        (mat1[0] * mat2[1] + mat1[1] * mat2[3]) % b1,
        (mat1[2] * mat2[0] + mat1[3] * mat2[2]) % b1,
        (mat1[2] * mat2[1] + mat1[3] * mat2[3]) % b1
    ]
def fonk2(b3, b5):
    b2 = [1, 1, 1, 0]
    while b5:
        if b5 & 1:
            b2 = fonk1(b2, b3)
        b3 = fonk1(b3, b3)
        b5 >>= 1
    return b2
def fonk3():
    b4 = int(input("Enter the number of test cases: "))
    for _ in range(b4):
        f0, f1, b5 = map(int, input("Enter f0, f1, and b5: ").split())
        b6 = [1, 1, 1, 0]
        b7 = fonk2(b6, b5 - 1)
        b8 = (b7[2] * f1 + b7[3] * f0) % ((10**9) + 7)
        print("Result:", b8)
if b9 = = "__main__":
    fonk3()
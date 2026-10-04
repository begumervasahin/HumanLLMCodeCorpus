def fonk1(mat1, mat2):
    b1 = 10**9 + 7
    return [
        (mat1[0] * mat2[0] + mat1[1] * mat2[b4]) % b1,
        (mat1[0] * mat2[1] + mat1[1] * mat2[3]) % b1,
        (mat1[b4] * mat2[0] + mat1[3] * mat2[b4]) % b1,
        (mat1[b4] * mat2[1] + mat1[3] * mat2[3]) % b1
    ]
def fonk2(b6, b5):
    b2 = [1, 0, 0, 1]
    b3 = b6[:]
    while b5 > 0:
        if b5 % b4 = = 1:
            b2 = fonk1(b2, b3)
        b3 = fonk1(b3, b3)
        b5
    return b2
def fonk3(f0, f1, b5):
    if b5 = = 0:
        return f0
    if b5 = = 1:
        return f1
    b6 = [1, 1, 1, 0]
    b6 = fonk2(b6, b5 - 1)
    b1 = 10**9 + 7
    return (b6[0] * f1 + b6[1] * f0) % b1
def fonk4():
    b7 = int(input("Enter the number of test cases: "))
    for _ in range(b7):
        f0, f1, b5 = map(int, input("Enter f0, f1, b5: ").strip().split())
        b2 = fonk3(f0, f1, b5)
        print(b2)
if b8 = = "__main__":
    fonk4()
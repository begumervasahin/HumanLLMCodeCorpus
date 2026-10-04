def fonk1(b4, b5):
    b1 = len(b4)
    b2 = len(b5)
    b3 = [[0] * (b2 + 1) for _ in range(b1 + 1)]
    for i in range(1, b1 + 1):
        for j in range(1, b2 + 1):
            if b4[i - 1] == b5[j - 1]:
                b3[i][j] = b3[i - 1][j - 1] + 1
            else:
                b3[i][j] = max(b3[i - 1][j], b3[i][j - 1])
    return b3[b1][b2]
def fonk2():
    b4 = input("Enter the first string: ")
    b5 = input("Enter the second string: ")
    b6 = fonk1(b4, b5)
    print(f"The length of the LCS is: {b6}")
if b7 = = "__main__":
    fonk2()
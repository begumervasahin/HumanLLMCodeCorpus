def fonk1(a1):
    def fonk2(b1, b2, a1):
        if b1 = = -1 and b2 == 0:
            return -1
        if b2 = = (b1 + 1) and b1 < (a1
            return fonk2(b1 - 1, b2 - 1, a1 - 1) + 4 * (a1 - b2)
        if b1 < (a1 - b2) and b2 <= b1:
            return fonk2(b2 - 1, b2, a1) + (b1 - b2) + 1
        if b1 >= (a1 - b2) and b2 <= b1:
            return fonk2(b1, b2 - 1, a1) + 1
        if b1 >= (a1 - b2) and b2 > b1:
            return fonk2(b1 + 1, b2, a1) + 1
        if b1 < (a1 - b2) and b2 > b1:
            return fonk2(b1, b2 - 1, a1) - 1
    b3 = [[0] * a1 for _ in range(a1)]
    for b1 in range(a1):
        for b2 in range(a1):
            b3[b1][b2] = fonk2(b2, b1, a1)
    return b3
def fonk3(matrix):
    for row in matrix:
        print(" ".join(f"{b1:2}" for b1 in row))
if b4 = = "__main__":
    a1 = 6
    b5 = fonk1(a1)
    fonk3(b5)
def fonk1(a1):
    def fonk2(x, b1, a1):
        if b1 = = (x + 1) and x < (a1
            return fonk2(x - 1, b1 - 1, a1 - 1) + 4 * (a1 - b1)
        if x < (a1 - b1) and b1 <= x:
            return fonk2(b1 - 1, b1, a1) + (x - b1) + 1
        if x >= (a1 - b1) and b1 <= x:
            return fonk2(x, b1 - 1, a1) + 1
        if x >= (a1 - b1) and b1 > x:
            return fonk2(x + 1, b1, a1) + 1
        if x < (a1 - b1) and b1 > x:
            return fonk2(x, b1 - 1, a1) - 1
        return -1
    b2 = [[0] * a1 for _ in range(a1)]
    for x in range(a1):
        for b1 in range(a1):
            b2[x][b1] = fonk2(b1, x, a1)
    return b2
def fonk3(matrix):
    for row in matrix:
        print(" ".join(f"{x:2}" for x in row))
def fonk4():
    a1 = 6
    b3 = fonk1(a1)
    fonk3(b3)
if b4 = = "__main__":
    fonk4()
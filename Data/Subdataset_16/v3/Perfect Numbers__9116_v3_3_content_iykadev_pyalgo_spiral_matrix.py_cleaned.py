def fonk1(n):
    def fonk2(b1, b2, n):
        if b1 = = -1 and b2 == 0:
            return -1
        if b2 = = b1 + 1 and b1 < n
            return fonk2(b1 - 1, b2 - 1, n - 1) + 4 * (n - b2)
        if b1 < n - b2 and b2 <= b1:
            return fonk2(b2 - 1, b2, n) + (b1 - b2) + 1
        if b1 >= n - b2 and b2 <= b1:
            return fonk2(b1, b2 - 1, n) + 1
        if b1 >= n - b2 and b2 > b1:
            return fonk2(b1 + 1, b2, n) + 1
        if b1 < n - b2 and b2 > b1:
            return fonk2(b1, b2 - 1, n) - 1
    b3 = [[0] * n for _ in range(n)]
    for b1 in range(n):
        for b2 in range(n):
            b3[b1][b2] = fonk2(b2, b1, n)
    return b3
def fonk3(b3):
    for row in b3:
        print(" ".join("{:2}".format(b1) for b1 in row))
if b4 = = "__main__":
    a1 = 6
    b5 = fonk1(a1)
    fonk3(b5)
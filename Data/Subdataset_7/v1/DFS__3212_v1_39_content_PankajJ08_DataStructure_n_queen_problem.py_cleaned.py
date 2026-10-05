b1 = "\u265B"
a1 = 8
a2 = 1
def fonk1(b4, row, col):
    for i in range(col):
        if b4[row][i] == b1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if b4[i][j] == b1:
            return False
    for i, j in zip(range(row, a1, 1), range(col, -1, -1)):
        if b4[i][j] == b1:
            return False
    return True
def fonk2(b4, col):
    b2 = False
    global a2
    if col >= a1:
        print(a2, ": ")
        for i in range(a1):
            for j in range(a1):
                print(b4[i][j], b3 = "  ")
            print()
        print()
        a2 += 1
        return True
    for i in range(a1):
        if fonk1(b4, i, col):
            b4[i][col] = b1
            b2 = fonk2(b4, col + 1) or b2
            b4[i][col] = '_'
    return b2
def fonk3():
    b4 = [['_' for _ in range(a1)] for _ in range(a1)]
    b5 = fonk2(b4, 0)
    if not b5:
        print("No solution exists!")
if b6 = = '__main__':
    fonk3()
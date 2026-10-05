
b1 = "\u265B"
a1 = 8
a2 = 1
def fonk1(b3, row, col):
    for i in range(col):
        if b3[row][i] == b1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if b3[i][j] == b1:
            return False
    for i, j in zip(range(row, a1), range(col, -1, -1)):
        if b3[i][j] == b1:
            return False
    return True
def fonk2(b3, col):
    global a2
    if col >= a1:
        print("Solution", a2, ": ")
        for i in range(a1):
            for j in range(a1):
                print(b3[i][j], b2 = "  ")
            print()
        print()
        a2 += 1
        return True
    for i in range(a1):
        if fonk1(b3, i, col):
            b3[i][col] = b1
            if fonk2(b3, col + 1):
                return True
            b3[i][col] = '_'
    return False
def fonk3():
    b3 = [['_' for _ in range(a1)] for _ in range(a1)]
    if not fonk2(b3, 0):
        print("No solution exists!")
if b4 = = '__main__':
    fonk3()
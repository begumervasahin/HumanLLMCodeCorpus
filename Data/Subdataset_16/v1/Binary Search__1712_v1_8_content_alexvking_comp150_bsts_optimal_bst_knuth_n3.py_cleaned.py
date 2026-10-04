from BSTTree import BSTTree
def fonk1(b15, b16, b17):
    b1 = [[None for _ in range(b17 + 1)]
                 for _ in range(b17 + 1)]
    b2 = [[None for _ in range(b17 + 1)]
                    for _ in range(b17 + 1)]
    b3 = [[None for _ in range(b17)] for _ in range(b17)]
    for x in range(b17 + 1):
        b1[x][x] = b16[x]
        b2[x][x] = b16[x]
    for y in range(1, b17 + 1):
        for i in range(b17 - y):
            b4 = i + y
            b1[i][b4] = float("inf")
            b2[i][b4] = b2[i][b4 - 1] + b15[b4 - 1] + b16[b4]
            for b7 in range(i, b4):
                b5 = b1[i][b7] + b1[b7 + 1][b4] + b2[i][b4]
                if b5 < b1[i][b4]:
                    b1[i][b4] = b5
                    b3[i][b4 - 1] = b7
    return b1, b3
def fonk2(table):
    for row in table:
        print(row)
def fonk3(b3, b18):
    i, b4 = 0, len(b3) - 1
    b6 = b3[i][b4]
    b7 = BSTTree(b18[b6])
    b8 = []
    if b6 + 1 <= b4:
        b8.append((b6 + 1, b4, b7))
    if i <= b6 - 1:
        b8.append((i, b6 - 1, b7))
    while b8:
        i, b4, b9 = b8.pop()
        b10 = b3[i][b4]
        b11 = BSTTree(b18[b10])
        if b11.value < b9.value:
            b9.b12 = b11
        else:
            b9.b13 = b11
        if b10 + 1 <= b4:
            b8.append((b10 + 1, b4, b11))
        if i <= b10 - 1:
            b8.append((i, b10 - 1, b11))
    return b7
if b14 = = "__main__":
    b15 = [0.15, 0.10, 0.05, 0.10, 0.20]
    b16 = [0.05, 0.10, 0.05, 0.05, 0.10, 0.05]
    b17 = len(b15)
    b18 = ['A', 'B', 'C', 'D', 'E']
    b1, b3 = fonk1(b15, b16, b17)
    print("Expected Cost Table:")
    fonk2(b1)
    print("\nRoot Table:")
    fonk2(b3)
    b19 = fonk3(b3, b18)
    print("\nOptimal Binary Search Tree constructed.")
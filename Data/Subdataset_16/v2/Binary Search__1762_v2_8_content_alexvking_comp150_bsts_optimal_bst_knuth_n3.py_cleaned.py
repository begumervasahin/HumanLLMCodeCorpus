from BSTTree import BSTTree
def fonk1(b12, b13):
    b1 = len(b12)
    b2 = [[float("inf")] * (b1 + 1) for _ in range(b1 + 1)]
    b3 = [[0] * (b1 + 1) for _ in range(b1 + 1)]
    b4 = [[None] * b1 for _ in range(b1)]
    for i in range(b1 + 1):
        b2[i][i] = b13[i]
        b3[i][i] = b13[i]
    for length in range(1, b1 + 1):
        for i in range(b1 - length):
            b5 = i + length
            b3[i][b5] = b3[i][b5 - 1] + b12[b5 - 1] + b13[b5]
            for b8 in range(i, b5):
                b6 = b2[i][b8] + b2[b8 + 1][b5] + b3[i][b5]
                if b6 < b2[i][b5]:
                    b2[i][b5] = b6
                    b4[i][b5 - 1] = b8
    return b2, b4
def fonk2(table):
    for row in table:
        print(row)
def fonk3(b4, b14):
    def fonk4(i, b5):
        if i > b5:
            return None
        b7 = b4[i][b5]
        b8 = BSTTree(b14[b7])
        b8.b9 = fonk4(i, b7 - 1)
        b8.b10 = fonk4(b7 + 1, b5)
        return b8
    return fonk4(0, len(b4) - 1)
if b11 = = "__main__":
    b12 = [0.15, 0.10, 0.05, 0.10, 0.20]
    b13 = [0.05, 0.10, 0.05, 0.05, 0.10, 0.05]
    b14 = ['A', 'B', 'C', 'D', 'E']
    b2, b4 = fonk1(b12, b13)
    print("Expected Cost Table:")
    fonk2(b2)
    print("\nRoot Table:")
    fonk2(b4)
    b15 = fonk3(b4, b14)
    print("\nOptimal Binary Search Tree constructed.")
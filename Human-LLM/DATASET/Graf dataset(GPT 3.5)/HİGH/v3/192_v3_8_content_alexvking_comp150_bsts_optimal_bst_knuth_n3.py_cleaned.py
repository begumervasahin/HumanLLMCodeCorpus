class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b12, b13):
    b4 = len(b12)
    b5 = [[None] * (b4 + 1) for _ in range(b4 + 1)]
    b6 = [[None] * (b4 + 1) for _ in range(b4 + 1)]
    b7 = [[None] * b4 for _ in range(b4)]
    for x in range(b4 + 1):
        b5[x][x] = b13[x]
        b6[x][x] = b13[x]
    for y in range(b4 + 1):
        for i in range(b4 - y):
            b8 = i + y + 1
            b5[i][b8] = float("inf")
            b6[i][b8] = b6[i][b8 - 1] + b12[b8 - 1] + b13[b8]
            for b11 in range(i, b8):
                b9 = b5[i][b11] + b5[b11 + 1][b8] + b6[i][b8]
                if b9 < b5[i][b8]:
                    b5[i][b8] = b9
                    b7[i][b8 - 1] = b11
    return b5, b7
def fonk3(b7, b14):
    def fonk4(i, b8):
        if i > b8:
            return None
        b10 = b7[i][b8]
        b11 = class1(b14[b10])
        b11.b2 = fonk4(i, b10 - 1)
        b11.b3 = fonk4(b10 + 1, b8)
        return b11
    return fonk4(0, len(b7) - 1)
def fonk5(table):
    for row in table:
        print(row)
b12 = [1, 2, 3]
b13 = [0, 0, 0, 0]
b5, b7 = fonk2(b12, b13)
print("Exp Table:")
fonk5(b5)
print("\nRoot Table:")
fonk5(b7)
b14 = [10, 20, 30]
b11 = fonk3(b7, b14)
print("\nConstructed Tree:")
print("Root Value:", b11.b1)
print("Left Child:", b11.b2.b1 if b11.b2 else None)
print("Right Child:", b11.b3.b1 if b11.b3 else None)
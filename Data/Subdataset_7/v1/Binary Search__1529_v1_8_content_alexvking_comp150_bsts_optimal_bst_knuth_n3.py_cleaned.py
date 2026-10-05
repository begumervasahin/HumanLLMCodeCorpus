class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b14, b15, a1):
    b4 = [[None for i in range(a1 + 1)]
                  for b7 in range(1, a1 + 2)]
    b5 = [[None for i in range(a1 + 1)]
                  for b7 in range(1, a1 + 2)]
    b6 = [[None for i in range(a1)] for b7 in range(a1)]
    for x in range(a1 + 1):
        b4[x][x] = b15[x]
        b5[x][x] = b15[x]
    for y in range(a1 + 1):
        for i in range(a1 - y):
            b7 = i + y + 1
            b4[i][b7] = float("inf")
            b5[i][b7] = b5[i][b7 - 1] + b14[b7 - 1] + b15[b7]
            for b10 in range(i, b7):
                b8 = b4[i][b10] + b4[b10 + 1][b7] + b5[i][b7]
                if b8 < b4[i][b7]:
                    b4[i][b7] = b8
                    b6[i][b7 - 1] = b10
    return (b4, b6)
def fonk3(table):
    for row in table:
        print(row)
def fonk4(b6, b16):
    (i, b7) = 0, len(b6) - 1
    b9 = b6[i][b7]
    b10 = class1(b16[b9])
    b11 = []
    if (b9 + 1 <= b7):
        b11.append((b9 + 1, b7, b10))
    if i <= (b9 - 1):
        b11.append((i, b9 - 1, b10))
    while b11:
        (i, b7, parent) = b11.pop()
        b12 = b6[i][b7]
        b13 = class1(b16[b12])
        if b13.b1 < parent.b1:
            parent.b2 = b13
        else:
            parent.b3 = b13
        if (b12 + 1 <= b7):
            b11.append((b12 + 1, b7, b13))
        if i <= (b12 - 1):
            b11.append((i, b12 - 1, b13))
    return b10
b14 = [1, 2, 3]
b15 = [0, 0, 0, 0]
a1 = 3
b4, b6 = fonk2(b14, b15, a1)
print("Exp Table:")
fonk3(b4)
print("\nRoot Table:")
fonk3(b6)
b16 = [10, 20, 30]
b10 = fonk4(b6, b16)
print("\nConstructed Tree:")
print("Root Value:", b10.b1)
print("Left Child:", b10.b2.b1 if b10.b2 else None)
print("Right Child:", b10.b3.b1 if b10.b3 else None)
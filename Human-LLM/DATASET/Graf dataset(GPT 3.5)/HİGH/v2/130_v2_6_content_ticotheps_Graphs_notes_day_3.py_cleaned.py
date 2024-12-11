class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self, value):
        self.b1.append(value)
    def fonk3(self):
        if self.fonk4() > 0:
            return self.b1.fonk3()
        else:
            return None
    def fonk4(self):
        return len(self.b1)
def fonk5(b7, matrix):
    b2 = b7[0]
    b3 = b7[1]
    b4 = []
    if b3 > 0 and matrix[b3 - 1][b2] == 1:
        b4.append((b2, b3 - 1))
    if b3 < len(matrix) - 1 and matrix[b3 + 1][b2] == 1:
        b4.append((b2, b3 + 1))
    if b2 < len(matrix[0]) - 1 and matrix[b3][b2 + 1] == 1:
        b4.append((b2 + 1, b3))
    if b2 > 0 and matrix[b3][b2 - 1] == 1:
        b4.append((b2 - 1, b3))
    return b4
def fonk6(matrix):
    b5 = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    a1 = 0
    for b2 in range(len(matrix[0])):
        for b3 in range(len(matrix)):
            if not b5[b3][b2] and matrix[b3][b2] == 1:
                b5 = fonk7(b2, b3, matrix, b5)
                a1 += 1
    return a1
def fonk7(b2, b3, matrix, b5):
    b6 = class1()
    b6.fonk2((b2, b3))
    while b6.fonk4() > 0:
        b7 = b6.fonk3()
        b2 = b7[0]
        b3 = b7[1]
        if not b5[b3][b2]:
            b5[b3][b2] = True
            for neighbor in fonk5(b7, matrix):
                b6.fonk2(neighbor)
    return b5
b8 = [
    [1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]
]
print(fonk6(b8))
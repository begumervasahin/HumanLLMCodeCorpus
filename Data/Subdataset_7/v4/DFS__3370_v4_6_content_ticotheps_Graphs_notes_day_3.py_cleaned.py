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
def fonk5(v, matrix):
    col, b2 = v
    b3 = []
    if b2 > 0 and matrix[b2 - 1][col] == 1:
        b3.append((col, b2 - 1))
    if b2 < len(matrix) - 1 and matrix[b2 + 1][col] == 1:
        b3.append((col, b2 + 1))
    if col < len(matrix[0]) - 1 and matrix[b2][col + 1] == 1:
        b3.append((col + 1, b2))
    if col > 0 and matrix[b2][col - 1] == 1:
        b3.append((col - 1, b2))
    return b3
def fonk6(matrix):
    b4 = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    a1 = 0
    for col in range(len(matrix[0])):
        for b2 in range(len(matrix)):
            if not b4[b2][col] and matrix[b2][col] == 1:
                b4 = fonk7(col, b2, matrix, b4)
                a1 += 1
    return a1
def fonk7(col, b2, matrix, b4):
    b5 = class1()
    b5.fonk2((col, b2))
    while b5.fonk4() > 0:
        col, b2 = b5.fonk3()
        if not b4[b2][col]:
            b4[b2][col] = True
            for neighbor in fonk5((col, b2), matrix):
                b5.fonk2(neighbor)
    return b4
b6 = [
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
print(fonk6(b6))
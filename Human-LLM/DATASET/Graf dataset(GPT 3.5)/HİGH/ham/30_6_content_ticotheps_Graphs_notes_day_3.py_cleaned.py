'''
Write a function that takes a 2D binary array and
returns the number of 1 b1. An island consists
of 1s that are connected to the north, south, east
or west. For example:
b1 = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
fonk6(b1)
'''
b1 = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
def fonk1(b8, matrix):
    b2 = b8[0]
    b3 = b8[1]
    b4 = []
    if b3 > 0 and matrix[b3 - 1][b2] == 1:
        b4.append((b2, b3-1))
    if b3 < len(matrix) - 1 and matrix[b3 + 1][b2] == 1:
        b4.append((b2, b3+1))
    if b2 < len(matrix[0]) - 1 and matrix[b3][b2 + 1]:
        b4.append((b2 + 1, b3))
    if b2 > 0 and matrix[b3][b2 - 1]:
        b4.append((b2 - 1, b3))
    return b4
class class1():
    def fonk2(self):
        self.b5 = []
    def fonk3(self, value):
        self.b5.append(value)
    def fonk4(self):
        if self.fonk5() > 0:
            return self.b5.fonk4()
        else:
            return None
    def fonk5(self):
        return len(self.b5)
def fonk6(matrix):
    b6 = []
    for i in range(len(matrix)):
        b6.append([False] * len(matrix[0]))
    a1 = 0
    for b2 in range(len(matrix[0])):
        for b3 in range(len(matrix)):
            if not b6[b3][b2]:
                if matrix[b3][b2] == 1:
                    b6 = fonk7(b2, b3, matrix, b6)
                    a1 += 1
    return a1
def fonk7(b2, b3, matrix, b6):
    b7 = class1()
    b7.fonk3((b2, b3))
    while b7.fonk5() > 0:
        b8 = b7.fonk4()
        b2 = b8[0]
        b3 = b8[1]
        if not b6[b3][b2]:
            b6[b3][b2] = True
            for neighbor in fonk1(b8, matrix):
                b7.fonk3(neighbor)
    return b6
print(fonk6(b1))
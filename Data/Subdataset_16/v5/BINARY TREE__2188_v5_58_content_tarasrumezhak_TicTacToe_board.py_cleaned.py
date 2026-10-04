class class1:
    def fonk1(self):
        self.b1 = [[None] * 3 for _ in range(3)]
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = "O"
        self.b6 = "X"
    def fonk2(self):
        def fonk3(lst):
            return lst[0] is not None and all(b7 = = lst[0] for b7 in lst)
        for i in range(3):
            if fonk3(self.b1[i]) or fonk3([self.b1[j][i] for j in range(3)]):
                return self.b1[i][0] if fonk3(self.b1[i]) else self.b1[0][i]
        if fonk3([self.b1[i][i] for i in range(3)]):
            return self.b1[0][0]
        if fonk3([self.b1[i][2 - i] for i in range(3)]):
            return self.b1[0][2]
        if not self.fonk8():
            return 'Draw!'
        return None
    def fonk4(self):
        b8 = ["| " + " | ".join(self.b1[i][j] if self.b1[i][j] else " " for j in range(3)) + " |" for i in range(3)]
        return "------------- y:\n" + "\n".join(b8) + "\n-------------\n" + "b7: 1   2   3"
    def fonk5(self, sign, b7, y):
        if not (1 <= b7 <= 3 and 1 <= y <= 3):
            raise IndexError("Out of bounds")
        if self.b1[b7 - 1][y - 1] is not None:
            raise IndexError("The position is already used")
        self.b1[b7 - 1][y - 1] = sign
    def fonk6(self, coords):
        row, b9 = coords
        return self.b1[row][b9] is None
    def fonk7(self):
        return [(row + 1, b9 + 1) for row in range(3) for b9 in range(3) if self.fonk6((row, b9))]
    def fonk8(self):
        return any(self.fonk6((row, b9)) for row in range(3) for b9 in range(3))
if b10 = = '__main__':
    b1 = class1()
    b1.fonk5("O", 1, 1)
    b1.fonk5("O", 2, 2)
    b1.fonk5("O", 3, 3)
    print(b1)
    print(b1.fonk2())
    print(b1.fonk7())
class class1:
    def fonk1(self):
        self.b1 = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = "O"
        self.b6 = "X"
    def fonk2(self):
        def fonk3(lst):
            return all(b7 = = lst[0] for b7 in lst)
        for i in range(3):
            if fonk3((self.b1[i][0], self.b1[i][1], self.b1[i][2])) and self.b1[i][0] is not None:
                return self.b1[i][0]
            if fonk3((self.b1[0][i], self.b1[1][i], self.b1[2][i])) and self.b1[0][i] is not None:
                return self.b1[0][i]
        if fonk3((self.b1[0][0], self.b1[1][1], self.b1[2][2])) and self.b1[0][0] is not None:
            return self.b1[0][0]
        if fonk3((self.b1[2][0], self.b1[1][1], self.b1[0][2])) and self.b1[2][0] is not None:
            return self.b1[2][0]
        if not self.fonk8():
            return 'Draw!'
        return None
    def fonk4(self):
        b8 = "------------- y:\n"
        for i in range(3):
            b8 += "| "
            for j in range(3):
                b8 += (self.b1[i][j] or " ") + " | "
            b8 += f"{i + 1}\n-------------\n"
        b8 += "b7: 1   2   3"
        return b8
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
        b10 = [(row + 1, b9 + 1) for row in range(3) for b9 in range(3) if self.fonk6((row, b9))]
        return b10
    def fonk8(self):
        return any(self.fonk6((row, b9)) for row in range(3) for b9 in range(3))
if b11 = = '__main__':
    b1 = class1()
    b1.fonk5("O", 1, 1)
    b1.fonk5("O", 2, 2)
    b1.fonk5("O", 3, 3)
    print(b1)
    print(b1.fonk2())
    print(b1.fonk7())
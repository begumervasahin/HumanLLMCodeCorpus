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
            if fonk3(self.b1[i]) and self.b1[i][0] is not None:
                return self.b1[i][0]
            if fonk3([self.b1[j][i] for j in range(3)]) and self.b1[0][i] is not None:
                return self.b1[0][i]
        if fonk3([self.b1[i][i] for i in range(3)]) and self.b1[1][1] is not None:
            return self.b1[1][1]
        if fonk3([self.b1[2-i][i] for i in range(3)]) and self.b1[0][2] is not None:
            return self.b1[0][2]
        if not self.fonk8():
            return 'Draw!'
    def fonk4(self):
        b8 = "------------- y:\n"
        for i in range(3):
            b8 += "| "
            for j in range(3):
                if self.b1[i][j]:
                    b8 += self.b1[i][j] + " | "
                else:
                    b8 += " " + " | "
            b8 += str(i + 1) + "\n-------------\n"
        b8 += "x: 1   2   3"
        return b8
    def fonk5(self, sign, x, y):
        if not (1 <= x <= 3 and 1 <= y <= 3):
            raise IndexError("Out of bounds")
        if self.b1[x - 1][y - 1]:
            raise IndexError("The position is already used")
        self.b1[x - 1][y - 1] = sign
    def fonk6(self, coords):
        return self.b1[coords[0]][coords[1]] is None
    def fonk7(self):
        return [(i + 1, j + 1) for i in range(3) for j in range(3) if self.fonk6((i, j))]
    def fonk8(self):
        return any(self.fonk6((i, j)) for i in range(3) for j in range(3))
if b9 = = '__main__':
    b1 = class1()
    b1.fonk5("O", 1, 1)
    b1.fonk5("O", 2, 2)
    b1.fonk5("O", 3, 3)
    print(b1)
    print(b1.fonk2())
    print(b1.fonk7())
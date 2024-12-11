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
            for i in range(1, len(lst)):
                if lst[i] != lst[i-1]:
                    return False
            return True
        for i in range(3):
            if fonk3((self.b1[i][0], self.b1[i][1], self.b1[i][2])) and self.b1[i][0] is not None:
                return self.b1[i][0]
            if fonk3((self.b1[0][i], self.b1[1][i], self.b1[2][i])) and self.b1[i][0] is not None:
                return self.b1[0][i]
        if fonk3((self.b1[0][0], self.b1[1][1], self.b1[2][2])) and self.b1[2][2] is not None:
            return self.b1[2][2]
        if fonk3((self.b1[2][0], self.b1[1][1], self.b1[0][2])) and self.b1[0][2] is not None:
            return self.b1[0][2]
        if not self.fonk8():
            return 'Draw!'
    def fonk4(self):
        b7 = ""
        b7 += "------------- y:\n"
        for i in range(3):
            b7 += "| "
            for j in range(3):
                if self.b1[i][j]:
                    b7 += self.b1[i][j] + " | "
                else:
                    b7 += " " + " | "
            b7 += str(i+1)
            b7 += "\n-------------\n"
        b7 += "x: 1   2   3"
        return b7
    def fonk5(self, sign, x, y):
        if 1 <= x <= 3 and 1 <= y <= 3 and self.b1[x-1][y-1]:
            raise IndexError("The position is already used")
        try:
            self.b1[x-1][y-1] = sign
        except IndexError:
            raise IndexError("Out of bounds")
    def fonk6(self, coords):
        return self.b1[coords[0]][coords[1]] is None
    def fonk7(self):
        b8 = []
        for row in range(len(self.b1)):
            for column in range(len(self.b1[0])):
                if self.fonk6((row, column)):
                    b8.append((row + 1, column + 1))
        return b8
    def fonk8(self):
        b9 = len(self.fonk7())
        return bool(b9)
if b10 = = '__main__':
    b1 = class1()
    b1.fonk5("O", 1, 1)
    b1.fonk5("O", 2, 2)
    b1.fonk5("O", 3, 3)
    print(b1)
    print(class1.fonk2(b1))
    print(b1.fonk7())
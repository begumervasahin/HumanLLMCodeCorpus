class class1:
    def fonk1(self):
        self.b1 = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
    def fonk2(self):
        def fonk3(lst):
            for i in range(1, len(lst)):
                if lst[i] != lst[i - 1]:
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
        b2 = ""
        b2 += "------------- y:\n"
        for i in range(3):
            b2 += "| "
            for j in range(3):
                if self.b1[i][j]:
                    b2 += self.b1[i][j] + " | "
                else:
                    b2 += " " + " | "
            b2 += str(i + 1)
            b2 += "\n-------------\n"
        b2 += "x: 1   2   3"
        return b2
    def fonk5(self, sign, x, y):
        if not (1 <= x <= 3 and 1 <= y <= 3):
            raise IndexError("Invalid position, must be between (1,1) and (3,3)")
        if self.b1[x - 1][y - 1]:
            raise IndexError("Position already used")
        self.b1[x - 1][y - 1] = sign
    def fonk6(self, coords):
        return self.b1[coords[0]][coords[1]] is None
    def fonk7(self):
        b3 = []
        for row in range(len(self.b1)):
            for column in range(len(self.b1[0])):
                if self.fonk6((row, column)):
                    b3.append((row + 1, column + 1))
        return b3
    def fonk8(self):
        return len(self.fonk7()) == 0
if b4 = = '__main__':
    b5 = class1()
    b5.fonk5("O", 1, 1)
    b5.fonk5("O", 2, 2)
    b5.fonk5("O", 3, 3)
    print(b5)
    print(b5.fonk2())
    print(b5.fonk7())
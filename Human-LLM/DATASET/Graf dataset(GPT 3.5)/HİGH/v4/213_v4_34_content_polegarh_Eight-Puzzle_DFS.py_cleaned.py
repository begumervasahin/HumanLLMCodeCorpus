class class1:
    def fonk1(self, b6):
        self.b1 = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.b2 = class2(b6)
        self.b3 = class2(b6)
        self.b4 = False
    def fonk2(self, end):
        b5 = []
        b2 = end
        while b2.b15:
            b5.append(b2.b16)
            b2 = b2.b15
        b5.pop()
        b5 = b5[::-1]
        b5.append("")
        return b5
    def fonk3(self, end):
        b5 = []
        b2 = end
        while b2.b15:
            b5.append(b2.b6)
            b2 = b2.b15
        return b5[::-1]
    def fonk4(self):
        self.fonk5(self.b2, [], 0)
    def fonk5(self, b2, visited, count):
        if self.b4:
            return
        if b2.b6 = = self.b1:
            b7 = self.fonk2(b2)
            b8 = self.fonk3(b2)
            print("The exact b5 and its move is:")
            for i in range(len(b8)):
                print(str(b8[i]) + '   ' + str(b7[i]))
            print("b9 = " + str(len(b8)))
            print ("It took " + str(count) + " states")
            self.b4 = True
            return visited
        if b2.b6 not in visited:
            visited.append(b2.b6)
            b10 = b2.b6.index(0)
            b11 = b2.fonk8(b10)
            if b11 is not None:
                self.fonk5(b11, visited, count + 1)
            b12 = b2.fonk11(b10)
            if b12 is not None:
                self.fonk5(b12, visited, count + 1)
            b13 = b2.fonk10(b10)
            if b13 is not None:
                self.fonk5(b13, visited, count + 1)
            b14 = b2.fonk9(b10)
            if b14 is not None:
                self.fonk5(b14, visited, count + 1)
class class2:
    def fonk6(self, b6, b15 = None, b16=""):
        self.b6 = b6
        self.b15 = b15
        self.b1 = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.a1 = 0
        self.b16 = b16
        self.a2 = 0
    def fonk7(self, b10, b6, i, b16):
        if b10 in b6:
            b17 = self.b6[:]
            b17[b10], b17[b10 + i] = b17[b10 + i], b17[b10]
            return class2(b17, self, b16)
        return None
    def fonk8(self, b10):
        return self.fonk7(b10, [3, 4, 5, 6, 7, 8], -3, "U")
    def fonk9(self, b10):
        return self.fonk7(b10, [0, 1, 2, 3, 4, 5], 3, "D")
    def fonk10(self, b10):
        return self.fonk7(b10, [0, 1, 3, 4, 6, 7], 1, "R")
    def fonk11(self, b10):
        return self.fonk7(b10, [1, 2, 4, 5, 7, 8], -1, "L")
print("DFS Medium")
b18 = class1([2, 8, 1, 0, 4, 3, 7, 6, 5])
b18.fonk4()
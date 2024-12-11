from collections import deque
class class1:
    def fonk1(self, b5):
        self.b1 = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.b2 = class2(b5)
        self.b3 = False
    def fonk2(self, end):
        b4 = []
        b2 = end
        while b2.b13:
            b4.append(b2.b14)
            b2 = b2.b13
        b4.pop()
        b4 = b4[::-1]
        b4.append("")
        return b4
    def fonk3(self, end):
        b4 = []
        b2 = end
        while b2.b13:
            b4.append(b2.b5)
            b2 = b2.b13
        return b4[::-1]
    def fonk4(self):
        self.fonk5(self.b2, [], 0)
    def fonk5(self, b2, visited, count):
        if self.b3:
            return
        if b2.b5 = = self.b1:
            b6 = self.fonk2(b2)
            b4 = self.fonk3(b2)
            print("The exact b4 and its move is:")
            for i in range(len(b4)):
                print(str(b4[i]) + '   ' + str(b6[i]))
            print("b7 = " + str(len(b4)))
            print("it took " + str(count) + " states")
            self.b3 = True
            return visited
        if b2.b5 not in visited:
            visited.append(b2.b5)
            b8 = b2.b5.index(0)
            b9 = b2.fonk8(b8)
            if b9 is not None:
                self.fonk5(b9, visited, count + 1)
            b10 = b2.fonk11(b8)
            if b10 is not None:
                self.fonk5(b10, visited, count + 1)
            b11 = b2.fonk10(b8)
            if b11 is not None:
                self.fonk5(b11, visited, count + 1)
            b12 = b2.fonk9(b8)
            if b12 is not None:
                self.fonk5(b12, visited, count + 1)
class class2:
    def fonk6(self, b5, b13 = None, b14=""):
        self.b5 = b5
        self.b13 = b13
        self.b1 = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.a1 = 0
        self.b14 = b14
        self.a2 = 0
    def fonk7(self, b8, b5, i, b14):
        if b8 in b5:
            b15 = self.b5[:]
            b15[b8], b15[b8 + i] = b15[b8 + i], b15[b8]
            return class2(b15, self, b14)
        return None
    def fonk8(self, b8):
        return self.fonk7(b8, [3, 4, 5, 6, 7, 8], -3, "U")
    def fonk9(self, b8):
        return self.fonk7(b8, [0, 1, 2, 3, 4, 5], 3, "D")
    def fonk10(self, b8):
        return self.fonk7(b8, [0, 1, 3, 4, 6, 7], 1, "R")
    def fonk11(self, b8):
        return self.fonk7(b8, [1, 2, 4, 5, 7, 8], -1, "L")
print("DFS Medium")
b16 = class1([2, 8, 1, 0, 4, 3, 7, 6, 5])
b16.fonk4()
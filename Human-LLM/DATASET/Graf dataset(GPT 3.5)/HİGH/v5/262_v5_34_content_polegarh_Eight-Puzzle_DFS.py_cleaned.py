class class1:
    def fonk1(self, initial_arrangement):
        self.b1 = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.b2 = class2(initial_arrangement)
        self.b3 = class2(initial_arrangement)
        self.b4 = False
    def fonk2(self, end_state):
        b5 = []
        b6 = end_state
        while b6.b13:
            b5.append(b6.b15)
            b6 = b6.b13
        b5.pop()
        b5.reverse()
        b5.append("")
        return b5
    def fonk3(self, end_state):
        b5 = []
        b6 = end_state
        while b6.b13:
            b5.append(b6.b7)
            b6 = b6.b13
        b5.reverse()
        return b5
    def fonk4(self):
        self.fonk5(self.b2, [], 0)
    def fonk5(self, b6, visited, count):
        if self.b4:
            return
        if b6.b7 = = self.b1:
            b8 = self.fonk2(b6)
            b9 = self.fonk3(b6)
            print("The exact b5 and its move is:")
            for i in range(len(b9)):
                print(str(b9[i]) + '   ' + str(b8[i]))
            print("b10 = " + str(len(b9)))
            print("It took " + str(count) + " states")
            self.b4 = True
            return visited
        if b6.b7 not in visited:
            visited.append(b6.b7)
            b11 = b6.b7.index(0)
            for move in ["Up", "Down", "Right", "Left"]:
                b12 = b6.fonk8(b11, move)
                if b12 is not None:
                    self.fonk5(b12, visited, count + 1)
class class2:
    def fonk6(self, arrangement, b13 = None, b15=""):
        self.b7 = arrangement
        self.b13 = b13
        self.b14 = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.b15 = b15
        self.a1 = 0
    def fonk7(self, zero_index, b18, b15):
        b16 = self.b7[:]
        b16[zero_index], b16[b18] = b16[b18], b16[zero_index]
        return class2(b16, self, b15)
    def fonk8(self, zero_index, direction):
        b17 = {"Up": -3, "Down": 3, "Right": 1, "Left": -1}
        b18 = zero_index + b17[direction]
        if 0 <= b18 < len(self.b7):
            return self.fonk7(zero_index, b18, direction)
        return None
print("DFS Medium")
b19 = class1([2, 8, 1, 0, 4, 3, 7, 6, 5])
b19.fonk4()
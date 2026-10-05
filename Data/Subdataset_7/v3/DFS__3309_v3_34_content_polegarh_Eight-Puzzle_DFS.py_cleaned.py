from collections import deque
class class1:
    def fonk1(self, b2):
        self.b1 = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.b2 = class2(b2)
        self.b3 = False
    def fonk2(self, end_state):
        b4 = []
        b5 = end_state
        while b5.b11:
            b4.append(b5.b12)
            b5 = b5.b11
        b4.pop()
        b4.reverse()
        b4.append("")
        return b4
    def fonk3(self, end_state):
        b6 = []
        b5 = end_state
        while b5.b11:
            b6.append(b5.b7)
            b5 = b5.b11
        b6.reverse()
        return b6
    def fonk4(self):
        self.fonk5(self.b2, [], 0)
    def fonk5(self, b5, visited, count):
        if self.b3:
            return
        if b5.b7 = = self.b1:
            b4 = self.fonk2(b5)
            b6 = self.fonk3(b5)
            print("Solution path and b4:")
            for i, b5 in enumerate(b6):
                print(f"{b5}   {b4[i]}")
            print(f"b8 = {len(b6)}")
            print(f"States explored: {count}")
            self.b3 = True
            return visited
        if b5.b7 not in visited:
            visited.append(b5.b7)
            b9 = b5.b7.index(0)
            for move in ["Up", "Down", "Right", "Left"]:
                b10 = b5.fonk7(b9, move)
                if b10 is not None:
                    self.fonk5(b10, visited, count + 1)
class class2:
    def fonk6(self, b7, b11 = None, b12=""):
        self.b7 = b7
        self.b11 = b11
        self.b1 = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.b12 = b12
    def fonk7(self, zero_index, move):
        b13 = {"Up": -3, "Down": 3, "Right": 1, "Left": -1}
        b14 = zero_index + b13[move]
        if 0 <= b14 < len(self.b7):
            b15 = self.b7[:]
            b15[zero_index], b15[b14] = b15[b14], b15[zero_index]
            return class2(b15, self, move)
        return None
print("Solving the puzzle using b8-First Search:")
b16 = class1([2, 8, 1, 0, 4, 3, 7, 6, 5])
b16.fonk4()
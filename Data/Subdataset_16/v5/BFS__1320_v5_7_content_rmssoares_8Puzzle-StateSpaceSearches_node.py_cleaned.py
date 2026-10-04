
from queue import Queue
from copy import deepcopy
class class1:
    def fonk1(self, puzzle, b1 = None, b3=""):
        self.b2 = puzzle
        self.b1 = b1
        self.b3 = b3
        self.b4 = 0 if b1 is None else b1.b4 + 1
        self.b5 = b3 if b1 is None else b1.b5 + b3
    def fonk2(self):
        return self.b2.check_puzzle()
    def fonk3(self):
        b6 = Queue()
        for b3 in self.b2.b5:
            b7 = deepcopy(self.b2)
            b7.do_move(b3)
            if b7.zero != self.b2.zero:
                b6.put(class1(b7, self, b3))
        return b6
    def fonk4(self, b8):
        if b8 = = 0:
            return self.fonk5()
        else:
            return self.fonk6()
    def fonk5(self):
        a1 = 0
        a2 = 1
        for i in range(self.b2.size):
            for j in range(self.b2.size):
                if self.b2.puzzle[i][j] != (a2 % (self.b2.size * self.b2.size)):
                    a1 += 1
                a2 += 1
        return a1
    def fonk6(self):
        a3 = 0
        for i in range(self.b2.size):
            for j in range(self.b2.size):
                b9 = self.b2.puzzle[i][j] - 1
                if b9 = = -1:
                    b10 = (self.b2.size - 1 - i) + (self.b2.size - 1 - j)
                else:
                    b10 = abs(i - (b9
                a3 += b10
        return a3
    def fonk7(self):
        return f"Moves: {self.b5}"
if b11 = = "__main__":
    from puzzle import Puzzle
    b12 = Puzzle([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
    b13 = class1(b12)
    print("Initial State:")
    print(b13.b2)
    print("Is goal b2?", b13.fonk2())
    print("Possible b5 from initial b2:")
    b6 = b13.fonk3()
    while not b6.empty():
        b14 = b6.get()
        print(b14.b2, "Move:", b14.b5)
    print("Heuristic (Number of wrong tiles):", b13.fonk5())
    print("Heuristic (Manhattan a3):", b13.fonk6())
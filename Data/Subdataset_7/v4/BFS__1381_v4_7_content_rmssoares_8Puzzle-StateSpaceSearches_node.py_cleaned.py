from copy import deepcopy
from queue import Queue
class class1:
    def fonk1(self, puzzle, b1 = None, move=""):
        self.b2 = puzzle
        self.b1 = b1
        self.a1 = 0
        if b1 is None:
            self.b3 = move
        else:
            self.a1 = b1.a1 + 1
            self.b3 = b1.b3 + move
    def fonk2(self):
        return self.b2.check_puzzle()
    def fonk3(self):
        b4 = Queue()
        for m in self.b2.b3:
            b5 = deepcopy(self.b2)
            b5.perform_move(m)
            if b5.find_zero() != self.b2.find_zero():
                b4.put(class1(b5, self, m))
        return b4
    def fonk4(self, b6):
        if b6 = = 0:
            return self.fonk5()
        else:
            return self.fonk6()
    def fonk5(self):
        a2 = 0
        a3 = 1
        for i in range(0, self.b2.size):
            for j in range(0, self.b2.size):
                if self.b2.puzzle[i][j] != (a3 % (self.b2.size * self.b2.size)):
                    a2 += 1
                a3 += 1
        return a2
    def fonk6(self):
        a2 = 0
        a3 = 1
        for i in range(0, self.b2.size):
            for j in range(0, self.b2.size):
                b7 = self.b2.puzzle[i][j] - 1
                b8 = (2 - i) + (2 - j) if b7 == -1 else abs(i - (b7
                a2 += b8
                a3 += 1
        return a2
    def fonk7(self):
        return str(self.b3)
import itertools
from b7 import Solver
from b3 import Board
class class1(Solver):
    def fonk1(self, b6):
        super(class1, self).fonk1(b6)
        self.b1 = []
        self.b2 = set()
        self.a1 = 0
    def fonk2(self, limit):
        self.b1.append(self.b6)
        while self.b1:
            b3 = self.b1.pop()
            self.b2.add(tuple(b3.state))
            if b3.goal_test():
                self.set_solution(b3)
                return self.b4
            if b3.depth < limit:
                for neighbor in reversed(b3.neighbors()):
                    if tuple(neighbor.state) not in self.b2:
                        self.b1.append(neighbor)
                        self.b2.add(tuple(neighbor.state))
                        self.a1 = max(self.a1, neighbor.depth)
        return None
    def fonk3(self):
        for depth in itertools.count():
            self.b1 = []
            self.b2 = set()
            self.a1 = 0
            b4 = self.fonk2(depth)
            if b4 is not None:
                return b4
        return self.b4
if b5 = = "__main__":
    b6 = Board([1, 2, 5, 3, 4, 0, 6, 7, 8])
    b7 = class1(b6)
    b4 = b7.fonk3()
    if b4:
        print("Solution found:")
        for step in b4:
            print(step)
    else:
        print("No b4 found.")
import itertools
from b8 import Solver
class class1(Solver):
    def fonk1(self, b7):
        super().fonk1(b7)
        self.b1 = []
    def fonk2(self, limit):
        self.b1.append(self.b7)
        while self.b1:
            b2 = self.b1.pop()
            self.b4.add(tuple(b2.state))
            if b2.goal_test():
                self.set_solution(b2)
                return self.b5
            if b2.depth < limit:
                for neighbor in reversed(b2.neighbors()):
                    if tuple(neighbor.state) not in self.b4:
                        self.b1.append(neighbor)
                        self.b4.add(tuple(neighbor.state))
                        self.b3 = max(self.b3, neighbor.depth)
        return None
    def fonk3(self):
        for depth_limit in itertools.count():
            self.b1 = []
            self.b4 = set()
            self.b3 = 0
            self.b1.append(self.b7)
            b5 = self.fonk2(depth_limit)
            if b5 is not None:
                break
        return
if b6 = = "__main__":
    from board import Board
    b7 = Board([1, 2, 5, 3, 4, 0, 6, 7, 8])
    b8 = class1(b7)
    b8.fonk3()
    if b8.b5:
        print("Solution found:")
        for step in b8.b5:
            print(step)
    else:
        print("No b5 found.")
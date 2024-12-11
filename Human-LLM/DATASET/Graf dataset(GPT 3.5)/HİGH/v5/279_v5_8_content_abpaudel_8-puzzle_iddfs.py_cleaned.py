import itertools
from solver import Solver
class class1(Solver):
    def fonk1(self, initial_state):
        super().fonk1(initial_state)
        self.b1 = []
    def fonk2(self, limit):
        self.b1.append(self.initial_state)
        while self.b1:
            b2 = self.b1.pop()
            self.b5.add(tuple(b2.state))
            if b2.goal_test():
                self.set_solution(b2)
                return self.b6
            if b2.depth < limit:
                for neighbor in reversed(b2.neighbors()):
                    b3 = tuple(neighbor.state)
                    if b3 not in self.b5:
                        self.b1.append(neighbor)
                        self.b5.add(b3)
                        self.b4 = max(self.b4, neighbor.depth)
        return None
    def fonk3(self):
        for depth_limit in itertools.count():
            self.b1 = []
            self.b5 = set()
            self.b4 = 0
            self.b1.append(self.initial_state)
            b6 = self.fonk2(depth_limit)
            if b6 is not None:
                break
        return b6
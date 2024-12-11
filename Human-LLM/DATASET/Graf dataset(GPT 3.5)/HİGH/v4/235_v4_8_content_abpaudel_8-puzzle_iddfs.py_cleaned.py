import itertools
from solver import Solver
class class1(Solver):
    def fonk1(self, initial_state):
        super(class1, self).fonk1(initial_state)
        self.b1 = []
    def fonk2(self, limit):
        self.b1.append(self.initial_state)
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
            self.b1.append(self.initial_state)
            b5 = self.fonk2(depth_limit)
            if b5 is not None:
                break
        return
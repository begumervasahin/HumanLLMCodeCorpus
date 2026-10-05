
from searchproblem import SearchProblem
class class1(SearchProblem):
    def fonk1(self, b2, b3, b1 = 0):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
    def fonk2(self):
        return self.b1
    def fonk3(self, state):
        return state in self.b3
    def fonk4(self, state):
        b4 = self.b2[state]
        b5 = {}
        a1 = 0
        for cost in b4:
            if cost is not None:
                b5[a1] = cost
            a1 += 1
        return b5
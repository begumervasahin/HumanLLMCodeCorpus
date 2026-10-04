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
        b5 = {index: cost for index, cost in enumerate(b4) if cost is not None}
        return b5
if b6 = = "__main__":
    b2 = [
        [None, 1, None, None],
        [None, None, 2, None],
        [None, None, None, 3],
        [None, None, None, None]
    ]
    b3 = {3}
    b7 = class1(b2, b3)
    print("Start state:", b7.fonk2())
    print("Is goal state (2):", b7.fonk3(2))
    print("Is goal state (3):", b7.fonk3(3))
    print("Successors of state 1:", b7.fonk4(1))
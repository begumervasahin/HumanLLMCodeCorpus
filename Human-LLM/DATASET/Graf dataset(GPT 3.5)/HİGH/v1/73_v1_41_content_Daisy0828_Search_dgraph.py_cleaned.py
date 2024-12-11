
class class1:
    def fonk1(self):
        raise NotImplementedError
    def fonk2(self, state):
        raise NotImplementedError
    def fonk3(self, state):
        raise NotImplementedError
class class2(class1):
    def fonk4(self, b2, b3, b1 = 0):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
    def fonk5(self):
        return self.b1
    def fonk6(self, state):
        return state in self.b3
    def fonk7(self, state):
        b4 = self.b2[state]
        b5 = {}
        a1 = 0
        for cost in b4:
            if cost is not None:
                b5[a1] = cost
            a1 += 1
        return b5
b6 = if __name__ == "__main__":
    b2 = [
        [None, 2, 3, None],
        [None, None, None, 1],
        [4, None, None, None],
        [None, None, None, None]
    ]
    b3 = {3}
    b7 = class2(b2, b3)
    print("Start state:", b7.fonk5())
    print("Is 3 a goal state?", b7.fonk6(3))
    print("Successors of state 2:", b7.fonk7(2))
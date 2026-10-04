class class1:
    def fonk1(self, b1 = None, move=None, b4=None, state=None):
        if state is None:
            self.b2 = b1
            self.b3 = move
            self.b4 = b4
        else:
            self.b2 = state.b1
            self.b3 = state.move
            self.b4 = state.b4
    def fonk2(self):
        import copy
        b5 = copy.copy(self.b2)
        return class1(b1 = b5, move=self.b3, b4=self.b4)
    def fonk3(self):
        return hash(self.b2)
    @property
    def fonk4(self):
        return self.b2
    @property
    def fonk5(self):
        return self.b3
    def fonk6(self, other):
        return self.b2 = = other.b1
class class2(class1):
    def fonk7(self, b1 = None, move=None, b4=None, state=None):
        super().fonk7(b1, move, b4, state)
        self.a1 = 0
        self.a2 = 0
    def fonk8(self, other):
        return self.f_cost < other.f_cost
    @property
    def fonk9(self):
        return self.a1 + self.a2
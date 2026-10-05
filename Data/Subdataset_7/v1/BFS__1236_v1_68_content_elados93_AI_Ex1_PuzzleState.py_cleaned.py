class class1(object):
    def fonk1(self, b1 = None, move=None, b4=None, b6=None):
        if b6 is None:
            self.b2 = b1
            self.b3 = move
            self.b4 = b4
        else:
            self.b2 = b6.b1
            self.b3 = b6.move
            self.b4 = b6.b4
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
    def fonk7(self, b1 = None, move=None, b4=None, b6=None):
        if b6 is None:
            class1.fonk7(self, b1, move, b4)
        else:
            class1.fonk7(self, b6 = b6)
        self.a1 = 0
        self.a2 = 0
    def fonk8(self, other):
        return self.f_cost < other.f_cost
    @property
    def fonk9(self):
        return self.a1 + self.a2
if b7 = = "__main__":
    b8 = class1(b1=[[1, 2, 3], [4, 5, 6], [7, 0, 8]], move=None, b4=None)
    print("Board:", b8.b1)
    print("Move:", b8.move)
    print("Came From:", b8.b4)
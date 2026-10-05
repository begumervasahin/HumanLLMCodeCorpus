class class1:
    def fonk1(self, b1 = None, move=None, b4=None, b5=None):
        if b5 is None:
            self.b2 = b1
            self.b3 = move
            self.b4 = b4
        else:
            self.b2 = b5.b1
            self.b3 = b5.move
            self.b4 = b5.b4
    def fonk2(self):
        return hash(self.b2)
    def fonk3(self, other):
        return self.b2 = = other.b1
    @property
    def fonk4(self):
        return self.b2
    @property
    def fonk5(self):
        return self.b3
class class2(class1):
    def fonk6(self, b1 = None, move=None, b4=None, b5=None):
        if b5 is None:
            super().fonk6(b1, move, b4)
        else:
            super().fonk6(b5 = b5)
        self.a1 = 0
        self.a2 = 0
    def fonk7(self, other):
        return self.f_cost < other.f_cost
    @property
    def fonk8(self):
        return self.a1 + self.a2
if b6 = = "__main__":
    b7 = class1(b1=[[1, 2, 3], [4, 5, 6], [7, 0, 8]], move=None, b4=None)
    print("Board:", b7.b1)
    print("Move:", b7.move)
    print("Came From:", b7.b4)
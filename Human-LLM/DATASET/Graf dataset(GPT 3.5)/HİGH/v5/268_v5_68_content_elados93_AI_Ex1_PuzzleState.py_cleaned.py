class class1:
    def fonk1(self, b1 = None, b2=None, b3=None, b4=None):
        if b4 is None:
            self.b1 = b1
            self.b2 = b2
            self.b3 = b3
        else:
            self.b1 = b4.b1
            self.b2 = b4.b2
            self.b3 = b4.b3
    def fonk2(self):
        return hash(tuple(self.b1))
    def fonk3(self, other):
        return self.b1 = = other.b1
class class2(class1):
    def fonk4(self, b1 = None, b2=None, b3=None, b4=None):
        super().fonk4(b1, b2, b3) if b4 is None else super().fonk4(b4 = b4)
        self.a1 = 0
        self.a2 = 0
    def fonk5(self, other):
        return self.f_cost < other.f_cost
    @property
    def fonk6(self):
        return self.a1 + self.a2
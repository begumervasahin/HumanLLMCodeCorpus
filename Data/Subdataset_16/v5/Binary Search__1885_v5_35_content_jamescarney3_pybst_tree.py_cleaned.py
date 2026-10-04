class class1:
    def fonk1(self):
        self.b1 = None
    def fonk2(self, b2):
        if self.b1 is None:
            self.b1 = class2(b2)
        else:
            self.b1.fonk5(b2)
        return self.b1
    def fonk3(self, b2):
        if self.b1 is None:
            return None
        return self.b1.fonk6(b2)
class class2:
    def fonk4(self, b2):
        self.b2 = b2
        self.b3 = None
        self.b4 = None
    def fonk5(self, b2):
        if b2 < self.b2:
            if self.b3 is None:
                self.b3 = class2(b2)
            else:
                self.b3.fonk5(b2)
        elif b2 > self.b2:
            if self.b4 is None:
                self.b4 = class2(b2)
            else:
                self.b4.fonk5(b2)
    def fonk6(self, b2):
        if self.b2 = = b2:
            return self
        elif b2 < self.b2:
            return self.b3.fonk6(b2) if self.b3 else None
        elif b2 > self.b2:
            return self.b4.fonk6(b2) if self.b4 else None
        return None

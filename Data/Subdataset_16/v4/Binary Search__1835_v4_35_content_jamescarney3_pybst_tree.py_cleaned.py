class class1:
    def fonk1(self):
        self.b1 = None
    def fonk2(self, b2):
        if not self.b1:
            self.b1 = class2(b2)
        else:
            self.b1.fonk5(b2)
        return self.b1
    def fonk3(self, b2):
        if not self.b1:
            return None
        elif self.b1.b2 = = b2:
            return self.b1
        else:
            return self.b1.fonk6(b2)
class class2:
    def fonk4(self, b2):
        self.b2 = b2
        self.b3 = None
        self.b4 = None
    def fonk5(self, b2):
        if b2 < self.b2:
            if not self.b3:
                self.b3 = class2(b2)
                return self.b3
            else:
                self.b3.fonk5(b2)
        elif b2 > self.b2:
            if not self.b4:
                self.b4 = class2(b2)
                return self.b4
            else:
                self.b4.fonk5(b2)
        return None
    def fonk6(self, b2):
        if self.b2 = = b2:
            return self
        elif b2 < self.b2 and self.b3:
            return self.b3.fonk6(b2)
        elif b2 > self.b2 and self.b4:
            return self.b4.fonk6(b2)
        return None

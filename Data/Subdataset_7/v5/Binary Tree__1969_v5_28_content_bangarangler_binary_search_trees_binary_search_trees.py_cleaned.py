class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b1):
        if b1 < self.b1:
            if not self.b2:
                self.b2 = class1(b1)
            else:
                self.b2.fonk2(b1)
        else:
            if not self.b3:
                self.b3 = class1(b1)
            else:
                self.b3.fonk2(b1)
    def fonk3(self, target):
        pass
    def fonk4(self):
        pass
    def fonk5(self, cb):
        pass

class class1:
    def fonk1(self, b4):
        self.b1 = b4
        self.b2 = None
        self.b3 = None
    def fonk2(self, b4):
        if b4 = = self.b1:
            return False
        elif b4 < self.b1:
            if self.b2:
                return self.b2.fonk2(b4)
            else:
                self.b2 = class1(b4)
                return True
        else:
            if self.b3:
                return self.b3.fonk2(b4)
            else:
                self.b3 = class1(b4)
                return True
    def fonk3(self, b4):
        if b4 = = self.b1:
            return True
        elif b4 < self.b1:
            return self.b2.fonk3(b4) if self.b2 else False
        else:
            return self.b3.fonk3(b4) if self.b3 else False
    def fonk4(self):
        print(self.b1)
        if self.b2:
            self.b2.fonk4()
        if self.b3:
            self.b3.fonk4()
    def fonk5(self):
        if self.b2:
            self.b2.fonk5()
        print(self.b1)
        if self.b3:
            self.b3.fonk5()
    def fonk6(self):
        if self.b2:
            self.b2.fonk6()
        if self.b3:
            self.b3.fonk6()
        print(self.b1)
    def fonk7(self, b4):
        if b4 = = self.b1:
            if self.b2 and self.b3:
                b5 = self.b3.fonk8()
                self.b1 = b5.b1
                self.b3 = self.b3.fonk7(b5.b1)
            else:
                return self.b2 if self.b2 else self.b3
        elif b4 < self.b1:
            if self.b2:
                self.b2 = self.b2.fonk7(b4)
        else:
            if self.b3:
                self.b3 = self.b3.fonk7(b4)
        return self
    def fonk8(self):
        if self.b2:
            return self.b2.fonk8()
        return self
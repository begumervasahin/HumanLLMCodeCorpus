class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b1):
        if b1 = = self.b1:
            return False
        elif b1 < self.b1:
            if self.b2:
                return self.b2.fonk2(b1)
            else:
                self.b2 = class1(b1)
                return True
        else:
            if self.b3:
                return self.b3.fonk2(b1)
            else:
                self.b3 = class1(b1)
                return True
    def fonk3(self, b1):
        if b1 = = self.b1:
            return True
        elif b1 > self.b1:
            if self.b3:
                return self.b3.fonk3(b1)
            else:
                return False
        else:
            if self.b2:
                return self.b2.fonk3(b1)
            else:
                return False
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
    def fonk7(self, b1):
        if b1 = = self.b1:
            if self.b2 and self.b3:
                b4 = self.b3.fonk8()
                self.b1 = b4.b1
                self.b3 = self.b3.fonk7(self.b1)
                return self
            elif self.b2:
                return self.b2
            elif self.b3:
                return self.b3
            else:
                return None
        elif b1 < self.b1 and self.b2:
            self.b2 = self.b2.fonk7(b1)
            return self
        elif b1 > self.b1 and self.b3:
            self.b3 = self.b3.fonk7(b1)
            return self
        else:
            return self
    def fonk8(self):
        if self.b2:
            return self.b2.fonk8()
        else:
            return self
class class1:
    def fonk1(self, val):
        self.b1 = val
        self.b2 = None
        self.b3 = None
    def fonk2(self, val):
        if self.b1 = = val:
            return False
        elif val < self.b1:
            if self.b2:
                return self.b2.fonk2(val)
            else:
                self.b2 = class1(val)
                return True
        else:
            if self.b3:
                return self.b3.fonk2(val)
            else:
                self.b3 = class1(val)
                return True
    def fonk3(self, val):
        if self.b1 = = val:
            return True
        elif val > self.b1:
            return self.b3.fonk3(val) if self.b3 else False
        else:
            return self.b2.fonk3(val) if self.b2 else False
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
    def fonk7(self, val):
        if self.b1 = = val:
            if self.b2 and self.b3:
                b4 = self.b3.fonk8()
                self.b1 = b4.b1
                self.b3 = self.b3.fonk7(b4.b1)
            elif self.b2:
                return self.b2
            elif self.b3:
                return self.b3
            else:
                return None
        elif val > self.b1:
            if self.b3:
                self.b3 = self.b3.fonk7(val)
        else:
            if self.b2:
                self.b2 = self.b2.fonk7(val)
        return self
    def fonk8(self):
        if self.b2:
            return self.b2.fonk8()
        return self
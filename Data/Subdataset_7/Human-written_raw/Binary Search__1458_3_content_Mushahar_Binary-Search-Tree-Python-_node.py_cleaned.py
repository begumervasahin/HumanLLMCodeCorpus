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
        print('Entered find\n')
        if self.b1 = = val:
            return True
        elif val > self.b1:
            if self.b3:
                return self.b3.fonk3(val)
            else:
                return False
        else:
            if self.b2:
                return self.b2.fonk3(val)
            else:
                return False
    def fonk4(self):
        print(self.b1)
        if self.b2:
            self.b2.fonk4()
        if self.b3:
            self.b3.fonk4()
        return True
    def fonk5(self):
        if self.b2:
            self.b2.fonk5()
        print(self.b1)
        if self.b3:
            self.b3.fonk5()
        return True
    def fonk6(self):
        if self.b2:
            self.b2.fonk6()
        if self.b3:
            self.b3.fonk6()
        print(self.b1)
        return True
    def fonk7(self, val):
        if self.b1 = = val:
            if self.b2 and self.b3:
                b4 = self.b3.fonk8()
                self.b1 = b4.b1
                self.b3 = self.b3.fonk7(self.b1)
                return self
            elif self.b2:
                print('Match found and only b2 node')
                b5 = self.b2
                del self
                return b5
            elif self.b3:
                print('Match found and only b3 node')
                b6 = self.b3
                del self
                return b6
            else:
                print('Match found and no children')
                del self
                return None
        elif val > self.b1:
            if self.b3:
                self.b3 = self.b3.fonk7(val)
                return self
            else:
                print('class1 not found !!')
                return self
        else:
            if self.b2:
                self.b2 = self.b2.fonk7(val)
                return self
            else:
                print('class1 not found !!')
                return self
    def fonk8(self):
        if self.b2:
            return self.b2.fonk8()
        else:
            return self
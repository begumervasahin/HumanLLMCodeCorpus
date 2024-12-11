class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = class1()
    def fonk3(self):
        return self.b3.b2 is None
    def fonk4(self, item):
        b4 = class1(item)
        b4.b2 = self.b3.b2
        self.b3.b2 = b4
    def fonk5(self):
        b5 = self.b3.b2
        a1 = 0
        while b5:
            a1 += 1
            b5 = b5.b2
        return a1
    def fonk6(self, item):
        b5 = self.b3.b2
        while b5:
            if b5.b1 = = item:
                return True
            b5 = b5.b2
        return False
    def fonk7(self, item):
        b5 = self.b3.b2
        b6 = None
        while b5:
            if b5.b1 = = item:
                if b6:
                    b6.b2 = b5.b2
                else:
                    self.b3.b2 = b5.b2
                return
            b6 = b5
            b5 = b5.b2
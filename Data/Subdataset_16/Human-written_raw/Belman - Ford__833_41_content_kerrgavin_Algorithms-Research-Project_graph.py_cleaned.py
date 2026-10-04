class class1(object):
    def fonk1(self, b1 = [], b2 = [], b3 = False):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = {}
    def fonk2(self, b11):
        return self.b4[b11.b8]
    def fonk3(self,b8):
        b5 = class2(b8=b8)
        self.b1.append(b5)
        self.b4[b5.b8] = []
    def fonk4(self,b5,b11,b12):
        b6 = class3(b5,b11,b12)
        self.b4[b5.b8].append(b6)
        self.b2.append(b6)
        if not self.b3:
            b7 = class3(b11, b5, b12)
            if b11 not in self.b4:
                self.b4[b11.b8].append(b7)
class class2(object):
    def fonk5(self, b8 = None, b9 = None, b10 = None):
        self.b8 = b8
        self.b9 = b9
        self.b10 = b10
class class3(object):
    def fonk6(self, b5 = None, b11 = None, b12 = None):
        self.b5 = b5
        self.b11 = b11
        self.b12 = b12
    def fonk7(self,other):
        if self.b5 = = other.b5 and self.b11 == other.b11:
            return True
        return False
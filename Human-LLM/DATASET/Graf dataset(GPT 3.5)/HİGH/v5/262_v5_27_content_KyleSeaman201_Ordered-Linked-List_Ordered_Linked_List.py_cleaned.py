class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
    def fonk2(self):
        return str(self.b1)
class class2:
    def fonk3(self):
        self.b3 = None
        self.b4 = None
        self.a1 = 0
    def fonk4(self, b1):
        b5 = class1(b1)
        if self.b3 is None or self.b3.b1 >= b5.b1:
            b5.b2 = self.b3
            self.b3 = b5
        else:
            b6 = self.b3
            while b6.b2 and b6.b2.b1 < b5.b1:
                b6 = b6.b2
            b5.b2 = b6.b2
            b6.b2 = b5
        if b5.b2 is None:
            self.b4 = b5
        self.a1 += 1
    def fonk5(self, b1):
        if self.b3 is None:
            return
        if self.b3.b1 = = b1:
            self.b3 = self.b3.b2
            if self.b3 is None:
                self.b4 = None
            self.a1 -= 1
            return
        b6 = self.b3
        while b6.b2 and b6.b2.b1 != b1:
            b6 = b6.b2
        if b6.b2 and b6.b2.b1 = = b1:
            b6.b2 = b6.b2.b2
            if b6.b2 is None:
                self.b4 = b6
            self.a1 -= 1
    def fonk6(self, b1):
        b6 = self.b3
        while b6:
            if b6.b1 = = b1:
                return True
            b6 = b6.b2
        return False
    def fonk7(self):
        if self.b3 is None:
            return None
        if self.b3 = = self.b4:
            b1 = self.b3.b1
            self.b3 = None
            self.b4 = None
            self.a1 = 0
            return b1
        b6 = self.b3
        while b6.b2 != self.b4:
            b6 = b6.b2
        b1 = self.b4.b1
        b6.b2 = None
        self.b4 = b6
        self.a1 -= 1
        return b1
    def fonk8(self):
        return self.a1 = = 0
    def fonk9(self):
        b7 = []
        b6 = self.b3
        while b6:
            b7.append(str(b6))
            b6 = b6.b2
        return ' -> '.join(b7)

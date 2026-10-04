class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self):
        return f"class1({self.b1})"
class class2:
    def fonk3(self):
        self.b4 = None
        self.b5 = None
    def fonk4(self):
        return self.b4 is None
    def fonk5(self, item):
        b6 = class1(item)
        if self.fonk4():
            self.b4 = b6
        else:
            self.b5.b2 = b6
        self.b5 = b6
    def fonk6(self):
        a1 = 0
        b7 = self.b4
        while b7:
            a1 += 1
            b7 = b7.b2
        return a1
    def fonk7(self, item):
        b7 = self.b4
        while b7:
            if b7.b1 = = item:
                return True
            b7 = b7.b2
        return False
    def fonk8(self, item):
        b7 = self.b4
        b8 = None
        while b7:
            if b7.b1 = = item:
                if b8 is None:
                    self.b4 = b7.b2
                else:
                    b8.b2 = b7.b2
                if b7 = = self.b5:
                    self.b5 = b8
                return
            b8 = b7
            b7 = b7.b2
    def fonk9(self):
        b9 = []
        b7 = self.b4
        while b7:
            b9.append(str(b7.b1))
            b7 = b7.b2
        print(" -> ".join(b9))

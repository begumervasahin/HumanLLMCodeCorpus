class class1:
    def fonk1(self, val):
        self.b1 = val
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self, val):
        self.b4 = class1(val)
        self.b5 = self.b4
    def fonk3(self, val):
        b6 = self.b4
        while b6.b2 != None:
            b6 = b6.b2
        b7 = class1(val)
        b6.b2 = b7
        b7.b3 = b6
        self.b5 = b7
    def fonk4(self, val, newVal):
        if self.b5.b1 = = val:
            self.fonk3(newVal)
        elif self.b4.b1 = = val:
            b7 = class1(newVal)
            b7.b2 = self.b4.b2
            b7.b3 = self.b4
            b7.b2.b3 = b7
            self.b4.b2 = b7
        else:
            b6 = self.b4.b2
            while b6.b1 != val:
                b6 = b6.b2
            b7 = class1(newVal)
            b7.b2 = b6.b2
            b7.b2.b3 = b7
            b7.b3 = b6
            b6.b2 = b7
    def fonk5(self, val):
        if self.b4.b1 = = val:
            self.b4 = self.b4.b2
            self.b4.b3 = None
        elif self.b5.b1 = = val:
            self.b5 = self.b5.b3
            self.b5.b2 = None
        else:
            b6 = self.b4.b2
            while b6.b1 != val:
                b6 = b6.b2
            b6.b3.b2 = b6.b2
            b6.b2.b3 = b6.b3
    def fonk6(self):
        b6 = self.b5
        while b6 != None:
            print(b6.b1)
            b6 = b6.b3
    def fonk7(self):
        b6 = self.b4
        while b6 != None:
            print(b6.b1)
            b6 = b6.b2
if b8 = = "__main__":
    b9 = class2(10)
    b9.fonk3(20)
    b9.fonk3(30)
    b9.fonk3(40)
    b9.fonk5(40)
    b9.fonk7()
    b9.fonk6()
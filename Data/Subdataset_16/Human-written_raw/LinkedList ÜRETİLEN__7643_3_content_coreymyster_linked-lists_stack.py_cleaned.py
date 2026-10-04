class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self, newdata):
        self.b1 = newdata
    def fonk5(self, newnext):
        self.b2 = newnext
class class2:
    def fonk6(self):
        self.b3 = None
    def fonk7(self):
        return self.b3 = = None
    def fonk8(self, item):
        b4 = class1(item)
        b4.fonk5(self.b3)
        self.b3 = b4
    def fonk9(self):
        b5 = self.b3
        a1 = 0
        while b5 != None:
            a1 = a1 + 1
            b5 = b5.fonk3()
        return a1
    def fonk10(self, item):
        b5 = self.b3
        b6 = False
        while b5 != None and not b6:
            if b5.fonk2() == item:
                b6 = True
            else:
                b5 = b5.fonk3()
        return b6
    def fonk11(self):
        b5 = self.b3
        b7 = None
        if b7 = = None:
            self.b3 = b5.fonk3()
        else:
            b7.fonk5(b5.fonk3())
b8 = class2()
b8.fonk8(80)
print(b8.fonk9())
b8.fonk8(3)
b8.fonk8(67)
b8.fonk8(15)
print(b8.fonk9())
print(b8.fonk10(15))
b8.fonk11()
print(b8.fonk9())
print(b8.fonk10(15))
b8.fonk8(15)
print(b8.fonk9())
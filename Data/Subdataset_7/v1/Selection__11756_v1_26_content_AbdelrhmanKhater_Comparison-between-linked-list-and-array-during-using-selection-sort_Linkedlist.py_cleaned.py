class class1:
    def fonk1(self, initdata):
        self.b1 = initdata
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
        self.b3 = class1(None)
    def fonk7(self):
        return self.b3.fonk3() is None
    def fonk8(self, item):
        b4 = class1(item)
        b4.fonk5(self.b3.fonk3())
        self.b3.fonk5(b4)
    def fonk9(self):
        b5 = self.b3.fonk3()
        a1 = 0
        while b5 is not None:
            a1 += 1
            b5 = b5.fonk3()
        return a1
    def fonk10(self, item):
        b5 = self.b3.fonk3()
        b6 = False
        while b5 is not None and not b6:
            if b5.fonk2() == item:
                b6 = True
            else:
                b5 = b5.fonk3()
        return b6
    def fonk11(self, item):
        b5 = self.b3.fonk3()
        b7 = None
        b6 = False
        while not b6 and b5 is not None:
            if b5.fonk2() == item:
                b6 = True
            else:
                b7 = b5
                b5 = b5.fonk3()
        if b7 is None:
            self.b3 = b5.fonk3()
        else:
            b7.fonk5(b5.fonk3())
if b8 = = "__main__":
    b9 = class2()
    print(b9.fonk7())
    b9.fonk8(1)
    b9.fonk8(2)
    b9.fonk8(3)
    print(b9.fonk9())
    print(b9.fonk10(2))
    print(b9.fonk10(4))
    b9.fonk11(1)
    print(b9.fonk9())
    print(b9.fonk7())
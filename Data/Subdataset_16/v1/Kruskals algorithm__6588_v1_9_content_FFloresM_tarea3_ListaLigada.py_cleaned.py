class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self, newdato):
        self.b1 = newdato
    def fonk5(self, newsig):
        self.b2 = newsig
class class2:
    def fonk6(self):
        self.b3 = None
        self.b4 = None
    def fonk7(self):
        return self.b3 is None
    def fonk8(self, item):
        b5 = class1(item)
        if self.fonk7():
            self.b3 = b5
            self.b4 = b5
        else:
            self.b4.fonk5(b5)
            self.b4 = b5
    def fonk9(self):
        b6 = self.b3
        a1 = 0
        while b6 is not None:
            a1 += 1
            b6 = b6.fonk3()
        return a1
    def fonk10(self, item):
        b6 = self.b3
        b7 = False
        while b6 is not None and not b7:
            if b6.fonk2() == item:
                b7 = True
            else:
                b6 = b6.fonk3()
        return b7
    def fonk11(self, item):
        b6 = self.b3
        b8 = None
        b7 = False
        while b6 is not None and not b7:
            if b6.fonk2() == item:
                b7 = True
            else:
                b8 = b6
                b6 = b6.fonk3()
        if b7:
            if b8 is None:
                self.b3 = b6.fonk3()
            else:
                b8.fonk5(b6.fonk3())
            if b6 = = self.b4:
                self.b4 = b8
    def fonk12(self):
        b6 = self.b3
        while b6 is not None:
            print(b6.fonk2(), b9 = '')
            b6 = b6.fonk3()
            if b6 is not None:
                print(" -> ", b9 = "")
        print()
if b10 = = "__main__":
    b11 = class2()
    b11.fonk8(1)
    b11.fonk8(2)
    b11.fonk8(3)
    b11.fonk12()
    print("Size:", b11.fonk9())
    print("Buscar 2:", b11.fonk10(2))
    print("Buscar 5:", b11.fonk10(5))
    b11.fonk11(2)
    b11.fonk12()

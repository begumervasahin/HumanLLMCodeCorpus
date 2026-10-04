class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self, new_next):
        self.b2 = new_next
class class2:
    def fonk5(self):
        self.b3 = None
        self.b4 = None
        self.a1 = 0
    def fonk6(self):
        return self.b3 is None
    def fonk7(self, item):
        b5 = class1(item)
        b5.fonk4(self.b3)
        self.b3 = b5
        if self.b4 is None:
            self.b4 = b5
        self.a1 += 1
    def fonk8(self, item):
        b5 = class1(item)
        if self.fonk6() or self.b4.fonk2() >= b5.fonk2():
            self.fonk9(b5)
            return
        b6 = None
        b7 = self.b4
        while b7 and b7.fonk2() <= b5.fonk2():
            b6 = b7
            b7 = b7.fonk3()
        b5.fonk4(b7)
        if b6:
            b6.fonk4(b5)
        else:
            self.b4 = b5
        self.a1 += 1
    def fonk9(self, b5):
        b5.fonk4(self.b4)
        self.b4 = b5
        if self.b3 is None:
            self.b3 = b5
        self.a1 += 1
    def fonk10(self):
        return self.a1
    def fonk11(self, item):
        b7 = self.b3
        while b7:
            if b7.fonk2() == item:
                return True
            b7 = b7.fonk3()
        return False
    def fonk12(self, item):
        b7 = self.b3
        b6 = None
        while b7:
            if b7.fonk2() == item:
                break
            b6 = b7
            b7 = b7.fonk3()
        if not b7:
            return
        if b6 is None:
            self.b3 = b7.fonk3()
        else:
            b6.fonk4(b7.fonk3())
        if b7 = = self.b4:
            self.b4 = b6
        self.a1 -= 1
if b8 = = "__main__":
    b9 = class2()
    b9.fonk7(10)
    b9.fonk7(20)
    b9.fonk7(30)
    print("Search for 20:", b9.fonk11(20))
    print("Search for 40:", b9.fonk11(40))
    b9.fonk12(20)
    print("Search for 20 after removal:", b9.fonk11(20))
    print("Length of the list:", b9.fonk10())

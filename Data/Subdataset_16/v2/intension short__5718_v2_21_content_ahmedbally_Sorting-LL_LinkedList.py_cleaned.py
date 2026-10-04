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
        if self.fonk6():
            self.b4 = b5
        self.b3 = b5
        self.a1 += 1
    def fonk8(self, b5):
        b6 = self.b4
        b7 = None
        while b6 is not None and b6.fonk2() <= b5.fonk2():
            b7 = b6
            b6 = b6.fonk3()
        if b7 is None:
            b5.fonk4(self.b4)
            self.b4 = b5
        else:
            b5.fonk4(b6)
            b7.fonk4(b5)
    def fonk9(self):
        a2 = 0
        b6 = self.b3
        while b6 is not None:
            a2 += 1
            b6 = b6.fonk3()
        return a2
    def fonk10(self, item):
        b6 = self.b3
        while b6 is not None:
            if b6.fonk2() == item:
                return True
            b6 = b6.fonk3()
        return False
    def fonk11(self, item):
        b6 = self.b3
        b7 = None
        while b6 is not None:
            if b6.fonk2() == item:
                break
            b7 = b6
            b6 = b6.fonk3()
        if b6 is None:
            return
        if b7 is None:
            self.b3 = b6.fonk3()
        else:
            b7.fonk4(b6.fonk3())
        if b6 = = self.b4:
            self.b4 = b7
        self.a1 -= 1
if b8 = = "__main__":
    b9 = class2()
    b9.fonk7(10)
    b9.fonk7(20)
    b9.fonk7(30)
    print("Search for 20:", b9.fonk10(20))
    print("Search for 40:", b9.fonk10(40))
    b9.fonk11(20)
    print("Search for 20 after removal:", b9.fonk10(20))
    print("Length of the list:", b9.fonk9())

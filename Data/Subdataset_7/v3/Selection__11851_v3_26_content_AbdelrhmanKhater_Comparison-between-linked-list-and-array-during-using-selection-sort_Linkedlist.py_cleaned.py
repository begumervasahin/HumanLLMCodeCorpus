class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
    def fonk2(self):
        return self.b1
    def fonk3(self, new_data):
        self.b1 = new_data
    def fonk4(self):
        return self.b2
    def fonk5(self, new_next):
        self.b2 = new_next
class class2:
    def fonk6(self):
        self.b3 = class1(None)
    def fonk7(self):
        return self.b3.fonk4() is None
    def fonk8(self, item):
        b4 = class1(item)
        b4.fonk5(self.b3.fonk4())
        self.b3.fonk5(b4)
    def fonk9(self):
        b5 = self.b3.fonk4()
        a1 = 0
        while b5 is not None:
            a1 += 1
            b5 = b5.fonk4()
        return a1
    def fonk10(self, item):
        b5 = self.b3.fonk4()
        while b5 is not None:
            if b5.fonk2() == item:
                return True
            b5 = b5.fonk4()
        return False
    def fonk11(self, item):
        b5 = self.b3.fonk4()
        b6 = self.b3
        while b5 is not None:
            if b5.fonk2() == item:
                b6.fonk5(b5.fonk4())
                return
            b6 = b5
            b5 = b5.fonk4()
if b7 = = "__main__":
    b8 = class2()
    print(b8.fonk7())
    b8.fonk8(1)
    b8.fonk8(2)
    b8.fonk8(3)
    print(b8.fonk9())
    print(b8.fonk10(2))
    print(b8.fonk10(4))
    b8.fonk11(1)
    print(b8.fonk9())
    print(b8.fonk7())
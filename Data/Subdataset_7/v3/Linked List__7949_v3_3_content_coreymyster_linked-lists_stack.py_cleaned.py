class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self):
        return self.b3 is None
    def fonk4(self, b6):
        b4 = class1(b6)
        b4.b2 = self.b3
        self.b3 = b4
    def fonk5(self):
        a1 = 0
        b5 = self.b3
        while b5:
            a1 += 1
            b5 = b5.b2
        return a1
    def fonk6(self, b6):
        b5 = self.b3
        while b5:
            if b5.b1 = = b6:
                return True
            b5 = b5.b2
        return False
    def fonk7(self):
        if self.b3:
            b6 = self.b3.b1
            self.b3 = self.b3.b2
            return b6
        else:
            raise IndexError("Pop from an empty list")
if b7 = = "__main__":
    b8 = class2()
    b8.fonk4(80)
    print("Size:", b8.fonk5())
    b8.fonk4(3)
    b8.fonk4(67)
    b8.fonk4(15)
    print("Size:", b8.fonk5())
    print("Search for 15:", b8.fonk6(15))
    b8.fonk7()
    print("Size after pop:", b8.fonk5())
    print("Search for 15 after pop:", b8.fonk6(15))
    b8.fonk4(15)
    print("Size after pushing 15 again:", b8.fonk5())
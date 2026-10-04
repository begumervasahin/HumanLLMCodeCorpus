class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
    def fonk2(self):
        return f"class1({self.b1})"
class class2:
    def fonk3(self):
        self.b3 = None
        self.b4 = None
    def fonk4(self):
        return self.b3 is None
    def fonk5(self, item):
        b5 = class1(item)
        if self.fonk4():
            self.b3 = b5
            self.b4 = b5
        else:
            self.b4.b2 = b5
            self.b4 = b5
    def fonk6(self):
        a1 = 0
        b6 = self.b3
        while b6:
            a1 += 1
            b6 = b6.b2
        return a1
    def fonk7(self, item):
        b6 = self.b3
        while b6:
            if b6.b1 = = item:
                return True
            b6 = b6.b2
        return False
    def fonk8(self, item):
        b6 = self.b3
        b7 = None
        b8 = False
        while b6 and not b8:
            if b6.b1 = = item:
                b8 = True
            else:
                b7 = b6
                b6 = b6.b2
        if b8:
            if b7 is None:
                self.b3 = b6.b2
            else:
                b7.b2 = b6.b2
            if b6 = = self.b4:
                self.b4 = b7
    def fonk9(self):
        b6 = self.b3
        while b6:
            print(b6.b1, b9 = " -> " if b6.b2 else "\n")
            b6 = b6.b2
if b10 = = "__main__":
    b11 = class2()
    b11.fonk5(1)
    b11.fonk5(2)
    b11.fonk5(3)
    b11.fonk9()
    print("Size:", b11.fonk6())
    print("Search 2:", b11.fonk7(2))
    print("Search 5:", b11.fonk7(5))
    b11.fonk8(2)
    b11.fonk9()

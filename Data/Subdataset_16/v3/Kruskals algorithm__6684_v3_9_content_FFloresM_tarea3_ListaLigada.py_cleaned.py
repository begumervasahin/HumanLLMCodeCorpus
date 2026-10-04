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
    def fonk5(self, b1):
        b5 = class1(b1)
        if self.fonk4():
            self.b3 = b5
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
    def fonk7(self, b1):
        b6 = self.b3
        while b6:
            if b6.b1 = = b1:
                return True
            b6 = b6.b2
        return False
    def fonk8(self, b1):
        b6 = self.b3
        b7 = None
        while b6:
            if b6.b1 = = b1:
                if b7 is None:
                    self.b3 = b6.b2
                else:
                    b7.b2 = b6.b2
                if b6 = = self.b4:
                    self.b4 = b7
                return
            b7 = b6
            b6 = b6.b2
    def fonk9(self):
        b6 = self.b3
        while b6:
            print(b6.b1, b8 = " -> " if b6.b2 else "\n")
            b6 = b6.b2
if b9 = = "__main__":
    b10 = class2()
    b10.fonk5(1)
    b10.fonk5(2)
    b10.fonk5(3)
    b10.fonk9()
    print("Size:", b10.fonk6())
    print("Search 2:", b10.fonk7(2))
    print("Search 5:", b10.fonk7(5))
    b10.fonk8(2)
    b10.fonk9()

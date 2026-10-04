class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self, new_value):
        self.b1 = new_value
    def fonk5(self, new_next):
        self.b2 = new_next
    def fonk6(self):
        return f"{self.b1}"
    b3 = __str__
class class2:
    def fonk7(self):
        self.b4 = None
        self.b5 = None
    def fonk8(self, b1):
        b6 = class1(b1)
        if self.b4 is None:
            self.b4 = b6
            self.b5 = b6
        elif self.b4.b1 > b6.b1:
            b6.b2 = self.b4
            self.b4 = b6
        elif self.b5.b1 < b6.b1:
            self.b5.b2 = b6
            self.b5 = b6
        else:
            b7 = self.b4
            while b7.b1 < b6.b1:
                b8 = b7
                b7 = b7.b2
            b8.b2 = b6
            b6.b2 = b7
    def fonk9(self, b1):
        if self.b4 and self.b4.b1 = = b1:
            self.b4 = self.b4.b2
            if self.b4 is None:
                self.b5 = None
        elif self.b5 and self.b5.b1 = = b1:
            b7 = self.b4
            while b7.b2 != self.b5:
                b7 = b7.b2
            self.b5 = b7
            self.b5.b2 = None
        else:
            b7 = self.b4
            while b7 and b7.b1 != b1:
                b8 = b7
                b7 = b7.b2
            if b7:
                b8.b2 = b7.b2
                if b7 = = self.b5:
                    self.b5 = b8
    def fonk10(self, b1):
        b7 = self.b4
        while b7:
            if b7.b1 = = b1:
                return True
            b7 = b7.b2
        return False
    def fonk11(self):
        if self.b5:
            b1 = self.b5.b1
            b7 = self.b4
            if self.b4 = = self.b5:
                self.b4 = None
                self.b5 = None
            else:
                while b7.b2 != self.b5:
                    b7 = b7.b2
                self.b5 = b7
                self.b5.b2 = None
            return b1
        raise IndexError("pop from empty list")
    def fonk12(self):
        return self.b4 is None
    def fonk13(self):
        a1 = 0
        b7 = self.b4
        while b7:
            a1 += 1
            b7 = b7.b2
        return a1
    def fonk14(self):
        b7 = self.b4
        while b7:
            print(b7.fonk2(), b9 = ' ')
            b7 = b7.fonk3()
        print()
if b10 = = "__main__":
    b11 = class2()
    b11.fonk8(3)
    b11.fonk8(1)
    b11.fonk8(2)
    b11.fonk8(5)
    b11.fonk8(4)
    print("Ordered List:")
    b11.fonk14()
    print("\nAfter deleting 3:")
    b11.fonk9(3)
    b11.fonk14()
    print("\nSearch for 4:", b11.fonk10(4))
    print("Search for 3:", b11.fonk10(3))
    print("\nPop last element:", b11.fonk11())
    b11.fonk14()
    print("\nIs empty:", b11.fonk12())
    print("Size of list:", b11.fonk13())
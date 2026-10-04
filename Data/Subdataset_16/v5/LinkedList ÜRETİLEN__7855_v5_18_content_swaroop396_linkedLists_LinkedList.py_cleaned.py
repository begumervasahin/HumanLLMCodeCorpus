class class1:
    def fonk1(self, b1 = None, b2=None):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, b1):
        self.b1 = b1
    def fonk3(self, node):
        self.b2 = node
    def fonk4(self):
        return self.b1
    def fonk5(self):
        return self.b2
class class2:
    def fonk6(self):
        self.b3 = None
    def fonk7(self, b1):
        b4 = class1(b1)
        b4.fonk3(self.b3)
        self.b3 = b4
    def fonk8(self, b1):
        if self.b3 is None:
            self.b3 = class1(b1)
            return
        b5 = self.b3
        while b5.fonk5():
            b5 = b5.fonk5()
        b5.fonk3(class1(b1))
    def fonk9(self):
        if self.b3 is None:
            print("Empty List!!!")
            return
        b5 = self.b3
        while b5:
            print(str(b5.fonk4()), b6 = " --> " if b5.fonk5() else "")
            b5 = b5.fonk5()
        print()
    def fonk10(self):
        b5 = self.b3
        a1 = 0
        while b5:
            a1 += 1
            b5 = b5.fonk5()
        return a1
    def fonk11(self, b1):
        b5 = self.b3
        a2 = 0
        while b5:
            if b5.fonk4() == b1:
                return a2
            a2 += 1
            b5 = b5.fonk5()
        return -1
    def fonk12(self, b1):
        b5 = self.b3
        b7 = None
        while b5:
            if b5.fonk4() == b1:
                if b7 is None:
                    self.b3 = b5.fonk5()
                else:
                    b7.fonk3(b5.fonk5())
                return True
            b7 = b5
            b5 = b5.fonk5()
        return False
    def fonk13(self):
        if self.b3 is None:
            return None
        b5 = self.b3
        b8 = b5.fonk4()
        while b5:
            if b5.fonk4() > b8:
                b8 = b5.fonk4()
            b5 = b5.fonk5()
        return b8
    def fonk14(self):
        if self.b3 is None:
            return None
        b5 = self.b3
        b9 = b5.fonk4()
        while b5:
            if b5.fonk4() < b9:
                b9 = b5.fonk4()
            b5 = b5.fonk5()
        return b9
    def fonk15(self, b1):
        self.fonk8(b1)
    def fonk16(self):
        if self.b3 is None:
            return None
        b5 = self.b3
        b7 = None
        while b5.fonk5():
            b7 = b5
            b5 = b5.fonk5()
        if b7 is None:
            self.b3 = None
        else:
            b7.fonk3(None)
        return b5.fonk4()
    def fonk17(self, a2):
        b5 = self.b3
        a3 = 0
        while b5 and a3 < a2:
            b5 = b5.fonk5()
            a3 += 1
        if b5 is None:
            raise IndexError("Index out of range")
        return b5.fonk4()
    def fonk18(self):
        b10 = class2()
        b5 = self.b3
        while b5:
            b10.fonk8(b5.fonk4())
            b5 = b5.fonk5()
        return b10
    def fonk19(self):
        self.b3 = None
    def fonk20(self, a2):
        b1 = self.fonk17(a2)
        self.fonk12(b1)
        return b1
    def fonk21(self, b11 = ""):
        b5 = self.b3
        b12 = []
        while b5:
            b12.append(str(b5.fonk4()))
            b5 = b5.fonk5()
        return b11.join(b12)
    def fonk22(self, element):
        b5 = self.b3
        a4 = 0
        while b5:
            if b5.fonk4() == element:
                a4 += 1
            b5 = b5.fonk5()
        return a4
    def fonk23(self):
        b5 = self.b3
        b12 = []
        while b5:
            b12.append(b5.fonk4())
            b5 = b5.fonk5()
        return b12
    def fonk24(self):
        b5 = self.b3
        b12 = set()
        while b5:
            b12.add(b5.fonk4())
            b5 = b5.fonk5()
        return b12
    def fonk25(self):
        b5 = self.b3
        b7 = None
        while b5:
            b13 = b5.fonk5()
            b5.fonk3(b7)
            b7 = b5
            b5 = b13
        self.b3 = b7
    def fonk26(self):
        if self.b3 is None:
            return
        b5 = self.b3
        while b5:
            b14 = b5
            b13 = b5.fonk5()
            while b13:
                if b13.fonk4() < b14.fonk4():
                    b14 = b13
                b13 = b13.fonk5()
            b15 = b5.fonk4()
            b5.fonk2(b14.fonk4())
            b14.fonk2(b15)
            b5 = b5.fonk5()
    def fonk27(self):
        b16 = self.fonk23()
        b16.fonk26()
        b17 = class2()
        for b1 in b16:
            b17.fonk8(b1)
        return b17
if b18 = = "__main__":
    b19 = class2()
    b19.fonk7(5)
    b19.fonk7(4)
    b19.fonk7(3)
    b19.fonk7(2)
    b19.fonk7(1)
    b19.fonk9()
    b19.fonk8(12)
    b19.fonk8(13)
    b19.fonk8(3)
    b19.fonk9()
    print("Length:", b19.fonk10())
    print("Index of 3:", b19.fonk11(3))
    print("Element at index 5:", b19.fonk17(5))
    print("Remove 12:", b19.fonk12(12))
    b19.fonk20(2)
    b19.fonk9()
    print("Max:", b19.fonk13())
    print("Min:", b19.fonk14())
    b19.fonk15(31)
    b19.fonk9()
    print("Pop:", b19.fonk16())
    b19.fonk9()
    b20 = b19.fonk18()
    b20.fonk9()
    b20.fonk19()
    b20.fonk9()
    print("To string:", b19.fonk21(","))
    print("Count of 3:", b19.fonk22(3))
    b10 = b19.fonk23()
    print("To list:", b10)
    b21 = b19.fonk24()
    print("To set:", b21)
    b19.fonk25()
    b19.fonk9()
    b22 = b19.fonk27()
    b22.fonk9()
    b19.fonk26()
    b19.fonk9()
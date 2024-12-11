class class1:
    def fonk1(self):
        self.b1 = None
    def fonk2(self, b9):
        b2 = class2(b9)
        b2.fonk25(self.b1)
        self.b1 = b2
    def fonk3(self, b9):
        b2 = class2(b9)
        if not self.b1:
            self.b1 = b2
            return
        b3 = self.b1
        while b3.fonk27():
            b3 = b3.fonk27()
        b3.fonk25(b2)
    def fonk4(self):
        b3 = self.b1
        while b3:
            print(b3.fonk26(), b4 = " ")
            b3 = b3.fonk27()
            if b3:
                print("-->", b4 = " ")
        print()
    def fonk5(self):
        b3 = self.b1
        a1 = 0
        while b3:
            a1 += 1
            b3 = b3.fonk27()
        return a1
    def fonk6(self, b9):
        b3 = self.b1
        a2 = 0
        while b3:
            if b3.fonk26() == b9:
                return a2
            else:
                a2 += 1
                b3 = b3.fonk27()
    def fonk7(self, item):
        b3 = self.b1
        b5 = None
        b6 = False
        while not b6 and b3:
            if b3.fonk26() == item:
                b6 = True
            else:
                b5 = b3
                b3 = b3.fonk27()
        if b5 is None:
            self.b1 = b3.fonk27()
        else:
            b5.fonk25(b3.fonk27())
        return b6
    def fonk8(self):
        b3 = self.b1
        b7 = b3.fonk26()
        while b3:
            if b3.fonk26() > b7:
                b7 = b3.fonk26()
            b3 = b3.fonk27()
        return b7
    def fonk9(self):
        b3 = self.b1
        b8 = b3.fonk26()
        while b3:
            if b3.fonk26() < b8:
                b8 = b3.fonk26()
            b3 = b3.fonk27()
        return b8
    def fonk10(self, b9):
        self.fonk3(b9)
    def fonk11(self):
        b3 = self.b1
        b5 = None
        while b3.fonk27():
            b5 = b3
            b3 = b3.fonk27()
        if b5 is None:
            self.b1 = None
        else:
            b5.fonk25(None)
            b9 = b3.fonk26()
            del b3
            return b9
    def fonk12(self, a2):
        b3 = self.b1
        a3 = 0
        while a3 != a2:
            b3 = b3.fonk27()
            a3 += 1
        return b3.fonk26()
    def fonk13(self):
        b10 = class1()
        b3 = self.b1
        while b3:
            b10.fonk3(b3.fonk26())
            b3 = b3.fonk27()
        return b10
    def fonk14(self):
        self.b1 = None
    def fonk15(self, a2):
        b9 = self.fonk12(a2)
        self.fonk7(b9)
        return b9
    def fonk16(self, b11 = ""):
        b3 = self.b1
        b12 = ""
        while b3:
            b12 += str(b3.fonk26())
            b3 = b3.fonk27()
            if b3:
                b12 += b11
        return b12
    def fonk17(self, element):
        b3 = self.b1
        a4 = 0
        while b3:
            if b3.fonk26() == element:
                a4 += 1
            b3 = b3.fonk27()
        return a4
    def fonk18(self):
        b3 = self.b1
        b12 = []
        while b3:
            b12.append(b3.fonk26())
            b3 = b3.fonk27()
        return b12
    def fonk19(self):
        b3 = self.b1
        b12 = set()
        while b3:
            b12.add(b3.fonk26())
            b3 = b3.fonk27()
        return b12
    def fonk20(self):
        b3 = self.b1
        b13 = None
        while b3:
            b14 = b3.fonk27()
            b3.fonk25(b13)
            b13 = b3
            b3 = b14
        self.b1 = b13
    def fonk21(self):
        b3 = self.b1
        while b3:
            b15 = b3
            b14 = b3.fonk27()
            while b14:
                if b14.fonk26() < b15.fonk26():
                    b15 = b14
                b14 = b14.fonk27()
            b16 = b3.fonk26()
            b3.fonk24(b15.fonk26())
            b15.fonk24(b16)
            b3 = b3.fonk27()
    def fonk22(self):
        b10 = self.fonk13()
        b10.fonk21()
        return b10
class class2:
    def fonk23(self, b9 = None, b14=None):
        self.b9 = b9
        self.b14 = b14
    def fonk24(self, b9):
        self.b9 = b9
    def fonk25(self, node):
        self.b14 = node
    def fonk26(self):
        return self.b9
    def fonk27(self):
        return self.b14
b17 = class1()
b17.fonk2(5)
b17.fonk2(4)
b17.fonk2(3)
b17.fonk2(2)
b17.fonk2(1)
b17.fonk4()
b17.fonk3(12)
b17.fonk3(13)
b17.fonk3(3)
b17.fonk4()
print(b17.fonk5())
print(b17.fonk6(3))
print(b17.fonk12(5))
print(b17.fonk7(12))
b17.fonk15(2)
b17.fonk4()
print(b17.fonk8())
print(b17.fonk9())
b17.fonk10(31)
b17.fonk4()
print(b17.fonk11())
b17.fonk4()
b18 = b17.fonk13()
b18.fonk4()
b18.fonk14()
b18.fonk4()
print(b17.fonk16(","))
print(b17.fonk17(3))
b10 = b17.fonk18()
print(b10)
b19 = b17.fonk19()
print(b19)
b17.fonk20()
b17.fonk4()
b20 = b17.fonk22()
b20.fonk4()
b17.fonk21()
b17.fonk4()
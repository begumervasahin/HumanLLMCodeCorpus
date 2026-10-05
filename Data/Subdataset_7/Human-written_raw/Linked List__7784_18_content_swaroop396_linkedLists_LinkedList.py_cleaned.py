class class1:
    def fonk1(self):
        self.b1 = None
    def fonk2(self, b9):
        b2 = class2(b9)
        b2.fonk25(self.b1)
        self.b1 = b2
        del b2
    def fonk3(self, b9):
        b3 = self.b1
        b2 = class2(b9)
        while b3.fonk27():
            b3 = b3.fonk27()
        b3.fonk25(b2)
        del b2
        return True
    def fonk4(self):
        b3 = self.b1
        if b3 is None:
            print("Empty List!!!")
            return False
        while b3:
            print(str(b3.fonk26()), b4 = " ")
            b3 = b3.b20
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
        a2 = 1
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
        while not b6:
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
            if b7 < b3.fonk26():
                b7 = b3.fonk26()
            b3 = b3.fonk27()
        return b7
    def fonk9(self):
        b3 = self.b1
        b8 = b3.fonk26()
        while b3:
            if b8 > b3.fonk26():
                b8 = b3.fonk26()
            b3 = b3.fonk27()
        return b8
    def fonk10(self, b9):
        self.fonk3(b9)
        return True
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
        a2 = int(a2)
        a3 = 1
        while a3 != a2:
            b3 = b3.fonk27()
            a3 += 1
        b9 = b3.fonk26()
        return b9
    def fonk13(self):
        b10 = class1()
        b3 = self.b1
        b10.fonk2(b3.fonk26())
        b3 = b3.fonk27()
        while b3:
            b10.fonk3(b3.fonk26())
            b3 = b3.fonk27()
        return b10
    def fonk14(self):
        self.b1 = None
        return True
    def fonk15(self, a2):
        b9 = self.fonk12(a2)
        self.fonk7(b9)
        return b9
    def fonk16(self, b11 = ""):
        b3 = self.b1
        b12 = ""
        while b3:
            b13 = b3.fonk26()
            b12 += str(b13)
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
        b14 = []
        while b3:
            b15 = b3.fonk26()
            b14.append(b15)
            b3 = b3.fonk27()
        return b14
    def fonk19(self):
        b3 = self.b1
        b16 = set()
        while b3:
            b15 = b3.fonk26()
            if b15 not in b16:
                b16.add(b15)
            b3 = b3.fonk27()
        return b16
    def fonk20(self):
        b3 = self.b1
        b2 = None
        b17 = None
        while b3:
            b2 = b3.fonk27()
            b3.fonk25(b17)
            b17 = b3
            b3 = b2
        self.b1 = b17
        return True
    def fonk21(self):
        b3 = self.b1
        b18 = b3
        while b18:
            b2 = b18
            b19 = b18
            b8 = b18.fonk26()
            while b2:
                if b8 > b2.fonk26():
                    b8 = b2.fonk26()
                    b19 = b2
                b2 = b2.fonk27()
            b10 = b18.fonk26()
            b18.fonk24(b19.fonk26())
            b19.fonk24(b10)
            b18 = b18.fonk27()
    def fonk22(self):
        b3 = self.b1
        b14 = self.fonk13()
        b14.fonk21()
        return b14
class class2:
    def fonk23(self, b9 = None, b20=None):
        self.b9 = b9
        self.b20 = b20
    def fonk24(self, b9):
        self.b9 = b9
    def fonk25(self, node):
        self.b20 = node
    def fonk26(self):
        return self.b9
    def fonk27(self):
        return self.b20
b21 = class1()
b21.fonk2(5)
b21.fonk2(4)
b21.fonk2(3)
b21.fonk2(2)
b21.fonk2(1)
b21.fonk4()
b21.fonk3(12)
b21.fonk3(13)
b21.fonk3(3)
b21.fonk4()
print(b21.fonk5())
print(b21.fonk6(3))
print(b21.fonk12(5))
print(b21.fonk7(12))
b21.fonk15(2)
b21.fonk4()
print(b21.fonk8())
print(b21.fonk9())
print(b21.fonk10(31))
b21.fonk4()
print(b21.fonk11())
b21.fonk4()
b22 = b21.fonk13()
b22.fonk4()
b22.fonk14()
b22.fonk4()
print(b21.fonk16(","))
print(b21.fonk17(3))
b23 = b21.fonk18()
print(b23)
b24 = b21.fonk19()
print(b24)
b21.fonk20()
b21.fonk4()
b25 = b21.fonk22()
b25.fonk4()
b21.fonk21()
b21.fonk4()
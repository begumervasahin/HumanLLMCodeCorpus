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
            return True
        b5 = self.b3
        b4 = class1(b1)
        while b5.fonk5():
            b5 = b5.fonk5()
        b5.fonk3(b4)
        return True
    def fonk9(self):
        b5 = self.b3
        if b5 is None:
            print("Empty List!!!")
            return False
        while b5:
            print(str(b5.fonk4()), b6 = " ")
            b5 = b5.fonk5()
            if b5:
                print("-->", b6 = " ")
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
            else:
                a2 += 1
                b5 = b5.fonk5()
        return -1
    def fonk12(self, item):
        b5 = self.b3
        b7 = None
        while b5:
            if b5.fonk4() == item:
                if b7 is None:
                    self.b3 = b5.fonk5()
                else:
                    b7.fonk3(b5.fonk5())
                return True
            else:
                b7 = b5
                b5 = b5.fonk5()
        return False
    def fonk13(self):
        if self.b3 is None:
            return None
        b5 = self.b3
        b8 = b5.fonk4()
        while b5:
            if b8 < b5.fonk4():
                b8 = b5.fonk4()
            b5 = b5.fonk5()
        return b8
    def fonk14(self):
        if self.b3 is None:
            return None
        b5 = self.b3
        b9 = b5.fonk4()
        while b5:
            if b9 > b5.fonk4():
                b9 = b5.fonk4()
            b5 = b5.fonk5()
        return b9
    def fonk15(self, b1):
        return self.fonk8(b1)
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
        while a3 != a2 and b5:
            b5 = b5.fonk5()
            a3 += 1
        if b5 is None:
            raise IndexError("Index out of range")
        return b5.fonk4()
    def fonk18(self):
        b10 = class2()
        b5 = self.b3
        if b5 is None:
            return b10
        b10.fonk7(b5.fonk4())
        b5 = b5.fonk5()
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
        b12 = ""
        while b5:
            b12 += str(b5.fonk4())
            b5 = b5.fonk5()
            if b5:
                b12 += b11
        return b12
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
        b13 = []
        while b5:
            b13.append(b5.fonk4())
            b5 = b5.fonk5()
        return b13
    def fonk24(self):
        b5 = self.b3
        b14 = set()
        while b5:
            b14.add(b5.fonk4())
            b5 = b5.fonk5()
        return b14
    def fonk25(self):
        b5 = self.b3
        b15 = None
        while b5:
            b16 = b5.fonk5()
            b5.fonk3(b15)
            b15 = b5
            b5 = b16
        self.b3 = b15
    def fonk26(self):
        if self.b3 is None:
            return
        b5 = self.b3
        while b5:
            b17 = b5
            b9 = b17
            while b17:
                if b17.fonk4() < b9.fonk4():
                    b9 = b17
                b17 = b17.fonk5()
            b18 = b5.fonk4()
            b5.fonk2(b9.fonk4())
            b9.fonk2(b18)
            b5 = b5.fonk5()
    def fonk27(self):
        b13 = self.fonk23()
        b13.fonk26()
        b19 = class2()
        for b1 in b13:
            b19.fonk8(b1)
        return b19
b20 = class2()
b20.fonk7(5)
b20.fonk7(4)
b20.fonk7(3)
b20.fonk7(2)
b20.fonk7(1)
b20.fonk9()
b20.fonk8(12)
b20.fonk8(13)
b20.fonk8(3)
b20.fonk9()
print(b20.fonk10())
print(b20.fonk11(3))
print(b20.fonk17(5))
print(b20.fonk12(12))
b20.fonk20(2)
b20.fonk9()
print(b20.fonk13())
print(b20.fonk14())
print(b20.fonk15(31))
b20.fonk9()
print(b20.fonk16())
b20.fonk9()
b21 = b20.fonk18()
b21.fonk9()
b21.fonk19()
b21.fonk9()
print(b20.fonk21(","))
print(b20.fonk22(3))
b22 = b20.fonk23()
print(b22)
b23 = b20.fonk24()
print(b23)
b20.fonk25()
b20.fonk9()
b24 = b20.fonk27()
b24.fonk9()
b20.fonk26()
b20.fonk9()
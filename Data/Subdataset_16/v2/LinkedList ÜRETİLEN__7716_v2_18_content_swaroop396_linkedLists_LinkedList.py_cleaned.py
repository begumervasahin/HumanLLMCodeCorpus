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
        b4 = class1(b1)
        if not self.b3:
            self.b3 = b4
            return
        b5 = self.b3
        while b5.fonk5():
            b5 = b5.fonk5()
        b5.fonk3(b4)
    def fonk9(self):
        b5 = self.b3
        if not b5:
            print("Empty List!!!")
            return
        while b5:
            print(b5.fonk4(), b6 = " ")
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
            b5 = b5.fonk5()
            a2 += 1
        return -1
    def fonk12(self, item):
        b5 = self.b3
        b7 = None
        b8 = False
        while b5 and not b8:
            if b5.fonk4() == item:
                b8 = True
            else:
                b7 = b5
                b5 = b5.fonk5()
        if b8:
            if b7 is None:
                self.b3 = b5.fonk5()
            else:
                b7.fonk3(b5.fonk5())
        return b8
    def fonk13(self):
        if not self.b3:
            return None
        b5 = self.b3
        b9 = b5.fonk4()
        while b5:
            if b5.fonk4() > b9:
                b9 = b5.fonk4()
            b5 = b5.fonk5()
        return b9
    def fonk14(self):
        if not self.b3:
            return None
        b5 = self.b3
        b10 = b5.fonk4()
        while b5:
            if b5.fonk4() < b10:
                b10 = b5.fonk4()
            b5 = b5.fonk5()
        return b10
    def fonk15(self, b1):
        self.fonk8(b1)
        return True
    def fonk16(self):
        if not self.b3:
            return None
        b5 = self.b3
        b7 = None
        while b5.fonk5():
            b7 = b5
            b5 = b5.fonk5()
        if b7:
            b7.fonk3(None)
        else:
            self.b3 = None
        return b5.fonk4()
    def fonk17(self, a2):
        if a2 < 0 or not self.b3:
            return None
        b5 = self.b3
        for _ in range(a2):
            if not b5.fonk5():
                return None
            b5 = b5.fonk5()
        return b5.fonk4()
    def fonk18(self):
        b11 = class2()
        b5 = self.b3
        while b5:
            b11.fonk8(b5.fonk4())
            b5 = b5.fonk5()
        return b11
    def fonk19(self):
        self.b3 = None
        return True
    def fonk20(self, a2):
        b1 = self.fonk17(a2)
        if b1 is not None:
            self.fonk12(b1)
        return b1
    def fonk21(self, b12 = ""):
        b5 = self.b3
        b13 = ""
        while b5:
            b13 += str(b5.fonk4())
            b5 = b5.fonk5()
            if b5:
                b13 += b12
        return b13
    def fonk22(self, element):
        b5 = self.b3
        a3 = 0
        while b5:
            if b5.fonk4() == element:
                a3 += 1
            b5 = b5.fonk5()
        return a3
    def fonk23(self):
        b5 = self.b3
        b13 = []
        while b5:
            b13.append(b5.fonk4())
            b5 = b5.fonk5()
        return b13
    def fonk24(self):
        b5 = self.b3
        b13 = set()
        while b5:
            b13.add(b5.fonk4())
            b5 = b5.fonk5()
        return b13
    def fonk25(self):
        b7 = None
        b5 = self.b3
        while b5:
            b14 = b5.fonk5()
            b5.fonk3(b7)
            b7 = b5
            b5 = b14
        self.b3 = b7
    def fonk26(self):
        if not self.b3 or not self.b3.fonk5():
            return
        b15 = None
        b5 = self.b3
        while b5:
            b14 = b5.fonk5()
            b15 = self.fonk27(b15, b5)
            b5 = b14
        self.b3 = b15
    def fonk27(self, b3, node):
        if not b3 or b3.fonk4() >= node.fonk4():
            node.fonk3(b3)
            return node
        b5 = b3
        while b5.fonk5() and b5.fonk5().fonk4() < node.fonk4():
            b5 = b5.fonk5()
        node.fonk3(b5.fonk5())
        b5.fonk3(node)
        return b3
    def fonk28(self):
        b11 = self.fonk18()
        b11.fonk26()
        return b11
if b16 = = "__main__":
    b17 = class2()
    b17.fonk7(5)
    b17.fonk7(4)
    b17.fonk7(3)
    b17.fonk7(2)
    b17.fonk7(1)
    b17.fonk9()
    b17.fonk8(12)
    b17.fonk8(13)
    b17.fonk8(3)
    b17.fonk9()
    print("Length:", b17.fonk10())
    print("Index of 3:", b17.fonk11(3))
    print("Element at index 5:", b17.fonk17(5))
    print("Removing 12:", b17.fonk12(12))
    b17.fonk20(2)
    b17.fonk9()
    print("Max:", b17.fonk13())
    print("Min:", b17.fonk14())
    print("Pushing 31:", b17.fonk15(31))
    b17.fonk9()
    print("Popping:", b17.fonk16())
    b17.fonk9()
    b18 = b17.fonk18()
    print("Copied list:")
    b18.fonk9()
    b18.fonk19()
    print("Cleared copied list:")
    b18.fonk9()
    print("List to string:", b17.fonk21(", "))
    print("Count of 3:", b17.fonk22(3))
    b11 = b17.fonk23()
    print("List:", b11)
    b19 = b17.fonk24()
    print("Set:", b19)
    b17.fonk25()
    print("Reversed list:")
    b17.fonk9()
    b20 = b17.fonk28()
    print("Sorted copy of list:")
    b20.fonk9()
    b17.fonk26()
    print("Sorted list:")
    b17.fonk9()
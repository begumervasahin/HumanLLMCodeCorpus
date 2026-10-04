class class1:
    def fonk1(self):
        self.b1 = None
    def fonk2(self, b10):
        b2 = class2(b10)
        b2.fonk26(self.b1)
        self.b1 = b2
    def fonk3(self, b10):
        if not self.b1:
            self.b1 = class2(b10)
            return
        b3 = self.b1
        while b3.fonk28():
            b3 = b3.fonk28()
        b3.fonk26(class2(b10))
    def fonk4(self):
        b3 = self.b1
        if not b3:
            print("Empty List!!!")
            return
        while b3:
            print(b3.fonk27(), b4 = " ")
            b3 = b3.fonk28()
            if b3:
                print("-->", b4 = " ")
        print()
    def fonk5(self):
        b3 = self.b1
        a1 = 0
        while b3:
            a1 += 1
            b3 = b3.fonk28()
        return a1
    def fonk6(self, b10):
        b3 = self.b1
        a2 = 0
        while b3:
            if b3.fonk27() == b10:
                return a2
            b3 = b3.fonk28()
            a2 += 1
        return -1
    def fonk7(self, item):
        b3 = self.b1
        b5 = None
        b6 = False
        while b3 and not b6:
            if b3.fonk27() == item:
                b6 = True
            else:
                b5 = b3
                b3 = b3.fonk28()
        if b6:
            if b5 is None:
                self.b1 = b3.fonk28()
            else:
                b5.fonk26(b3.fonk28())
        return b6
    def fonk8(self):
        if not self.b1:
            return None
        b3 = self.b1
        b7 = b3.fonk27()
        while b3:
            if b3.fonk27() > b7:
                b7 = b3.fonk27()
            b3 = b3.fonk28()
        return b7
    def fonk9(self):
        if not self.b1:
            return None
        b3 = self.b1
        b8 = b3.fonk27()
        while b3:
            if b3.fonk27() < b8:
                b8 = b3.fonk27()
            b3 = b3.fonk28()
        return b8
    def fonk10(self, b10):
        self.fonk3(b10)
        return True
    def fonk11(self):
        if not self.b1:
            return None
        b3 = self.b1
        b5 = None
        while b3.fonk28():
            b5 = b3
            b3 = b3.fonk28()
        if b5:
            b5.fonk26(None)
        else:
            self.b1 = None
        return b3.fonk27()
    def fonk12(self, a2):
        if a2 < 0 or not self.b1:
            return None
        b3 = self.b1
        for _ in range(a2):
            if not b3.fonk28():
                return None
            b3 = b3.fonk28()
        return b3.fonk27()
    def fonk13(self):
        b9 = class1()
        b3 = self.b1
        while b3:
            b9.fonk3(b3.fonk27())
            b3 = b3.fonk28()
        return b9
    def fonk14(self):
        self.b1 = None
        return True
    def fonk15(self, a2):
        b10 = self.fonk12(a2)
        if b10 is not None:
            self.fonk7(b10)
        return b10
    def fonk16(self, b11 = ""):
        b3 = self.b1
        b12 = ""
        while b3:
            b12 += str(b3.fonk27())
            b3 = b3.fonk28()
            if b3:
                b12 += b11
        return b12
    def fonk17(self, element):
        b3 = self.b1
        a3 = 0
        while b3:
            if b3.fonk27() == element:
                a3 += 1
            b3 = b3.fonk28()
        return a3
    def fonk18(self):
        b3 = self.b1
        b13 = []
        while b3:
            b13.append(b3.fonk27())
            b3 = b3.fonk28()
        return b13
    def fonk19(self):
        b3 = self.b1
        b14 = set()
        while b3:
            b14.add(b3.fonk27())
            b3 = b3.fonk28()
        return b14
    def fonk20(self):
        b5 = None
        b15 = self.b1
        while b15:
            b16 = b15.fonk28()
            b15.fonk26(b5)
            b5 = b15
            b15 = b16
        self.b1 = b5
    def fonk21(self):
        if not self.b1 or not self.b1.fonk28():
            return
        b17 = None
        b15 = self.b1
        while b15:
            b16 = b15.fonk28()
            b17 = self.fonk22(b17, b15)
            b15 = b16
        self.b1 = b17
    def fonk22(self, b1, node):
        if not b1 or b1.fonk27() >= node.fonk27():
            node.fonk26(b1)
            return node
        b15 = b1
        while b15.fonk28() and b15.fonk28().fonk27() < node.fonk27():
            b15 = b15.fonk28()
        node.fonk26(b15.fonk28())
        b15.fonk26(node)
        return b1
    def fonk23(self):
        b18 = self.fonk13()
        b18.fonk21()
        return b18
class class2:
    def fonk24(self, b10 = None, b19=None):
        self.b10 = b10
        self.b19 = b19
    def fonk25(self, b10):
        self.b10 = b10
    def fonk26(self, node):
        self.b19 = node
    def fonk27(self):
        return self.b10
    def fonk28(self):
        return self.b19
b20 = class1()
b20.fonk2(5)
b20.fonk2(4)
b20.fonk2(3)
b20.fonk2(2)
b20.fonk2(1)
b20.fonk4()
b20.fonk3(12)
b20.fonk3(13)
b20.fonk3(3)
b20.fonk4()
print("Length:", b20.fonk5())
print("Index of 3:", b20.fonk6(3))
print("Element at index 5:", b20.fonk12(5))
print("Removing 12:", b20.fonk7(12))
b20.fonk15(2)
b20.fonk4()
print("Max:", b20.fonk8())
print("Min:", b20.fonk9())
print("Pushing 31:", b20.fonk10(31))
b20.fonk4()
print("Popping:", b20.fonk11())
b20.fonk4()
b21 = b20.fonk13()
print("Copied list:")
b21.fonk4()
b21.fonk14()
print("Cleared copied list:")
b21.fonk4()
print("List to string:", b20.fonk16(", "))
print("Count of 3:", b20.fonk17(3))
b22 = b20.fonk18()
print("List:", b22)
b23 = b20.fonk19()
print("Set:", b23)
b20.fonk20()
print("Reversed list:")
b20.fonk4()
b24 = b20.fonk23()
print("Sorted copy of list:")
b24.fonk4()
b20.fonk21()
print("Sorted list:")
b20.fonk4()
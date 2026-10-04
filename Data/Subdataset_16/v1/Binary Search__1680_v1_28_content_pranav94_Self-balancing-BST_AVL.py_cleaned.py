
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, b1):
        if not self.b4:
            self.b4 = class1(b1)
        else:
            self.fonk4(self.b4, b1)
    def fonk4(self, b6, b1):
        if b1 < b6.b1:
            if b6.b2 is None:
                b6.b2 = class1(b1)
            else:
                self.fonk4(b6.b2, b1)
        else:
            if b6.b3 is None:
                b6.b3 = class1(b1)
            else:
                self.fonk4(b6.b3, b1)
    def fonk5(self, b1):
        self.b4 = self.fonk6(self.b4, b1)
    def fonk6(self, b6, b1):
        if not b6:
            return None
        if b1 < b6.b1:
            b6.b2 = self.fonk6(b6.b2, b1)
        elif b1 > b6.b1:
            b6.b3 = self.fonk6(b6.b3, b1)
        else:
            if not b6.b2:
                return b6.b3
            if not b6.b3:
                return b6.b2
            b5 = self.fonk7(b6.b3)
            b6.b1 = b5.b1
            b6.b3 = self.fonk6(b6.b3, b5.b1)
        return b6
    def fonk7(self, b6):
        while b6.b2 is not None:
            b6 = b6.b2
        return b6
    def fonk8(self, b1):
        return self.fonk9(self.b4, b1)
    def fonk9(self, b6, b1):
        if b6 is None or b6.b1 = = b1:
            return b6
        if b1 < b6.b1:
            return self.fonk9(b6.b2, b1)
        return self.fonk9(b6.b3, b1)
    def fonk10(self):
        return self.fonk11(self.b4)
    def fonk11(self, b6):
        b7 = []
        if b6:
            b7 = self.fonk11(b6.b2)
            b7.append(b6.b1)
            b7 = b7 + self.fonk11(b6.b3)
        return b7
from class2 import class2
from class1 import class1
class class3(class1):
    def fonk12(self, b1):
        self.a1 = 0
        super().fonk12(b1)
class class4(class2):
    def fonk13(self, b6):
        b8 = b6.b3
        b6.b3 = b8.b2
        b8.b2 = b6
        self.fonk20(b6)
        self.fonk20(b8)
        return b8
    def fonk14(self, b6):
        b8 = b6.b2
        b6.b2 = b8.b3
        b8.b3 = b6
        self.fonk20(b6)
        self.fonk20(b8)
        return b8
    def fonk15(self, b6):
        b9 = self.fonk22(b6)
        if b9 > 1:
            if self.fonk22(b6.b2) < 0:
                b6.b2 = self.fonk13(b6.b2)
            return self.fonk14(b6)
        if b9 < -1:
            if self.fonk22(b6.b3) > 0:
                b6.b3 = self.fonk14(b6.b3)
            return self.fonk13(b6)
        return b6
    def fonk16(self, b6, b1):
        if not b6:
            return class3(b1)
        if b1 < b6.b1:
            b6.b2 = self.fonk16(b6.b2, b1)
        else:
            b6.b3 = self.fonk16(b6.b3, b1)
        self.fonk20(b6)
        return self.fonk15(b6)
    def fonk17(self, b1):
        self.b4 = self.fonk16(self.b4, b1)
    def fonk18(self, b6, b1):
        if not b6:
            return None
        if b1 < b6.b1:
            b6.b2 = self.fonk18(b6.b2, b1)
        elif b1 > b6.b1:
            b6.b3 = self.fonk18(b6.b3, b1)
        else:
            if not b6.b2 and not b6.b3:
                return None
            if not b6.b2:
                return b6.b3
            if not b6.b3:
                return b6.b2
            b5 = self.fonk7(b6.b3)
            b6.b1 = b5.b1
            b6.b3 = self.fonk18(b6.b3, b5.b1)
        self.fonk20(b6)
        return self.fonk15(b6)
    def fonk19(self, b1):
        self.b4 = self.fonk18(self.b4, b1)
    def fonk20(self, b6):
        b6.a1 = 1 + max(self.fonk21(b6.b2), self.fonk21(b6.b3))
    @staticmethod
    def fonk21(b6):
        if not b6:
            return 0
        return b6.a1
    def fonk22(self, b6):
        return self.fonk21(b6.b2) - self.fonk21(b6.b3)
if b10 = = "__main__":
    b11 = class4()
    b12 = [10, 20, 30, 40, 50, 25]
    for value in b12:
        b11.fonk17(value)
    print("In-order traversal after insertions:", b11.fonk10())
    b11.fonk19(40)
    print("In-order traversal after deleting 40:", b11.fonk10())
    print("Root b9:", b11.fonk22(b11.b4))
    print("Root a1:", b11.b4.a1)
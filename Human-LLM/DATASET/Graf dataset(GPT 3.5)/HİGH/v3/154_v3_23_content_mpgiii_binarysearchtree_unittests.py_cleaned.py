class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self, b4 = None):
        self.b5 = None
        if b4:
            for item in b4:
                self.fonk3(item)
    def fonk3(self, b1):
        if not self.b5:
            self.b5 = class1(b1)
        else:
            self.fonk4(self.b5, b1)
    def fonk4(self, b7, b1):
        if b1 < b7.b1:
            if not b7.b2:
                b7.b2 = class1(b1)
            else:
                self.fonk4(b7.b2, b1)
        elif b1 > b7.b1:
            if not b7.b3:
                b7.b3 = class1(b1)
            else:
                self.fonk4(b7.b3, b1)
    def fonk5(self, b1):
        self.b5 = self.fonk6(self.b5, b1)
    def fonk6(self, b7, b1):
        if not b7:
            return None
        if b1 < b7.b1:
            b7.b2 = self.fonk6(b7.b2, b1)
        elif b1 > b7.b1:
            b7.b3 = self.fonk6(b7.b3, b1)
        else:
            if not b7.b2 and not b7.b3:
                return None
            if not b7.b2:
                return b7.b3
            if not b7.b3:
                return b7.b2
            b6 = self.fonk7(b7.b3)
            b7.b1 = b6
            b7.b3 = self.fonk6(b7.b3, b6)
        return b7
    def fonk7(self, b7):
        while b7.b2:
            b7 = b7.b2
        return b7.b1
    def fonk8(self):
        return self.fonk9(self.b5, [])
    def fonk9(self, b7, b8):
        if b7:
            self.fonk9(b7.b2, b8)
            b8.append(b7.b1)
            self.fonk9(b7.b3, b8)
        return b8
    def fonk10(self):
        return self.fonk11(self.b5, [])
    def fonk11(self, b7, b8):
        if b7:
            b8.append(b7.b1)
            self.fonk11(b7.b2, b8)
            self.fonk11(b7.b3, b8)
        return b8
    def fonk12(self):
        return self.fonk13(self.b5, [])
    def fonk13(self, b7, b8):
        if b7:
            self.fonk13(b7.b2, b8)
            self.fonk13(b7.b3, b8)
            b8.append(b7.b1)
        return b8
    def fonk14(self):
        if not self.b5:
            return []
        b8 = []
        b9 = [self.b5]
        while b9:
            b7 = b9.pop(0)
            b8.append(b7.b1)
            if b7.b2:
                b9.append(b7.b2)
            if b7.b3:
                b9.append(b7.b3)
        return b8
    def fonk15(self, b1):
        return self.fonk16(self.b5, b1)
    def fonk16(self, b7, b1):
        if not b7:
            return False
        if b1 = = b7.b1:
            return True
        elif b1 < b7.b1:
            return self.fonk16(b7.b2, b1)
        else:
            return self.fonk16(b7.b3, b1)
import unittest
class class3(unittest.TestCase):
    def fonk17(self):
        b10 = class2(b4=[0, 1, 2, 5, 90, -1])
        self.assertListEqual(b10.fonk8(), [-1, 0, 1, 2, 5, 90])
        self.assertListEqual(b10.fonk10(), [0, -1, 1, 2, 5, 90])
        self.assertListEqual(b10.fonk12(), [-1, 2, 1, 90, 5, 0])
        self.assertListEqual(b10.fonk14(), [0, -1, 1, 2, 5, 90])
    def fonk18(self):
        b10 = class2(b4=[0, -1, 1])
        self.assertListEqual(b10.fonk8(), [-1, 0, 1])
    def fonk19(self):
        b10 = class2(b4=[2, 0, 1])
        self.assertListEqual(b10.fonk10(), [2, 0, 1])
    def fonk20(self):
        b10 = class2(b4=[2, 0, 1])
        self.assertListEqual(b10.fonk12(), [1, 0, 2])
    def fonk21(self):
        b10 = class2(b4=[2, 0, 1, 6, 10])
        self.assertListEqual(b10.fonk14(), [2, 0, 6, 1, 10])
    def fonk22(self):
        b10 = class2()
        b10.fonk3(0)
        b10.fonk3(-1)
        b10.fonk3(1)
        self.assertListEqual(b10.fonk8(), [-1, 0, 1])
    def fonk23(self):
        b10 = class2(b4=[0, 1, 2])
        b10.fonk5(0)
        self.assertListEqual(b10.fonk8(), [1, 2])
    def fonk24(self):
        b10 = class2(b4=[0, 1, 2])
        self.assertTrue(0 in b10)
        b10.fonk5(0)
        self.assertFalse(0 in b10)
if b11 = = '__main__':
    unittest.main()
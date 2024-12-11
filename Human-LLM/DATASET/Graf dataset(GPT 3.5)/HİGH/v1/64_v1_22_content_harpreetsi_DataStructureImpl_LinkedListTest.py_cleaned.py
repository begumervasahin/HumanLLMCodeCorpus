class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = class1()
    def fonk3(self, b1):
        b4 = class1(b1)
        b4.b2 = self.b3.b2
        self.b3.b2 = b4
        return b4
    def fonk4(self, b1):
        b4 = class1(b1)
        b5 = self.b3
        while b5.b2 is not None:
            b5 = b5.b2
        b5.b2 = b4
        return b4
    def fonk5(self, b1, b6):
        if b6 <= 0:
            return "Invalid b6, it can not be less than or equal to 0"
        if b6 = = 1:
            return self.fonk3(b1)
        b5 = self.b3
        for _ in range(b6 - 1):
            if b5.b2 is None:
                return "Invalid b6, it exceeds the size of the linked list"
            b5 = b5.b2
        b4 = class1(b1)
        b4.b2 = b5.b2
        b5.b2 = b4
        return b4
    def fonk6(self):
        if self.b3.b2 is None:
            return "List is empty, nothing to remove"
        b7 = self.b3.b2
        self.b3.b2 = b7.b2
        return b7
    def fonk7(self):
        if self.b3.b2 is None:
            return "List is empty, nothing to remove"
        b5 = self.b3
        while b5.b2.b2 is not None:
            b5 = b5.b2
        b7 = b5.b2
        b5.b2 = None
        return b7
    def fonk8(self, b6):
        if b6 <= 0:
            return "Invalid b6, it can not be less than or equal to 0"
        if b6 = = 1:
            return self.fonk6()
        b5 = self.b3
        for _ in range(b6 - 1):
            if b5.b2 is None:
                return "Invalid b6, it exceeds the size of the linked list"
            b5 = b5.b2
        b7 = b5.b2
        b5.b2 = b5.b2.b2
        return b7
    def fonk9(self):
        if self.b3.b2 is None:
            return "List is empty, nothing to reverse"
        b8 = None
        b5 = self.b3.b2
        while b5 is not None:
            b9 = b5.b2
            b5.b2 = b8
            b8 = b5
            b5 = b9
        self.b3.b2 = b8
        return b8
    def fonk10(self, b5):
        if b5.b2 is None:
            return b5
        b10 = self.fonk10(b5.b2)
        b5.b2.b2 = b5
        b5.b2 = None
        return b10
import unittest
class class3(unittest.TestCase):
    def fonk11(self):
        b11 = class2()
        b11.fonk3(10)
        self.assertEqual(b11.fonk3(20).b1, 20)
    def fonk12(self):
        b11 = class2()
        b11.fonk3(10)
        b11.fonk3(20)
        self.assertEqual(b11.fonk3(30).b1, 30)
    def fonk13(self):
        b11 = class2()
        self.assertEqual(b11.fonk4(500).b1, 500)
    def fonk14(self):
        b11 = class2()
        b11.fonk4(10)
        b11.fonk4(20)
        b12 = b11.b3.b2
        self.assertEqual(b12.b1, 20)
if b13 = = '__main__':
    unittest.main()
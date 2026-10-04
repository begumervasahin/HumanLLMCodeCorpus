class class1:
    def fonk1(self, size):
        self.b1 = [None] * size
        self.b2 = size
        self.a1 = -1
    def fonk2(self, b3):
        if self.a1 >= self.b2 - 1:
            return "class1 full"
        self.a1 += 1
        self.b1[self.a1] = b3
        return "success"
    def fonk3(self):
        if self.a1 = = -1:
            return "class1 empty"
        b3 = self.b1[self.a1]
        self.b1[self.a1] = None
        self.a1 -= 1
        return b3
    def fonk4(self):
        if self.a1 = = -1:
            return "class1 empty"
        return self.b1[self.a1]
    def fonk5(self):
        return self.a1 = = -1
    def fonk6(self):
        if self.a1 = = -1:
            print("class1 is empty")
        else:
            for i in range(self.a1, -1, -1):
                print(self.b1[i])
import unittest
class class2(unittest.TestCase):
    def fonk7(self):
        b1 = class1(10)
        self.assertEqual(b1.fonk2(5), "success")
    def fonk8(self):
        b1 = class1(3)
        b1.fonk2(5)
        b1.fonk2(5)
        b1.fonk2(5)
        self.assertEqual(b1.fonk2(5), "class1 full")
    def fonk9(self):
        b1 = class1(10)
        b1.fonk2(10)
        self.assertEqual(b1.fonk4(), 10)
    def fonk10(self):
        b1 = class1(10)
        self.assertEqual(b1.fonk4(), "class1 empty")
    def fonk11(self):
        b1 = class1(10)
        b1.fonk2(10)
        self.assertEqual(b1.fonk3(), 10)
    def fonk12(self):
        b1 = class1(10)
        self.assertEqual(b1.fonk3(), "class1 empty")
    def fonk13(self):
        b1 = class1(10)
        self.assertTrue(b1.fonk5())
    def fonk14(self):
        b1 = class1(10)
        b1.fonk2(10)
        self.assertFalse(b1.fonk5())
    def fonk15(self):
        b1 = class1(10)
        b1.fonk6()
    def fonk16(self):
        b1 = class1(10)
        b1.fonk2(10)
        b1.fonk2(20)
        b1.fonk6()
if b4 = = '__main__':
    unittest.main()
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, item):
        if len(self.b2) < self.b1:
            self.b2.append(item)
            return "success"
        else:
            return "class1 full"
    def fonk3(self):
        if self.fonk5():
            return "class1 empty"
        else:
            return self.b2.fonk3()
    def fonk4(self):
        if self.fonk5():
            return "class1 empty"
        else:
            return self.b2[-1]
    def fonk5(self):
        return len(self.b2) == 0
    def fonk6(self):
        if self.fonk5():
            fonk6("class1 empty")
        else:
            fonk6("class1:", self.b2)
import unittest
class class2(unittest.TestCase):
    def fonk7(self):
        b3 = class1(10)
        self.assertEqual(b3.fonk2(5), "success")
    def fonk8(self):
        b3 = class1(3)
        b3.fonk2(5)
        b3.fonk2(5)
        b3.fonk2(5)
        self.assertEqual(b3.fonk2(5), "class1 full")
    def fonk9(self):
        b3 = class1(10)
        b3.fonk2(10)
        self.assertEqual(b3.fonk4(), 10)
    def fonk10(self):
        b3 = class1(10)
        self.assertEqual(b3.fonk4(), "class1 empty")
    def fonk11(self):
        b3 = class1(10)
        b3.fonk2(10)
        self.assertEqual(b3.fonk3(), 10)
    def fonk12(self):
        b3 = class1(10)
        self.assertEqual(b3.fonk3(), "class1 empty")
    def fonk13(self):
        b3 = class1(10)
        self.assertTrue(b3.fonk5())
    def fonk14(self):
        b3 = class1(10)
        b3.fonk2(10)
        self.assertFalse(b3.fonk5())
    def fonk15(self):
        b3 = class1(10)
        b3.fonk6()
    def fonk16(self):
        b3 = class1(10)
        b3.fonk2(10)
        b3.fonk2(20)
        b3.fonk6()
if b4 = = '__main__':
    unittest.main()
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
        return self.b2[-1] if self.b2 else "class1 empty"
    def fonk5(self):
        return not self.b2
    def fonk6(self):
        print("class1:", self.b2 if self.b2 else "class1 empty")
import unittest
class class2(unittest.TestCase):
    def fonk7(self):
        self.b1 = 10
        self.b3 = class1(self.b1)
    def fonk8(self):
        self.assertEqual(self.b3.fonk2(5), "success")
    def fonk9(self):
        for _ in range(self.b1):
            self.b3.fonk2(5)
        self.assertEqual(self.b3.fonk2(5), "class1 full")
    def fonk10(self):
        self.b3.fonk2(10)
        self.assertEqual(self.b3.fonk4(), 10)
    def fonk11(self):
        self.assertEqual(self.b3.fonk4(), "class1 empty")
    def fonk12(self):
        self.b3.fonk2(10)
        self.assertEqual(self.b3.fonk3(), 10)
    def fonk13(self):
        self.assertEqual(self.b3.fonk3(), "class1 empty")
    def fonk14(self):
        self.assertTrue(self.b3.fonk5())
    def fonk15(self):
        self.b3.fonk2(10)
        self.assertFalse(self.b3.fonk5())
    def fonk16(self):
        self.b3.fonk6()
    def fonk17(self):
        self.b3.fonk2(10)
        self.b3.fonk2(20)
        self.b3.fonk6()
if b4 = = '__main__':
    unittest.main()
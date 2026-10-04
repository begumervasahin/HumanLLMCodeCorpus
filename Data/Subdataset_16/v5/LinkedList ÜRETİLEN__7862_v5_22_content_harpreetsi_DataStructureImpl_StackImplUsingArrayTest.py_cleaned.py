import unittest
from StackImplUsingArray import Stack
class class1(unittest.TestCase):
    def fonk1(self):
        self.a1 = 10
        self.b1 = Stack(self.a1)
    def fonk2(self):
        self.assertEqual(self.b1.push(5), "success")
    def fonk3(self):
        b2 = Stack(3)
        b2.push(5)
        b2.push(5)
        b2.push(5)
        self.assertEqual(b2.push(5), "Stack full")
    def fonk4(self):
        self.b1.push(10)
        self.assertEqual(self.b1.topElement(), 10)
    def fonk5(self):
        self.assertEqual(self.b1.topElement(), "Stack empty")
    def fonk6(self):
        self.b1.push(10)
        self.assertEqual(self.b1.pop(), 10)
    def fonk7(self):
        self.assertEqual(self.b1.pop(), "Stack empty")
    def fonk8(self):
        self.assertTrue(self.b1.isEmpty())
    def fonk9(self):
        self.b1.push(10)
        self.assertFalse(self.b1.isEmpty())
    def fonk10(self):
        try:
            self.b1.print()
            b3 = "No exception"
        except Exception as e:
            b3 = str(e)
        self.assertEqual(b3, "No exception")
    def fonk11(self):
        self.b1.push(10)
        self.b1.push(20)
        try:
            self.b1.print()
            b3 = "No exception"
        except Exception as e:
            b3 = str(e)
        self.assertEqual(b3, "No exception")
if b4 = = '__main__':
    unittest.main()
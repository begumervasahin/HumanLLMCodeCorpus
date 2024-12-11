from StackImplUsingArray import Stack
import unittest
class class1(unittest.TestCase):
    def fonk1(self):
        b1 = Stack(10)
        self.assertEqual(b1.push(5), "success")
    def fonk2(self):
        b1 = Stack(3)
        b1.push(5)
        b1.push(5)
        b1.push(5)
        self.assertEqual(b1.push(5), "Stack full")
    def fonk3(self):
        b1 = Stack(10)
        b1.push(10)
        self.assertEqual(b1.top_element(), 10)
    def fonk4(self):
        b1 = Stack(10)
        self.assertEqual(b1.top_element(), "Stack empty")
    def fonk5(self):
        b1 = Stack(10)
        b1.push(10)
        self.assertEqual(b1.pop(), 10)
    def fonk6(self):
        b1 = Stack(10)
        self.assertEqual(b1.pop(), "Stack empty")
    def fonk7(self):
        b1 = Stack(10)
        self.assertTrue(b1.is_empty())
    def fonk8(self):
        b1 = Stack(10)
        b1.push(10)
        self.assertFalse(b1.is_empty())
    def fonk9(self):
        b1 = Stack(10)
        b1.print()
    def fonk10(self):
        b1 = Stack(10)
        b1.push(10)
        b1.push(20)
        b1.print()
if b2 = = '__main__':
    unittest.main()
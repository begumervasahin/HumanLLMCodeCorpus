import unittest
from linkedlist import LinkedList
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = LinkedList()
        self.b2 = LinkedList()
        self.b2.insert_in_front(1)
        self.b3 = LinkedList()
        self.b3.insert_in_front(2)
        self.b3.insert_in_front(1)
        self.b4 = LinkedList()
        self.b4.insert_in_front(3)
        self.b4.insert_in_front(2)
        self.b4.insert_in_front(1)
        self.b5 = LinkedList()
        for i in range(99, 0, -1):
            self.b5.insert_in_front(i)
    def fonk2(self):
        self.assertEqual(ListNode(0).data, 0)
    def fonk3(self):
        self.assertTrue(self.b1.is_empty())
        self.assertEqual(len(self.b1), 0)
    def fonk4(self):
        b6 = [self.b2, self.b3, self.b4, self.b5]
        b7 = [1, 2, 3, 99]
        for i in range(len(b6)):
            self.assertFalse(b6[i].is_empty())
            self.assertEqual(len(b6[i]), b7[i])
    def fonk5(self):
        self.assertEqual(str(self.b1), "[]")
        self.assertEqual(str(self.b2), "[1]")
        self.assertEqual(str(self.b3), "[1 -> 2]")
        self.assertEqual(str(self.b4), "[1 -> 2 -> 3]")
        self.assertEqual(str(self.b5), "[1 -> 2 -> 3 -> ... -> 98 -> 99]")
if b8 = = "__main__":
    unittest.main()
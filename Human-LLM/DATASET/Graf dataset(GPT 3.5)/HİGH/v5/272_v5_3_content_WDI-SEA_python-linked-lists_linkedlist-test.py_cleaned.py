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
        b6 = [(self.b2, 1), (self.b3, 2), (self.b4, 3), (self.b5, 99)]
        for test_list, size in b6:
            self.assertFalse(test_list.is_empty())
            self.assertEqual(len(test_list), size)
    def fonk5(self):
        b6 = [
            (self.b1, "[]"),
            (self.b2, "[1]"),
            (self.b3, "[1 -> 2]"),
            (self.b4, "[1 -> 2 -> 3]"),
            (self.b5, "[1 -> 2 -> 3 -> ... -> 98 -> 99]")
        ]
        for test_list, expected_str in b6:
            self.assertEqual(str(test_list), expected_str)
if b7 = = "__main__":
    unittest.main()
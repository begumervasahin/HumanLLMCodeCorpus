import unittest
from linkedlist import LinkedList
class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.empty_list = LinkedList()
        self.l1 = LinkedList()
        self.l1.insert_in_front(1)
        self.l2 = LinkedList()
        self.l2.insert_in_front(2)
        self.l2.insert_in_front(1)
        self.l3 = LinkedList()
        self.l3.insert_in_front(3)
        self.l3.insert_in_front(2)
        self.l3.insert_in_front(1)
        self.l99 = LinkedList()
        for i in range(99, 0, -1):
            self.l99.insert_in_front(i)
    def test_list_node(self):
        self.assertEqual(ListNode(0).data, 0)
    def test_empty_list_is_empty(self):
        self.assertTrue(self.empty_list.is_empty())
        self.assertEqual(len(self.empty_list), 0)
    def test_not_is_empty(self):
        test_data = [(self.l1, 1), (self.l2, 2), (self.l3, 3), (self.l99, 99)]
        for test_list, size in test_data:
            self.assertFalse(test_list.is_empty())
            self.assertEqual(len(test_list), size)
    def test_str_representation(self):
        test_data = [
            (self.empty_list, "[]"),
            (self.l1, "[1]"),
            (self.l2, "[1 -> 2]"),
            (self.l3, "[1 -> 2 -> 3]"),
            (self.l99, "[1 -> 2 -> 3 -> ... -> 98 -> 99]")
        ]
        for test_list, expected_str in test_data:
            self.assertEqual(str(test_list), expected_str)
if __name__ == "__main__":
    unittest.main()
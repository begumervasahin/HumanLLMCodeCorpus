import unittest
from LinkedList import LinkedList
class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.mylist = LinkedList()
    def test_add_at_the_beginning_empty_list(self):
        result = self.mylist.add_at_the_beginning(10)
        self.assertEqual(result.data, 10)
    def test_add_at_the_beginning_non_empty_list(self):
        self.mylist.add_at_the_beginning(10)
        result = self.mylist.add_at_the_beginning(20)
        self.assertEqual(result.data, 20)
    def test_add_at_the_end_empty_list(self):
        result = self.mylist.add_at_the_end(500)
        self.assertEqual(result.data, 500)
    def test_add_at_the_end_non_empty_list(self):
        self.mylist.add_at_the_end(10)
        self.mylist.add_at_the_end(20)
        temp = self.mylist.head.next
        self.assertEqual(temp.data, 20)
    def test_add_at_nth_position_1st_position_non_empty_list(self):
        self.mylist.add_at_the_end(10)
        self.mylist.add_at_the_end(20)
        self.mylist.add_at_the_end(30)
        result = self.mylist.add_at_nth_position(5, 1)
        self.assertEqual(result.data, 5)
    def test_add_at_nth_position_0th_position_invalid(self):
        result = self.mylist.add_at_nth_position(5, 0)
        self.assertEqual(result, "Invalid position, it cannot be less than or equal to 0")
    def test_add_at_nth_position_positive(self):
        self.mylist.add_at_the_end(10)
        self.mylist.add_at_the_end(20)
        self.mylist.add_at_the_end(30)
        self.mylist.add_at_the_end(40)
        result = self.mylist.add_at_nth_position(25, 3)
        self.assertEqual(self.mylist.head.next.next.data, 25)
    def test_add_at_nth_position_invalid_position(self):
        self.mylist.add_at_the_end(10)
        self.mylist.add_at_the_end(20)
        self.mylist.add_at_the_end(30)
        self.mylist.add_at_the_end(40)
        result = self.mylist.add_at_nth_position(50, 6)
        self.assertEqual(result, "Invalid position, it exceeds the size of the linked list")
    def test_remove_at_the_beginning_empty_list(self):
        result = self.mylist.remove_at_the_beginning()
        self.assertEqual(result, "List is empty, nothing to remove")
    def test_remove_at_the_beginning_non_empty_list(self):
        self.mylist.add_at_the_end(10)
        self.mylist.add_at_the_end(20)
        self.mylist.add_at_the_end(30)
        result = self.mylist.remove_at_the_beginning()
        self.assertEqual(result.data, 20)
    def test_remove_at_the_end_empty_list(self):
        result = self.mylist.remove_at_the_end()
        self.assertEqual(result, "List is empty, nothing to remove")
    def test_remove_at_the_end_list_has_one_element(self):
        self.mylist.add_at_the_end(10)
        result = self.mylist.remove_at_the_end()
        self.assertEqual(result, None)
    def test_remove_at_the_end_list_has_more_than_one_elements(self):
        self.mylist.add_at_the_end(10)
        self.mylist.add_at_the_end(20)
        self.mylist.add_at_the_end(30)
        result = self.mylist.remove_at_the_end()
        self.assertEqual(self.mylist.head.next.next, None)
    def test_remove_at_nth_position_0th_position_invalid(self):
        result = self.mylist.remove_at_nth_position(0)
        self.assertEqual(result, "Invalid position, it cannot be less than or equal to 0")
    def test_remove_at_nth_position_1st_position(self):
        self.mylist.add_at_the_end(10)
        self.mylist.add_at_the_end(20)
        result = self.mylist.remove_at_nth_position(1)
        self.assertEqual(result.data, 20)
    def test_remove_at_nth_position_positive(self):
        self.mylist.add_at_the_end(10)
        self.mylist.add_at_the_end(20)
        self.mylist.add_at_the_end(30)
        self.mylist.add_at_the_end(40)
        result = self.mylist.remove_at_nth_position(3)
        self.assertEqual(self.mylist.head.next.next.data, 40)
    def test_remove_at_nth_position_invalid_position(self):
        self.mylist.add_at_the_end(10)
        self.mylist.add_at_the_end(20)
        self.mylist.add_at_the_end(30)
        result = self.mylist.remove_at_nth_position(4)
        self.assertEqual(result, "Invalid position, it exceeds the size of the linked list")
    def test_reverse_empty_list(self):
        result = self.mylist.reverse()
        self.assertEqual(result, "List is empty, nothing to reverse")
    def test_reverse_non_empty_list(self):
        self.mylist.add_at_the_end(10)
        self.mylist.add_at_the_end(20)
        self.mylist.add_at_the_end(30)
        self.mylist.add_at_the_end(40)
        result = self.mylist.reverse()
        self.assertEqual(self.mylist.head.data, 40)
    def test_reverse_one_element_list(self):
        self.mylist.add_at_the_end(10)
        result = self.mylist.reverse()
        self.assertEqual(self.mylist.head.data, 10)
    def test_reverse_using_recursion_empty_list(self):
        result = self.mylist.reverse_using_recursion(self.mylist.head)
        self.assertEqual(result, "List is empty, nothing to reverse")
    def test_reverse_using_recursion_one_element_list(self):
        self.mylist.add_at_the_end(10)
        result = self.mylist.reverse_using_recursion(self.mylist.head)
        self.assertEqual(self.mylist.head.data, 10)
    def test_reverse_using_recursion_non_empty_list(self):
        self.mylist.add_at_the_end(10)
        self.mylist.add_at_the_end(20)
        self.mylist.add_at_the_end(30)
        self.mylist.add_at_the_end(40)
        self.mylist.add_at_the_end(50)
        self.mylist.add_at_the_end(60)
        result = self.mylist.reverse_using_recursion(self.mylist.head)
        self.assertEqual(self.mylist.head.data, 60)
if __name__ == '__main__':
    unittest.main()
import unittest
from LinkedList import LinkedList
class LinkedListTest(unittest.TestCase):
    def test_add_at_the_beginning_empty_list(self):
        mylist = LinkedList()
        result = mylist.add_at_the_beginning(10)
        self.assertEqual(result.data, 10)
    def test_add_at_the_beginning_non_empty_list(self):
        mylist = LinkedList()
        mylist.add_at_the_beginning(10)
        result = mylist.add_at_the_beginning(20)
        self.assertEqual(result.data, 20)
    def test_add_at_the_end_empty_list(self):
        mylist = LinkedList()
        result = mylist.add_at_the_end(500)
        self.assertEqual(result.data, 500)
    def test_add_at_the_end_non_empty_list(self):
        mylist = LinkedList()
        mylist.add_at_the_end(10)
        mylist.add_at_the_end(20)
        temp = mylist.head.next
        self.assertEqual(temp.data, 20)
    def test_add_at_nth_position_1st_position_non_empty_list(self):
        mylist = LinkedList()
        mylist.add_at_the_end(10)
        mylist.add_at_the_end(20)
        mylist.add_at_the_end(30)
        result = mylist.add_at_nth_position(5, 1)
        self.assertEqual(result.data, 5)
    def test_add_at_nth_position_0th_position_invalid(self):
        mylist = LinkedList()
        result = mylist.add_at_nth_position(5, 0)
        self.assertEqual(result, "Invalid position, it cannot be less than or equal to 0")
    def test_add_at_nth_position_positive(self):
        mylist = LinkedList()
        mylist.add_at_the_end(10)
        mylist.add_at_the_end(20)
        mylist.add_at_the_end(30)
        mylist.add_at_the_end(40)
        result = mylist.add_at_nth_position(25, 3)
        self.assertEqual(result.next.next.data, 25)
    def test_add_at_nth_position_invalid_position(self):
        mylist = LinkedList()
        mylist.add_at_the_end(10)
        mylist.add_at_the_end(20)
        mylist.add_at_the_end(30)
        mylist.add_at_the_end(40)
        result = mylist.add_at_nth_position(50, 6)
        self.assertEqual(result, "Invalid position, it exceeds the size of the linked list")
    def test_remove_at_the_beginning_empty_list(self):
        mylist = LinkedList()
        result = mylist.remove_at_the_beginning()
        self.assertEqual(result, "List is empty, nothing to remove")
    def test_remove_at_the_beginning_non_empty_list(self):
        mylist = LinkedList()
        mylist.add_at_the_end(10)
        mylist.add_at_the_end(20)
        mylist.add_at_the_end(30)
        result = mylist.remove_at_the_beginning()
        self.assertEqual(result.data, 20)
    def test_remove_at_the_end_empty_list(self):
        mylist = LinkedList()
        result = mylist.remove_at_the_end()
        self.assertEqual(result, "List is empty, nothing to remove")
    def test_remove_at_the_end_list_has_one_element(self):
        mylist = LinkedList()
        mylist.add_at_the_end(10)
        result = mylist.remove_at_the_end()
        self.assertEqual(result, None)
    def test_remove_at_the_end_list_has_more_than_one_elements(self):
        mylist = LinkedList()
        mylist.add_at_the_end(10)
        mylist.add_at_the_end(20)
        mylist.add_at_the_end(30)
        result = mylist.remove_at_the_end()
        self.assertEqual(result.next.data, 20)
    def test_remove_at_nth_position_0th_position_invalid(self):
        mylist = LinkedList()
        result = mylist.remove_at_nth_position(0)
        self.assertEqual(result, "Invalid position, it cannot be less than or equal to 0")
    def test_remove_at_nth_position_1st_position(self):
        mylist = LinkedList()
        mylist.add_at_the_end(10)
        mylist.add_at_the_end(20)
        result = mylist.remove_at_nth_position(1)
        self.assertEqual(result.data, 20)
    def test_remove_at_nth_position_positive(self):
        mylist = LinkedList()
        mylist.add_at_the_end(10)
        mylist.add_at_the_end(20)
        mylist.add_at_the_end(30)
        mylist.add_at_the_end(40)
        result = mylist.remove_at_nth_position(3)
        self.assertEqual(result.next.next.data, 40)
    def test_remove_at_nth_position_invalid_position(self):
        mylist = LinkedList()
        mylist.add_at_the_end(10)
        mylist.add_at_the_end(20)
        mylist.add_at_the_end(30)
        result = mylist.remove_at_nth_position(4)
        self.assertEqual(result, "Invalid position, it exceeds the size of the linked list")
    def test_reverse_empty_list(self):
        mylist = LinkedList()
        result = mylist.reverse()
        self.assertEqual(result, "List is empty, nothing to reverse")
    def test_reverse_non_empty_list(self):
        mylist = LinkedList()
        mylist.add_at_the_end(10)
        mylist.add_at_the_end(20)
        mylist.add_at_the_end(30)
        mylist.add_at_the_end(40)
        result = mylist.reverse()
        self.assertEqual(result.data, 40)
    def test_reverse_one_element_list(self):
        mylist = LinkedList()
        mylist.add_at_the_end(10)
        result = mylist.reverse()
        self.assertEqual(result.data, 10)
    def test_reverse_using_recursion_empty_list(self):
        mylist = LinkedList()
        result = mylist.reverse_using_recursion(mylist.head)
        self.assertEqual(result, "List is empty, nothing to reverse")
    def test_reverse_using_recursion_one_element_list(self):
        mylist = LinkedList()
        mylist.add_at_the_end(10)
        result = mylist.reverse_using_recursion(mylist.head)
        self.assertEqual(result.data, 10)
    def test_reverse_using_recursion_non_empty_list(self):
        mylist = LinkedList()
        mylist.add_at_the_end(10)
        mylist.add_at_the_end(20)
        mylist.add_at_the_end(30)
        mylist.add_at_the_end(40)
        mylist.add_at_the_end(50)
        mylist.add_at_the_end(60)
        result = mylist.reverse_using_recursion(mylist.head)
        self.assertEqual(result.data, 60)
if __name__ == '__main__':
    unittest.main()
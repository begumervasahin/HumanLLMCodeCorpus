class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node()
    def add_at_the_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        return new_node
    def add_at_the_end(self, data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node
        return new_node
    def add_at_nth_position(self, data, position):
        if position <= 0:
            return "Invalid position, it can not be less than or equal to 0"
        if position == 1:
            return self.add_at_the_begining(data)
        cur_node = self.head
        for _ in range(position - 1):
            if cur_node.next is None:
                return "Invalid position, it exceeds the size of the linked list"
            cur_node = cur_node.next
        new_node = Node(data)
        new_node.next = cur_node.next
        cur_node.next = new_node
        return new_node
    def remove_at_the_begining(self):
        if self.head.next is None:
            return "List is empty, nothing to remove"
        removed_node = self.head.next
        self.head.next = removed_node.next
        return removed_node
    def remove_at_the_end(self):
        if self.head.next is None:
            return "List is empty, nothing to remove"
        cur_node = self.head
        while cur_node.next.next is not None:
            cur_node = cur_node.next
        removed_node = cur_node.next
        cur_node.next = None
        return removed_node
    def remove_at_nth_position(self, position):
        if position <= 0:
            return "Invalid position, it can not be less than or equal to 0"
        if position == 1:
            return self.remove_at_the_begining()
        cur_node = self.head
        for _ in range(position - 1):
            if cur_node.next is None:
                return "Invalid position, it exceeds the size of the linked list"
            cur_node = cur_node.next
        removed_node = cur_node.next
        cur_node.next = cur_node.next.next
        return removed_node
    def reverse(self):
        if self.head.next is None:
            return "List is empty, nothing to reverse"
        prev_node = None
        cur_node = self.head.next
        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head.next = prev_node
        return prev_node
    def reverse_using_recursion(self, cur_node):
        if cur_node.next is None:
            return cur_node
        new_head = self.reverse_using_recursion(cur_node.next)
        cur_node.next.next = cur_node
        cur_node.next = None
        return new_head
import unittest
class LinkedListTest(unittest.TestCase):
    def test_add_at_the_begining_empty_list(self):
        mylist = LinkedList()
        mylist.add_at_the_begining(10)
        self.assertEqual(mylist.add_at_the_begining(20).data, 20)
    def test_add_at_the_begining_non_empty_list(self):
        mylist = LinkedList()
        mylist.add_at_the_begining(10)
        mylist.add_at_the_begining(20)
        self.assertEqual(mylist.add_at_the_begining(30).data, 30)
    def test_add_at_the_end_empty_list(self):
        mylist = LinkedList()
        self.assertEqual(mylist.add_at_the_end(500).data, 500)
    def test_add_at_the_end_non_empty_list(self):
        mylist = LinkedList()
        mylist.add_at_the_end(10)
        mylist.add_at_the_end(20)
        temp = mylist.head.next
        self.assertEqual(temp.data, 20)
if __name__ == '__main__':
    unittest.main()
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
    def push(self, item):
        if len(self.stack) < self.capacity:
            self.stack.append(item)
            return "success"
        else:
            return "Stack full"
    def pop(self):
        if self.is_empty():
            return "Stack empty"
        else:
            return self.stack.pop()
    def top_element(self):
        if self.is_empty():
            return "Stack empty"
        else:
            return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
    def print_stack(self):
        if self.is_empty():
            print("Stack empty")
        else:
            print("Stack:", self.stack)
import unittest
class TestStackImplUsingArray(unittest.TestCase):
    def test_push(self):
        my_stack = Stack(10)
        self.assertEqual(my_stack.push(5), "success")
    def test_stack_overflow(self):
        my_stack = Stack(3)
        my_stack.push(5)
        my_stack.push(5)
        my_stack.push(5)
        self.assertEqual(my_stack.push(5), "Stack full")
    def test_top_element(self):
        my_stack = Stack(10)
        my_stack.push(10)
        self.assertEqual(my_stack.top_element(), 10)
    def test_top_element_stack_empty(self):
        my_stack = Stack(10)
        self.assertEqual(my_stack.top_element(), "Stack empty")
    def test_pop(self):
        my_stack = Stack(10)
        my_stack.push(10)
        self.assertEqual(my_stack.pop(), 10)
    def test_stack_underflow(self):
        my_stack = Stack(10)
        self.assertEqual(my_stack.pop(), "Stack empty")
    def test_is_empty(self):
        my_stack = Stack(10)
        self.assertTrue(my_stack.is_empty())
    def test_is_not_empty(self):
        my_stack = Stack(10)
        my_stack.push(10)
        self.assertFalse(my_stack.is_empty())
    def test_print_empty_stack(self):
        my_stack = Stack(10)
        my_stack.print_stack()
    def test_print(self):
        my_stack = Stack(10)
        my_stack.push(10)
        my_stack.push(20)
        my_stack.print_stack()
if __name__ == '__main__':
    unittest.main()
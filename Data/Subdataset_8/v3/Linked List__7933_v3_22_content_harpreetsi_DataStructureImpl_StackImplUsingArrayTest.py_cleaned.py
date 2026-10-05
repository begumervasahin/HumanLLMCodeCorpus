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
        return self.stack[-1] if self.stack else "Stack empty"
    def is_empty(self):
        return not self.stack
    def print_stack(self):
        print("Stack:", self.stack if self.stack else "Stack empty")
import unittest
class TestStackImplUsingArray(unittest.TestCase):
    def setUp(self):
        self.capacity = 10
        self.my_stack = Stack(self.capacity)
    def test_push(self):
        self.assertEqual(self.my_stack.push(5), "success")
    def test_stack_overflow(self):
        for _ in range(self.capacity):
            self.my_stack.push(5)
        self.assertEqual(self.my_stack.push(5), "Stack full")
    def test_top_element(self):
        self.my_stack.push(10)
        self.assertEqual(self.my_stack.top_element(), 10)
    def test_top_element_stack_empty(self):
        self.assertEqual(self.my_stack.top_element(), "Stack empty")
    def test_pop(self):
        self.my_stack.push(10)
        self.assertEqual(self.my_stack.pop(), 10)
    def test_stack_underflow(self):
        self.assertEqual(self.my_stack.pop(), "Stack empty")
    def test_is_empty(self):
        self.assertTrue(self.my_stack.is_empty())
    def test_is_not_empty(self):
        self.my_stack.push(10)
        self.assertFalse(self.my_stack.is_empty())
    def test_print_empty_stack(self):
        self.my_stack.print_stack()
    def test_print(self):
        self.my_stack.push(10)
        self.my_stack.push(20)
        self.my_stack.print_stack()
if __name__ == '__main__':
    unittest.main()
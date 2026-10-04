class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.max_size = size
        self.top = -1
    def push(self, item):
        if self.top >= self.max_size - 1:
            return "Stack full"
        self.top += 1
        self.stack[self.top] = item
        return "success"
    def pop(self):
        if self.top == -1:
            return "Stack empty"
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item
    def top_element(self):
        if self.top == -1:
            return "Stack empty"
        return self.stack[self.top]
    def is_empty(self):
        return self.top == -1
    def print_stack(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            for i in range(self.top, -1, -1):
                print(self.stack[i])
import unittest
class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack(10)
        self.assertEqual(stack.push(5), "success")
    def test_stack_overflow(self):
        stack = Stack(3)
        stack.push(5)
        stack.push(5)
        stack.push(5)
        self.assertEqual(stack.push(5), "Stack full")
    def test_top_element(self):
        stack = Stack(10)
        stack.push(10)
        self.assertEqual(stack.top_element(), 10)
    def test_top_element_stack_empty(self):
        stack = Stack(10)
        self.assertEqual(stack.top_element(), "Stack empty")
    def test_pop(self):
        stack = Stack(10)
        stack.push(10)
        self.assertEqual(stack.pop(), 10)
    def test_stack_underflow(self):
        stack = Stack(10)
        self.assertEqual(stack.pop(), "Stack empty")
    def test_is_empty(self):
        stack = Stack(10)
        self.assertTrue(stack.is_empty())
    def test_is_not_empty(self):
        stack = Stack(10)
        stack.push(10)
        self.assertFalse(stack.is_empty())
    def test_print_empty_stack(self):
        stack = Stack(10)
        stack.print_stack()
    def test_print_stack(self):
        stack = Stack(10)
        stack.push(10)
        stack.push(20)
        stack.print_stack()
if __name__ == '__main__':
    unittest.main()
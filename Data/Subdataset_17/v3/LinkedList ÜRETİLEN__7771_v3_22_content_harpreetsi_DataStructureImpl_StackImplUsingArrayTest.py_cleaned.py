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
        if self.is_empty():
            print("Stack is empty")
        else:
            for i in range(self.top, -1, -1):
                print(self.stack[i])
import unittest
class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(10)
    def test_push(self):
        self.assertEqual(self.stack.push(5), "success")
    def test_stack_overflow(self):
        stack = Stack(3)
        stack.push(5)
        stack.push(5)
        stack.push(5)
        self.assertEqual(stack.push(5), "Stack full")
    def test_top_element(self):
        self.stack.push(10)
        self.assertEqual(self.stack.top_element(), 10)
    def test_top_element_stack_empty(self):
        self.assertEqual(self.stack.top_element(), "Stack empty")
    def test_pop(self):
        self.stack.push(10)
        self.assertEqual(self.stack.pop(), 10)
    def test_stack_underflow(self):
        self.assertEqual(self.stack.pop(), "Stack empty")
    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
    def test_is_not_empty(self):
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())
    def test_print_empty_stack(self):
        with self.assertLogs(level='INFO') as log:
            self.stack.print_stack()
            self.assertIn("Stack is empty", log.output)
    def test_print_stack(self):
        self.stack.push(10)
        self.stack.push(20)
        with self.assertLogs(level='INFO') as log:
            self.stack.print_stack()
            self.assertIn("20", log.output)
            self.assertIn("10", log.output)
if __name__ == '__main__':
    unittest.main()
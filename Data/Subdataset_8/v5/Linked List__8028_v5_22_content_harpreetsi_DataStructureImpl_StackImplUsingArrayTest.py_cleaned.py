from StackImplUsingArray import Stack
import unittest
class TestStackImplUsingArray(unittest.TestCase):
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
        stack.print()
    def test_print(self):
        stack = Stack(10)
        stack.push(10)
        stack.push(20)
        stack.print()
if __name__ == '__main__':
    unittest.main()
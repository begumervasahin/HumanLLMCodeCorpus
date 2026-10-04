import unittest
from StackImplUsingArray import Stack
class TestStackImplUsingArray(unittest.TestCase):
    def setUp(self):
        self.stack_capacity = 10
        self.myStack = Stack(self.stack_capacity)
    def test_push(self):
        self.assertEqual(self.myStack.push(5), "success")
    def test_stack_overflow(self):
        small_stack = Stack(3)
        small_stack.push(5)
        small_stack.push(5)
        small_stack.push(5)
        self.assertEqual(small_stack.push(5), "Stack full")
    def test_top_element(self):
        self.myStack.push(10)
        self.assertEqual(self.myStack.topElement(), 10)
    def test_top_element_stack_empty(self):
        self.assertEqual(self.myStack.topElement(), "Stack empty")
    def test_pop(self):
        self.myStack.push(10)
        self.assertEqual(self.myStack.pop(), 10)
    def test_stack_underflow(self):
        self.assertEqual(self.myStack.pop(), "Stack empty")
    def test_is_empty(self):
        self.assertTrue(self.myStack.isEmpty())
    def test_is_not_empty(self):
        self.myStack.push(10)
        self.assertFalse(self.myStack.isEmpty())
    def test_print_empty_stack(self):
        try:
            self.myStack.print()
            result = "No exception"
        except Exception as e:
            result = str(e)
        self.assertEqual(result, "No exception")
    def test_print(self):
        self.myStack.push(10)
        self.myStack.push(20)
        try:
            self.myStack.print()
            result = "No exception"
        except Exception as e:
            result = str(e)
        self.assertEqual(result, "No exception")
if __name__ == '__main__':
    unittest.main()
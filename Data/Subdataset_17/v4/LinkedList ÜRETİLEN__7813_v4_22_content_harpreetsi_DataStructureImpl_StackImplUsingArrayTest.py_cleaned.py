import unittest
from StackImplUsingArray import Stack
class TestStackImplUsingArray(unittest.TestCase):
    def test_push(self):
        myStack = Stack(10)
        self.assertEqual(myStack.push(5), "success")
    def test_stack_overflow(self):
        myStack = Stack(3)
        myStack.push(5)
        myStack.push(5)
        myStack.push(5)
        self.assertEqual(myStack.push(5), "Stack full")
    def test_top_element(self):
        myStack = Stack(10)
        myStack.push(10)
        self.assertEqual(myStack.topElement(), 10)
    def test_top_element_stack_empty(self):
        myStack = Stack(10)
        self.assertEqual(myStack.topElement(), "Stack empty")
    def test_pop(self):
        myStack = Stack(10)
        myStack.push(10)
        self.assertEqual(myStack.pop(), 10)
    def test_stack_underflow(self):
        myStack = Stack(10)
        self.assertEqual(myStack.pop(), "Stack empty")
    def test_is_empty(self):
        myStack = Stack(10)
        self.assertTrue(myStack.isEmpty())
    def test_is_not_empty(self):
        myStack = Stack(10)
        myStack.push(10)
        self.assertFalse(myStack.isEmpty())
    def test_print_empty_stack(self):
        myStack = Stack(10)
        myStack.print()
    def test_print(self):
        myStack = Stack(10)
        myStack.push(10)
        myStack.push(20)
        myStack.print()
if __name__ == '__main__':
    unittest.main()
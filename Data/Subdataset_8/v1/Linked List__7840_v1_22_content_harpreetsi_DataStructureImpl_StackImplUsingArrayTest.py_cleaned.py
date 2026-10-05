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
        if self.isEmpty():
            return "Stack empty"
        else:
            return self.stack.pop()
    def topElement(self):
        if self.isEmpty():
            return "Stack empty"
        else:
            return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
    def print(self):
        if self.isEmpty():
            print("Stack empty")
        else:
            print("Stack:", self.stack)
import unittest
class TestStackImplUsingArray(unittest.TestCase):
    def test_push(self):
        myStack = Stack(10)
        self.assertEqual(myStack.push(5), "success")
    def test_stackOverflow(self):
        myStack = Stack(3)
        myStack.push(5)
        myStack.push(5)
        myStack.push(5)
        self.assertEqual(myStack.push(5), "Stack full")
    def test_topElement(self):
        myStack = Stack(10)
        myStack.push(10)
        self.assertEqual(myStack.topElement(), 10)
    def test_topElement_stackEmpty(self):
        myStack = Stack(10)
        self.assertEqual(myStack.topElement(), "Stack empty")
    def test_pop(self):
        myStack = Stack(10)
        myStack.push(10)
        self.assertEqual(myStack.pop(), 10)
    def test_stackUnderflow(self):
        myStack = Stack(10)
        self.assertEqual(myStack.pop(), "Stack empty")
    def test_isEmpty(self):
        myStack = Stack(10)
        self.assertTrue(myStack.isEmpty())
    def test_isNotEmpty(self):
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
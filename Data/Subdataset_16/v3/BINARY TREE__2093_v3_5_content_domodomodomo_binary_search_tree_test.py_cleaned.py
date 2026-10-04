import unittest
import random
from binary_search_tree import iterator, generator, BinarySearchTree, BinarySearchNode
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = BinarySearchTree()
        self.b2 = [random.randint(0, 99) for _ in range(1000)]
    def fonk2(self):
        for value in self.b2:
            self.b1.insert(value)
        b3 = self.b1.list()
        random.shuffle(b3)
        for value in b3:
            self.b1.delete_left(value)
        self.assertEqual(self.b1.list(), [])
    def fonk3(self):
        for value in self.b2:
            self.b1.insert(value)
        b3 = self.b1.list_sequentially()
        random.shuffle(b3)
        for value in b3:
            self.b1.delete_right(value)
        self.assertEqual(self.b1.list(), [])
    def fonk4(self):
        for value in self.b2:
            self.b1.insert(value)
        BinarySearchNode.b4 = iterator
        self.assertEqual(self.b1.list(), list(self.b1))
    def fonk5(self):
        for value in self.b2:
            self.b1.insert(value)
        BinarySearchNode.b4 = generator
        self.assertEqual(self.b1.list(), list(self.b1))
if b5 = = '__main__':
    unittest.main()
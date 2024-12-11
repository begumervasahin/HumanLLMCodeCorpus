import unittest
import random
from binary_search_tree import BinarySearchTree, BinarySearchNode, iterator, generator
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = BinarySearchTree()
    def fonk2(self):
        for value in (random.randint(0, 99) for _ in range(1000)):
            self.b1.insert(value)
        b2 = self.b1.list()
        random.shuffle(b2)
        for value in b2:
            self.b1.delete_left(value)
        self.assertEqual(self.b1.list(), [])
    def fonk3(self):
        for value in (random.randint(0, 99) for _ in range(1000)):
            self.b1.insert(value)
        b2 = self.b1.list_sequentially()
        random.shuffle(b2)
        for value in b2:
            self.b1.delete_right(value)
        self.assertEqual(self.b1.list(), [])
    def fonk4(self):
        for value in (random.randint(0, 99) for _ in range(1000)):
            self.b1.insert(value)
        BinarySearchNode.b3 = iterator
        self.assertEqual(self.b1.list(), list(self.b1))
    def fonk5(self):
        for value in (random.randint(0, 99) for _ in range(1000)):
            self.b1.insert(value)
        BinarySearchNode.b3 = generator
        self.assertEqual(self.b1.list(), list(self.b1))
if b4 = = '__main__':
    unittest.main()
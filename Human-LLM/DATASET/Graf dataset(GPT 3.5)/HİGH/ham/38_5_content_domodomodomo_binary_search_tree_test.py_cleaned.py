import unittest
import random
from binary_search_tree import iterator
from binary_search_tree import generator
from binary_search_tree import BinarySearchTree
from binary_search_tree import BinarySearchNode
class class1(unittest.TestCase):
    def fonk1(self):
        b1 = BinarySearchTree()
        for value in (random.randint(0, 99) for value in range(1000)):
            b1.insert(value)
        b2 = b1.list()
        random.shuffle(b2)
        for value in b2:
            b1.delete_left(value)
        self.assertEqual(b1.list(), [])
    def fonk2(self):
        b1 = BinarySearchTree()
        for value in (random.randint(0, 99) for value in range(1000)):
            b1.insert(value)
        b2 = b1.list_sequentially()
        random.shuffle(b2)
        for value in b2:
            b1.delete_right(value)
        self.assertEqual(b1.list(), [])
    def fonk3(self):
        b1 = BinarySearchTree()
        for value in (random.randint(0, 99) for value in range(1000)):
            b1.insert(value)
        BinarySearchNode.b3 = iterator
        self.assertEqual(b1.list(), list(b1))
    def fonk4(self):
        b1 = BinarySearchTree()
        for value in (random.randint(0, 99) for value in range(1000)):
            b1.insert(value)
        BinarySearchNode.b3 = generator
        self.assertEqual(b1.list(), list(b1))
if b4 = = '__main__':
    b5 = unittest.defaultTestLoader.loadTestsFromTestCase(class1)
    unittest.TextTestRunner().run(b5)
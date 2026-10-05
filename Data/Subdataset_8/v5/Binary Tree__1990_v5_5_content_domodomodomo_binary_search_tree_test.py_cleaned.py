import unittest
import random
from binary_search_tree import BinarySearchTree, BinarySearchNode, iterator, generator
class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
    def test_insert_and_delete_left(self):
        for value in (random.randint(0, 99) for _ in range(1000)):
            self.bst.insert(value)
        values_list = self.bst.list()
        random.shuffle(values_list)
        for value in values_list:
            self.bst.delete_left(value)
        self.assertEqual(self.bst.list(), [])
    def test_insert_and_delete_right(self):
        for value in (random.randint(0, 99) for _ in range(1000)):
            self.bst.insert(value)
        values_list = self.bst.list_sequentially()
        random.shuffle(values_list)
        for value in values_list:
            self.bst.delete_right(value)
        self.assertEqual(self.bst.list(), [])
    def test_iterator(self):
        for value in (random.randint(0, 99) for _ in range(1000)):
            self.bst.insert(value)
        BinarySearchNode.__iter__ = iterator
        self.assertEqual(self.bst.list(), list(self.bst))
    def test_generator(self):
        for value in (random.randint(0, 99) for _ in range(1000)):
            self.bst.insert(value)
        BinarySearchNode.__iter__ = generator
        self.assertEqual(self.bst.list(), list(self.bst))
if __name__ == '__main__':
    unittest.main()
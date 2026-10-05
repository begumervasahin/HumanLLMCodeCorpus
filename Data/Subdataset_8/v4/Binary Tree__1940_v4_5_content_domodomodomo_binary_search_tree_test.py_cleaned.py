import unittest
import random
from binary_search_tree import BinarySearchTree, BinarySearchNode, iterator, generator
class TestBinarySearchTree(unittest.TestCase):
    def test_insert_and_delete_left(self):
        bst = BinarySearchTree()
        for value in (random.randint(0, 99) for _ in range(1000)):
            bst.insert(value)
        values_list = bst.list()
        random.shuffle(values_list)
        for value in values_list:
            bst.delete_left(value)
        self.assertEqual(bst.list(), [])
    def test_insert_and_delete_right(self):
        bst = BinarySearchTree()
        for value in (random.randint(0, 99) for _ in range(1000)):
            bst.insert(value)
        values_list = bst.list_sequentially()
        random.shuffle(values_list)
        for value in values_list:
            bst.delete_right(value)
        self.assertEqual(bst.list(), [])
    def test_iterator(self):
        bst = BinarySearchTree()
        for value in (random.randint(0, 99) for _ in range(1000)):
            bst.insert(value)
        BinarySearchNode.__iter__ = iterator
        self.assertEqual(bst.list(), list(bst))
    def test_generator(self):
        bst = BinarySearchTree()
        for value in (random.randint(0, 99) for _ in range(1000)):
            bst.insert(value)
        BinarySearchNode.__iter__ = generator
        self.assertEqual(bst.list(), list(bst))
if __name__ == '__main__':
    unittest.main()
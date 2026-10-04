import unittest
import random
from binary_search_tree import iterator, generator, BinarySearchTree, BinarySearchNode
class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        self.values = [random.randint(0, 99) for _ in range(1000)]
        for value in self.values:
            self.bst.insert(value)
    def test_insert_list_delete_left(self):
        lst = self.bst.list()
        random.shuffle(lst)
        for value in lst:
            self.bst.delete_left(value)
        self.assertEqual(self.bst.list(), [])
    def test_insert_list_sequentially_delete_right(self):
        lst = self.bst.list_sequentially()
        random.shuffle(lst)
        for value in lst:
            self.bst.delete_right(value)
        self.assertEqual(self.bst.list(), [])
    def test_iterator(self):
        BinarySearchNode.__iter__ = iterator
        self.assertEqual(self.bst.list(), list(self.bst))
    def test_generator(self):
        BinarySearchNode.__iter__ = generator
        self.assertEqual(self.bst.list(), list(self.bst))
if __name__ == '__main__':
    unittest.main()
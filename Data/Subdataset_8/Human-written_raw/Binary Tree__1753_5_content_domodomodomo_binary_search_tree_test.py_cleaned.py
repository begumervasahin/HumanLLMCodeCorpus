import unittest
import random
from binary_search_tree import iterator
from binary_search_tree import generator
from binary_search_tree import BinarySearchTree
from binary_search_tree import BinarySearchNode
class Test(unittest.TestCase):
    def test_insert_list_delete_left(self):
        bst = BinarySearchTree()
        for value in (random.randint(0, 99) for value in range(1000)):
            bst.insert(value)
        lst = bst.list()
        random.shuffle(lst)
        for value in lst:
            bst.delete_left(value)
        self.assertEqual(bst.list(), [])
    def test_insert_list_sequentially_delte_right(self):
        bst = BinarySearchTree()
        for value in (random.randint(0, 99) for value in range(1000)):
            bst.insert(value)
        lst = bst.list_sequentially()
        random.shuffle(lst)
        for value in lst:
            bst.delete_right(value)
        self.assertEqual(bst.list(), [])
    def test_iterator(self):
        bst = BinarySearchTree()
        for value in (random.randint(0, 99) for value in range(1000)):
            bst.insert(value)
        BinarySearchNode.__iter__ = iterator
        self.assertEqual(bst.list(), list(bst))
    def test_generator(self):
        bst = BinarySearchTree()
        for value in (random.randint(0, 99) for value in range(1000)):
            bst.insert(value)
        BinarySearchNode.__iter__ = generator
        self.assertEqual(bst.list(), list(bst))
if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
    unittest.TextTestRunner().run(suite)
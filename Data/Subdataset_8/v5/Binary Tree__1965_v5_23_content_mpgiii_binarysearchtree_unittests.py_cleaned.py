import unittest
from binarytreevis import BinarySearchTree
class TestBinarySearchTree(unittest.TestCase):
    def test_constructor(self):
        bt1 = BinarySearchTree(contents=[0, 1, 2, 5, 90, -1])
        bt2 = BinarySearchTree(contents=[0, 1, 2, 5, 90, -1])
        self.assertListEqual(bt1.inorder(), bt2.inorder())
        self.assertListEqual(bt1.preorder(), bt2.preorder())
        self.assertListEqual(bt1.postorder(), bt2.postorder())
        self.assertListEqual(bt1.levelorder(), bt2.levelorder())
    def test_inorder(self):
        bt = BinarySearchTree(contents=[0, -1, 1])
        self.assertListEqual(bt.inorder(), [-1, 0, 1])
    def test_preorder(self):
        bt = BinarySearchTree(contents=[2, 0, 1])
        self.assertListEqual(bt.preorder(), [2, 0, 1])
    def test_postorder(self):
        bt = BinarySearchTree(contents=[2, 0, 1])
        self.assertListEqual(bt.postorder(), [1, 0, 2])
    def test_levelorder(self):
        bt = BinarySearchTree(contents=[2, 0, 1, 6, 10])
        self.assertListEqual(bt.levelorder(), [2, 0, 6, 1, 10])
    def test_insert(self):
        bt = BinarySearchTree()
        bt.insert(0)
        bt.insert(-1)
        bt.insert(1)
        self.assertListEqual(bt.inorder(), [-1, 0, 1])
    def test_delete(self):
        bt = BinarySearchTree(contents=[0, 1, 2])
        bt.delete(0)
        self.assertListEqual(bt.inorder(), [1, 2])
    def test_contains(self):
        bt = BinarySearchTree(contents=[0, 1, 2])
        self.assertTrue(0 in bt)
        bt.delete(0)
        self.assertFalse(0 in bt)
if __name__ == '__main__':
    unittest.main()
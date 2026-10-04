import unittest
from binarytreevis import BinarySearchTree
class class1(unittest.TestCase):
    def fonk1(self):
        b1 = BinarySearchTree(contents=[0, 1, 2, 5, 90, -1])
        b2 = BinarySearchTree(contents=[0, 1, 2, 5, 90, -1])
        self.assertListEqual(b1.inorder(), b2.inorder())
        self.assertListEqual(b1.preorder(), b2.preorder())
        self.assertListEqual(b1.postorder(), b2.postorder())
        self.assertListEqual(b1.levelorder(), b2.levelorder())
    def fonk2(self):
        b3 = BinarySearchTree(contents=[0, -1, 1])
        self.assertListEqual(b3.inorder(), [-1, 0, 1])
    def fonk3(self):
        b3 = BinarySearchTree(contents=[2, 0, 1])
        self.assertListEqual(b3.preorder(), [2, 0, 1])
    def fonk4(self):
        b3 = BinarySearchTree(contents=[2, 0, 1])
        self.assertListEqual(b3.postorder(), [1, 0, 2])
    def fonk5(self):
        b3 = BinarySearchTree(contents=[2, 0, 1, 6, 10])
        self.assertListEqual(b3.levelorder(), [2, 0, 6, 1, 10])
    def fonk6(self):
        b3 = BinarySearchTree()
        b3.insert(0)
        b3.insert(-1)
        b3.insert(1)
        self.assertListEqual(b3.inorder(), [-1, 0, 1])
    def fonk7(self):
        b3 = BinarySearchTree(contents=[0, 1, 2])
        b3.delete(0)
        self.assertListEqual(b3.inorder(), [1, 2])
    def fonk8(self):
        b3 = BinarySearchTree(contents=[0, 1, 2])
        self.assertTrue(0 in b3)
        b3.delete(0)
        self.assertFalse(0 in b3)
class class2(unittest.TestCase):
    def fonk9(self):
        b1 = BinarySearchTree(contents=[0, 100, -100, -150, -50, 2000])
        b2 = BinarySearchTree(contents=[0, 100, -100, -150, -50, 2000])
        self.assertListEqual(b1.inorder(), b2.inorder())
        self.assertListEqual(b1.preorder(), b2.preorder())
        self.assertListEqual(b1.postorder(), b2.postorder())
        self.assertListEqual(b1.levelorder(), b2.levelorder())
    def fonk10(self):
        b3 = BinarySearchTree(contents=[0, 100, -100, -150, -50, 2000])
        self.assertListEqual(b3.inorder(), [-150, -100, -50, 0, 100, 2000])
    def fonk11(self):
        b3 = BinarySearchTree(contents=[0, 100, -100, -150, -50, 2000])
        self.assertListEqual(b3.preorder(), [0, -100, -150, -50, 100, 2000])
    def fonk12(self):
        b3 = BinarySearchTree(contents=[0, 100, -100, -150, -50, 2000])
        self.assertListEqual(b3.postorder(), [-150, -50, -100, 2000, 100, 0])
    def fonk13(self):
        b3 = BinarySearchTree(contents=[0, 100, -100, -150, -50, 2000])
        self.assertListEqual(b3.levelorder(), [0, -100, 100, -150, -50, 2000])
    def fonk14(self):
        b3 = BinarySearchTree()
        b3.insert(0)
        b3.insert(-1)
        b3.insert(1)
        self.assertListEqual(b3.inorder(), [-1, 0, 1])
    def fonk15(self):
        b3 = BinarySearchTree(contents=[0, 1, 2])
        b3.delete(0)
        self.assertListEqual(b3.inorder(), [1, 2])
    def fonk16(self):
        b3 = BinarySearchTree(contents=[0, 1, 2])
        self.assertTrue(0 in b3)
        b3.delete(0)
        self.assertFalse(0 in b3)
if b4 = = '__main__':
    unittest.main()
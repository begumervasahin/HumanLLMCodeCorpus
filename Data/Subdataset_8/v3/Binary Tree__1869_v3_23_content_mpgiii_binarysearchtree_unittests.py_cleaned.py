class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self, contents=None):
        self.root = None
        if contents:
            for item in contents:
                self.insert(item)
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)
    def _insert_recursively(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        elif value > node.value:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)
    def delete(self, value):
        self.root = self._delete_recursively(self.root, value)
    def _delete_recursively(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self._delete_recursively(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursively(node.right, value)
        else:
            if not node.left and not node.right:
                return None
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_val = self._find_min(node.right)
            node.value = min_val
            node.right = self._delete_recursively(node.right, min_val)
        return node
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node.value
    def inorder(self):
        return self._inorder_recursively(self.root, [])
    def _inorder_recursively(self, node, result):
        if node:
            self._inorder_recursively(node.left, result)
            result.append(node.value)
            self._inorder_recursively(node.right, result)
        return result
    def preorder(self):
        return self._preorder_recursively(self.root, [])
    def _preorder_recursively(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursively(node.left, result)
            self._preorder_recursively(node.right, result)
        return result
    def postorder(self):
        return self._postorder_recursively(self.root, [])
    def _postorder_recursively(self, node, result):
        if node:
            self._postorder_recursively(node.left, result)
            self._postorder_recursively(node.right, result)
            result.append(node.value)
        return result
    def levelorder(self):
        if not self.root:
            return []
        result = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
    def __contains__(self, value):
        return self._contains_recursively(self.root, value)
    def _contains_recursively(self, node, value):
        if not node:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._contains_recursively(node.left, value)
        else:
            return self._contains_recursively(node.right, value)
import unittest
class BinarySearchTreeTests(unittest.TestCase):
    def test_constructor(self):
        bt = BinarySearchTree(contents=[0, 1, 2, 5, 90, -1])
        self.assertListEqual(bt.inorder(), [-1, 0, 1, 2, 5, 90])
        self.assertListEqual(bt.preorder(), [0, -1, 1, 2, 5, 90])
        self.assertListEqual(bt.postorder(), [-1, 2, 1, 90, 5, 0])
        self.assertListEqual(bt.levelorder(), [0, -1, 1, 2, 5, 90])
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
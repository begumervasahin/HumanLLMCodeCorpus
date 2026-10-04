from BST import BST
from TreeNode import TreeNode
class AVLTreeNode(TreeNode):
    def __init__(self, val):
        super().__init__(val)
        self.height = 1
class AVL(BST):
    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root
    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root
    def _rebalance(self, node):
        balance_factor = self._balance_factor(node)
        if balance_factor > 1:
            if self._balance_factor(node.left) >= 0:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
        if balance_factor < -1:
            if self._balance_factor(node.right) <= 0:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
        return node
    def _insert_node(self, node, val):
        if not node:
            return AVLTreeNode(val)
        if val < node.val:
            node.left = self._insert_node(node.left, val)
        else:
            node.right = self._insert_node(node.right, val)
        self._update_height(node)
        return self._rebalance(node)
    def insert(self, val):
        self.root = self._insert_node(self.root, val)
    def _delete_node(self, node, val):
        if not node:
            return None
        if val < node.val:
            node.left = self._delete_node(node.left, val)
        elif val > node.val:
            node.right = self._delete_node(node.right, val)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                predecessor = self._get_predecessor(node)
                node.val = predecessor.val
                node.left = self._delete_node(node.left, predecessor.val)
        self._update_height(node)
        return self._rebalance(node)
    def delete(self, val):
        self.root = self._delete_node(self.root, val)
    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))
    @staticmethod
    def _height(node):
        return node.height if node else 0
    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0
    def _get_predecessor(self, node):
        current = node.left
        while current.right:
            current = current.right
        return current
class AVLTreeNode:
    def __init__(self, val):
        self.val = val
        self.height = 1
        self.left = None
        self.right = None
class AVL:
    def __init__(self):
        self.root = None
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
    def rebalance(self, node):
        balance_factor = self._balance(node)
        if balance_factor > 1:
            if self._balance(node.left) >= 0:
                return self.rotate_right(node)
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance_factor < -1:
            if self._balance(node.right) <= 0:
                return self.rotate_left(node)
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node
    def insert(self, val):
        self.root = self._insert_node(self.root, val)
    def _insert_node(self, node, val):
        if not node:
            return AVLTreeNode(val)
        if val < node.val:
            node.left = self._insert_node(node.left, val)
        else:
            node.right = self._insert_node(node.right, val)
        self._update_height(node)
        return self.rebalance(node)
    def delete(self, val):
        self.root = self._delete_node(self.root, val)
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
        return self.rebalance(node)
    def _get_predecessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node
    def _update_height(self, node):
        if node:
            node.height = 1 + max(self._height(node.left), self._height(node.right))
    def _height(self, node):
        return node.height if node else 0
    def _balance(self, node):
        return self._height(node.left) - self._height(node.right)
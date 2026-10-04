
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)
    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)
    def delete(self, val):
        self.root = self._delete(self.root, val)
    def _delete(self, node, val):
        if not node:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_larger_node = self._find_min(node.right)
            node.val = min_larger_node.val
            node.right = self._delete(node.right, min_larger_node.val)
        return node
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    def search(self, val):
        return self._search(self.root, val)
    def _search(self, node, val):
        if node is None or node.val == val:
            return node
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)
    def inorder(self):
        return self._inorder(self.root)
    def _inorder(self, node):
        result = []
        if node:
            result = self._inorder(node.left)
            result.append(node.val)
            result = result + self._inorder(node.right)
        return result
from BST import BST
from TreeNode import TreeNode
class AVLTreeNode(TreeNode):
    def __init__(self, val):
        self.height = 0
        super().__init__(val)
class AVL(BST):
    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.calculate_height(node)
        self.calculate_height(new_root)
        return new_root
    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.calculate_height(node)
        self.calculate_height(new_root)
        return new_root
    def rebalance(self, node):
        balance = self.balance(node)
        if balance > 1:
            if self.balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1:
            if self.balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node
    def insert_node(self, node, val):
        if not node:
            return AVLTreeNode(val)
        if val < node.val:
            node.left = self.insert_node(node.left, val)
        else:
            node.right = self.insert_node(node.right, val)
        self.calculate_height(node)
        return self.rebalance(node)
    def insert(self, val):
        self.root = self.insert_node(self.root, val)
    def delete_node(self, node, val):
        if not node:
            return None
        if val < node.val:
            node.left = self.delete_node(node.left, val)
        elif val > node.val:
            node.right = self.delete_node(node.right, val)
        else:
            if not node.left and not node.right:
                return None
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_larger_node = self._find_min(node.right)
            node.val = min_larger_node.val
            node.right = self.delete_node(node.right, min_larger_node.val)
        self.calculate_height(node)
        return self.rebalance(node)
    def delete(self, val):
        self.root = self.delete_node(self.root, val)
    def calculate_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))
    @staticmethod
    def height(node):
        if not node:
            return 0
        return node.height
    def balance(self, node):
        return self.height(node.left) - self.height(node.right)
if __name__ == "__main__":
    avl = AVL()
    values_to_insert = [10, 20, 30, 40, 50, 25]
    for value in values_to_insert:
        avl.insert(value)
    print("In-order traversal after insertions:", avl.inorder())
    avl.delete(40)
    print("In-order traversal after deleting 40:", avl.inorder())
    print("Root balance:", avl.balance(avl.root))
    print("Root height:", avl.root.height)
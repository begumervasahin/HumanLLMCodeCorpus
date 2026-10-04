class AVLTree:
    class Node:
        def __init__(self, value, left=None, right=None, height=1):
            self.value = value
            self.left = left
            self.right = right
            self.height = height
    def __init__(self):
        self._root = None
    def insert(self, value):
        self._root = self._insert(self._root, value)
    def remove(self, value):
        self._root = self._remove(self._root, value)
    def find(self, value):
        return self._find(self._root, value)
    def height(self):
        return self._get_height(self._root)
    def min(self):
        if not self.is_empty():
            return self._find_min(self._root).value
        return None
    def max(self):
        if not self.is_empty():
            return self._find_max(self._root).value
        return None
    def is_empty(self):
        return self._root is None
    def __str__(self):
        return self._print_tree(self._root)
    def _insert(self, node, value):
        if node is None:
            return AVLTree.Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node
        return self._balance_tree(node)
    def _remove(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            if node.left is None or node.right is None:
                return node.left if node.left else node.right
            else:
                min_node = self._find_min(node.right)
                node.value = min_node.value
                node.right = self._remove_min(node.right)
        return self._balance_tree(node)
    def _find(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._find(node.left, value)
        else:
            return self._find(node.right, value)
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    def _find_max(self, node):
        while node.right is not None:
            node = node.right
        return node
    def _remove_min(self, node):
        if node.left is None:
            return node.right
        node.left = self._remove_min(node.left)
        return self._balance_tree(node)
    def _get_height(self, node):
        return node.height if node else 0
    def _update_height(self, node):
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
    def _balance_factor(self, node):
        return self._get_height(node.right) - self._get_height(node.left)
    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root
    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root
    def _balance_tree(self, node):
        self._update_height(node)
        if self._balance_factor(node) == 2:
            if self._balance_factor(node.right) < 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        if self._balance_factor(node) == -2:
            if self._balance_factor(node.left) > 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        return node
    def _print_tree(self, node):
        if node is None:
            return ''
        result = f'{node.value},{node.height}\n'
        result += self._print_tree(node.left)
        result += self._print_tree(node.right)
        return result
if __name__ == "__main__":
    avl_tree = AVLTree()
    values = [10, 20, 30, 40, 50, 25]
    for val in values:
        avl_tree.insert(val)
    print("AVL Tree:")
    print(avl_tree)
    print("Find node with value 20:")
    node = avl_tree.find(20)
    print(node.value if node else "Not found")
    print("Minimum value in AVL Tree:")
    print(avl_tree.min())
    print("Maximum value in AVL Tree:")
    print(avl_tree.max())
    print("Removing node with value 10:")
    avl_tree.remove(10)
    print(avl_tree)
    print("Tree height:")
    print(avl_tree.height())
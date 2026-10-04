class Node:
    def __init__(self, word):
        self.word = word
        self.count = 1
        self.left = None
        self.right = None
class BSTree:
    def __init__(self, root=None):
        self.root = root
    def find(self, word):
        return self._find(self.root, word)
    def add(self, word):
        if self.root is None:
            self.root = Node(word)
        else:
            self._add(self.root, word)
    def in_order_print(self):
        self._in_order_print(self.root)
    def size(self):
        return self._size(self.root)
    def height(self):
        return self._height(self.root)
    def _add(self, node, word):
        if word == node.word:
            node.count += 1
        elif word < node.word:
            if node.left is None:
                node.left = Node(word)
            else:
                self._add(node.left, word)
        else:
            if node.right is None:
                node.right = Node(word)
            else:
                self._add(node.right, word)
    def _find(self, node, word):
        if node is None:
            return 0
        if word == node.word:
            return node.count
        elif word < node.word:
            return self._find(node.left, word)
        else:
            return self._find(node.right, word)
    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)
    def _height(self, node):
        if node is None:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1
    def _in_order_print(self, node):
        if node is None:
            return
        self._in_order_print(node.left)
        print(f"{node.word}: {node.count}")
        self._in_order_print(node.right)

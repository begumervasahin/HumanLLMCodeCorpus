import random
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.priority = random.random()
    def __str__(self):
        return str(self.data)
class TreapSet:
    def __init__(self):
        self.root = None
        self.count = 0
    def add(self, element):
        self.count += 1
        self.root = self._add_recursive(self.root, element)
    def _add_recursive(self, node, element):
        if node is None:
            return Node(element)
        if element < node.data:
            node.left = self._add_recursive(node.left, element)
            if node.left.priority > node.priority:
                node = self._right_rotate(node)
        elif element > node.data:
            node.right = self._add_recursive(node.right, element)
            if node.right.priority > node.priority:
                node = self._left_rotate(node)
        return node
    def _left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root
    def _right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root
    def __contains__(self, element):
        return self._contains_recursive(self.root, element)
    def _contains_recursive(self, node, element):
        if node is None:
            return False
        if node.data == element:
            return True
        elif element < node.data:
            return self._contains_recursive(node.left, element)
        else:
            return self._contains_recursive(node.right, element)
    def height(self):
        return self._height_recursive(self.root)
    def _height_recursive(self, node):
        if node is None:
            return 0
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))
    def __len__(self):
        return self.count
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
    def left_rotate(self, node):
        new_parent = node.right
        node.right = new_parent.left
        new_parent.left = node
        return new_parent
    def right_rotate(self, node):
        new_parent = node.left
        node.left = new_parent.right
        new_parent.right = node
        return new_parent
    def add(self, element):
        self.count += 1
        if self.root is None:
            self.root = Node(element)
        else:
            self.root = self._add_recursive(element, self.root)
    def _add_recursive(self, element, node):
        if node is None:
            return Node(element)
        if element < node.data:
            node.left = self._add_recursive(element, node.left)
            if node.left.priority > node.priority:
                node = self.right_rotate(node)
        else:
            node.right = self._add_recursive(element, node.right)
            if node.right.priority > node.priority:
                node = self.left_rotate(node)
        return node
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
from random import randint
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    def convert_to_array(self, array):
        if self.left:
            self.left.convert_to_array(array)
        array.append(self.value)
        if self.right:
            self.right.convert_to_array(array)
        return array
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data)
    def find(self, data):
        return self._find_node(self.root, data)
    def _find_node(self, node, data):
        if node is None:
            return False
        if data == node.value:
            return True
        elif data < node.value:
            return self._find_node(node.left, data)
        else:
            return self._find_node(node.right, data)
    def convert_to_array(self):
        if self.root:
            return self.root.convert_to_array([])
        return []
    def rearrange(self):
        nodes = self.convert_to_array()
        nodes.sort()
        middle = len(nodes)
        self.root = Node(nodes.pop(middle))
        for element in nodes:
            self.root.insert(element)
        return self.convert_to_array()
tree = BinaryTree()
for _ in range(50):
    tree.insert(randint(0, 100))
print("Original tree (DFS):", tree.convert_to_array())
print("Rearranged tree (DFS):", tree.rearrange())
print("Find 55:", tree.find(55))
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
    def convert_to_array(self):
        array = []
        self._dfs(self, array)
        return array
    def _dfs(self, node, array):
        if node:
            array.append(node.value)
            self._dfs(node.left, array)
            self._dfs(node.right, array)
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)
    def find(self, value):
        return self._find_node(self.root, value)
    def _find_node(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._find_node(node.left, value)
        return self._find_node(node.right, value)
    def convert_to_array(self):
        if self.root is not None:
            return self.root.convert_to_array()
        return []
    def rearrange(self):
        nodes = self.convert_to_array()
        nodes.sort()
        middle_index = len(nodes)
        self.root = Node(nodes.pop(middle_index))
        for value in nodes:
            self.insert(value)
        return self.convert_to_array()
tree = BinaryTree()
for _ in range(50):
    tree.insert(randint(0, 100))
print("Original tree (DFS array):", tree.convert_to_array())
print("Rearranged tree (DFS array):", tree.rearrange())
print("Is 55 in the tree?", tree.find(55))
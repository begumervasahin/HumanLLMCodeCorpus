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
    def to_array(self, array=None):
        if array is None:
            array = []
        array.append(self.value)
        if self.left:
            self.left.to_array(array)
        if self.right:
            self.right.to_array(array)
        return array
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
        elif value < node.value:
            return self._find_node(node.left, value)
        else:
            return self._find_node(node.right, value)
    def to_array(self):
        return self.root.to_array() if self.root else []
    def rearrange(self):
        nodes = self.to_array()
        nodes.sort()
        self.root = Node(nodes.pop(len(nodes)
        for value in nodes:
            self.insert(value)
        return self.to_array()
if __name__ == "__main__":
    tree = BinaryTree()
    for _ in range(50):
        tree.insert(randint(0, 100))
    print("Tree in DFS Array Form:")
    print(tree.to_array())
    print("\nRe-arranged Tree with Median as Root:")
    print(tree.rearrange())
    value_to_find = 55
    print(f"\nSearching for {value_to_find} in the tree:")
    print("Found!" if tree.find(value_to_find) else "Not Found!")
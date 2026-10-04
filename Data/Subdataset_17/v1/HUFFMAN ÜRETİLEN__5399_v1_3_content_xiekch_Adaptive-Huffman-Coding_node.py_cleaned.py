class Node:
    def __init__(self, char=None):
        self.weight = 0
        self.parent = None
        self.right = None
        self.left = None
        self.level = 0
        self.char = char if char is not None else b'*'
    def set_left(self, node):
        self.left = node
        node.parent = self
        node.update_level()
    def set_right(self, node):
        self.right = node
        node.parent = self
        node.update_level()
    def replace_child(self, child, node):
        if self.left == child:
            self.set_left(node)
        elif self.right == child:
            self.set_right(node)
    def update_level(self):
        self.level = self.parent.level + 1 if self.parent else 0
        if self.left:
            self.left.update_level()
        if self.right:
            self.right.update_level()
    def has_no_child(self):
        return self.left is None and self.right is None
    def is_ancestor(self, node):
        ancestor = self.parent
        while ancestor:
            if ancestor == node:
                return True
            ancestor = ancestor.parent
        return False
    def swap(self, node):
        if self == node or node.is_ancestor(self) or self.is_ancestor(node):
            return
        parent1 = self.parent
        parent2 = node.parent
        parent2.replace_child(node, self)
        parent1.replace_child(self, node)
if __name__ == "__main__":
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    node_a.set_left(node_b)
    node_a.set_right(node_c)
    node_b.swap(node_c)
    print(f"Node A's left child: {node_a.left.char}")
    print(f"Node A's right child: {node_a.right.char}")

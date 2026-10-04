class Node:
    def __init__(self, char=None):
        self.char = char or b'*'
        self.weight = 0
        self.level = 0
        self.parent = None
        self.left = None
        self.right = None
    def set_left(self, child_node):
        self.left = child_node
        self._update_child(child_node)
    def set_right(self, child_node):
        self.right = child_node
        self._update_child(child_node)
    def replace_child(self, current_child, new_child):
        if self.left == current_child:
            self.set_left(new_child)
        elif self.right == current_child:
            self.set_right(new_child)
    def update_level(self):
        self.level = self.parent.level + 1 if self.parent else 0
        if self.left:
            self.left.update_level()
        if self.right:
            self.right.update_level()
    def has_no_children(self):
        return self.left is None and self.right is None
    def is_ancestor_of(self, node):
        current = node.parent
        while current:
            if current == self:
                return True
            current = current.parent
        return False
    def swap_with(self, other):
        if self == other or self.is_ancestor_of(other) or other.is_ancestor_of(self):
            return
        self_parent = self.parent
        other_parent = other.parent
        other_parent.replace_child(other, self)
        self_parent.replace_child(self, other)
    def _update_child(self, child_node):
        child_node.parent = self
        child_node.update_level()
if __name__ == "__main__":
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    node_a.set_left(node_b)
    node_a.set_right(node_c)
    node_b.swap_with(node_c)
    print(f"Node A's left child: {node_a.left.char}")
    print(f"Node A's right child: {node_a.right.char}")

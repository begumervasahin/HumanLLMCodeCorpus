class Node:
    def __init__(self, char=None):
        self.weight = 0
        self.parent = None
        self.left = None
        self.right = None
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
    def replace_child(self, old_child, new_child):
        if self.left == old_child:
            self.set_left(new_child)
        elif self.right == old_child:
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
        ancestor = self
        while ancestor:
            if ancestor == node:
                return True
            ancestor = ancestor.parent
        return False
    def swap_with(self, node):
        if self == node or self.is_ancestor_of(node) or node.is_ancestor_of(self):
            return
        self_parent, node_parent = self.parent, node.parent
        if self_parent:
            self_parent.replace_child(self, node)
        if node_parent:
            node_parent.replace_child(node, self)
        self.left, node.left = node.left, self.left
        self.right, node.right = node.right, self.right
        self.update_level()
        node.update_level()
class AVLTreeNode:
    def __init__(self, key_data):
        self.key_data = key_data
        self.count = 1
        self.depth = 0
        self.height = 0
        self.order = -1
        self.parent = None
        self.left = None
        self.right = None
    def is_left_child(self):
        return self.parent is not None and self.parent.left == self
    def is_right_child(self):
        return self.parent is not None and self.parent.right == self
    def is_leaf(self):
        return self.left is None and self.right is None
    def is_root(self):
        return self.parent is None
    def has_grand_parent(self):
        return self.parent and self.parent.parent
    def left_subtree_height(self):
        return self.left.height if self.left else -1
    def right_subtree_height(self):
        return self.right.height if self.right else -1
    def max_subtree_height(self):
        return max(self.left_subtree_height(), self.right_subtree_height())
    def is_balanced(self):
        return abs(self.right_subtree_height() - self.left_subtree_height()) <= 1
    def rightmost_node_in_left_subtree(self):
        current_node = self
        while current_node.left:
            current_node = current_node.left
        return current_node if current_node != self else None
    def leftmost_node_in_right_subtree(self):
        current_node = self
        while current_node.right:
            current_node = current_node.right
        return current_node if current_node != self else None
    def parent_of_nearest_ancestor_that_is_left_child(self):
        current_node = self
        while current_node.is_right_child():
            current_node = current_node.parent
        if current_node.is_left_child():
            return current_node.parent
        return None
    def parent_of_nearest_ancestor_that_is_right_child(self):
        current_node = self
        while current_node.is_left_child():
            current_node = current_node.parent
        if current_node.is_right_child():
            return current_node.parent
        return None
    def next(self):
        if self.is_root():
            return self.leftmost_node_in_right_subtree() if self.right else None
        if self.is_left_child():
            return self.leftmost_node_in_right_subtree() if self.right else self.parent
        return self.leftmost_node_in_right_subtree() or self.parent_of_nearest_ancestor_that_is_left_child()
    def prev(self):
        if self.is_root():
            return self.rightmost_node_in_left_subtree() if self.left else None
        if self.is_left_child():
            return self.rightmost_node_in_left_subtree() if self.left else self.parent_of_nearest_ancestor_that_is_right_child()
        return self.rightmost_node_in_left_subtree() or self.parent
class AVLTree:
    def __init__(self):
        self.root_node = None
        self.num_nodes = 0
    def find(self, key_data):
        current_node = self.root_node
        while current_node:
            if current_node.key_data == key_data:
                return current_node
            current_node = current_node.left if current_node.key_data > key_data else current_node.right
        return None
    def insert(self, key_data):
        if not self.root_node:
            self.root_node = AVLTreeNode(key_data)
            self.root_node.height = 0
            self.root_node.depth = 0
            self.num_nodes = 1
        else:
            new_node = self.root_node.insert(self, key_data)
            if new_node:
                new_node.bubble_up(self)
    def remove(self, key_data):
        removed_node = self.find(key_data)
        if removed_node:
            removed_node.remove(self)
            self.num_nodes -= 1
        return removed_node
    def print_tree(self):
        current_node = self.root_node
        while current_node:
            print(current_node.key_data)
            current_node = current_node.next()
    def get_first(self):
        current_node = self.root_node
        while current_node.left:
            current_node = current_node.left
        return current_node
    def mark_order(self):
        current_node = self.get_first()
        n = 0
        while current_node:
            current_node.order = n
            n += 1
            current_node = current_node.next()
if __name__ == "__main__":
    tree = AVLTree()
    for key in [5, 3, 7, 4, 6, 8]:
        tree.insert(key)
    tree.print_tree()
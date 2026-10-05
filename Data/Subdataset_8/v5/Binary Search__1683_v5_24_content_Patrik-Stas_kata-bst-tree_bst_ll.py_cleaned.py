class Node:
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
    def remove_child(self, child_node):
        if child_node == self.left:
            self.left = None
        elif child_node == self.right:
            self.right = None
    def print_info(self):
        left_str = f"_left: {self.left.value}" if self.left else "        "
        right_str = f"_right: {self.right.value}" if self.right else "         "
        parent_str = "   ROOT" if self.parent is None else f"   _parent: {self.parent.value}"
        print(f"Node({self.value})  {left_str}  {right_str}  {parent_str}")
    def is_leaf(self):
        return self.left is None and self.right is None
    def is_root(self):
        return self.parent is None
    def set_right(self, child_node):
        self.right = child_node
        if child_node:
            child_node.parent = self
    def set_left(self, child_node):
        self.left = child_node
        if child_node:
            child_node.parent = self
    def replace_child(self, old_child, new_child):
        if old_child == self.left:
            self.set_left(new_child)
        elif old_child == self.right:
            self.set_right(new_child)
        else:
            raise ValueError("old_child node not found")
class TreePrinter:
    def __init__(self, bst):
        self.bst = bst
    def print_bst(self):
        print("foo")
    def print_preorder(self, nice_print=False):
        self.preorder(self.bst.root, nice_print)
    def preorder(self, traverse_node, nice_print):
        if traverse_node is None:
            raise ValueError("Passing None as node to preorder print is not expected.")
        if nice_print:
            traverse_node.print_info()
        else:
            print(f"{traverse_node.value} ", end='')
        if traverse_node.left:
            self.preorder(traverse_node.left, nice_print)
        if traverse_node.right:
            self.preorder(traverse_node.right, nice_print)
class BstByLinkedList:
    def __init__(self):
        self.root = None
    def count_nodes(self):
        return self._count_nodes(self.root)
    def _count_nodes(self, subtree_root):
        if subtree_root is not None:
            return 1 + self._count_nodes(subtree_root.left) + self._count_nodes(subtree_root.right)
        return 0
    def insert(self, key, value):
        if key is None or value is None:
            raise ValueError("Key or value cannot be None.")
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(self.root, key, value)
    def _insert(self, subtree_root, key, value):
        if key == subtree_root.key:
            raise ValueError(f"Duplicate key: {key}")
        if key < subtree_root.key:
            if subtree_root.left is None:
                subtree_root.set_left(Node(key, value))
            else:
                self._insert(subtree_root.left, key, value)
        else:
            if subtree_root.right is None:
                subtree_root.set_right(Node(key, value))
            else:
                self._insert(subtree_root.right, key, value)
    def _search(self, subtree_root, search_key):
        if subtree_root is None or subtree_root.key == search_key:
            return subtree_root
        elif search_key < subtree_root.key:
            return self._search(subtree_root.left, search_key)
        else:
            return self._search(subtree_root.right, search_key)
    def search(self, search_key):
        node = self._search(self.root, search_key)
        return node.value if node else None
    def find_max_node(self, subtree_root):
        while subtree_root.right:
            subtree_root = subtree_root.right
        return subtree_root
    def delete(self, key):
        node = self._search(self.root, key)
        if not node:
            raise ValueError(f"Node with key {key} not found.")
        deleted_value = node.value
        if node.is_leaf():
            if node.parent:
                node.parent.remove_child(node)
            else:
                self.root = None
        elif not node.left:
            node.parent.replace_child(node, node.right)
        elif not node.right:
            node.parent.replace_child(node, node.left)
        else:
            max_left_node = self.find_max_node(node.left)
            node.key, node.value = max_left_node.key, max_left_node.value
            self.delete(max_left_node.key)
        return deleted_value
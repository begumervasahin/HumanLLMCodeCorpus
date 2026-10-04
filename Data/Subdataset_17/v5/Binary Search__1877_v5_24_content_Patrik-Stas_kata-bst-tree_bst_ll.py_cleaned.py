class Node:
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
    def remove_child(self, child_to_remove):
        if child_to_remove == self.left:
            self.left = None
        elif child_to_remove == self.right:
            self.right = None
    def print_info(self):
        left_str = "left: None" if self.left is None else f"left: {self.left.value}"
        right_str = "right: None" if self.right is None else f"right: {self.right.value}"
        parent_str = "ROOT" if self.parent is None else f"parent: {self.parent.value}"
        print(f"Node({self.value})  {left_str}  {right_str}  {parent_str}")
    def is_leaf(self):
        return self.left is None and self.right is None
    def is_root(self):
        return self.parent is None
    def set_right(self, child_node):
        self.right = child_node
        child_node.parent = self
    def set_left(self, child_node):
        self.left = child_node
        child_node.parent = self
    def replace_child(self, old_child, new_child):
        if old_child == self.left:
            self.set_left(new_child)
        elif old_child == self.right:
            self.set_right(new_child)
        else:
            raise ValueError("Child node not found among this node's children.")
        old_child.parent = None
class TreePrinter:
    def __init__(self, bst):
        self.bst = bst
        self.center = 40
    def print_tree(self):
        print("Tree structure placeholder")
    def print_preorder(self, detailed=False):
        self._preorder(self.bst.root, detailed)
    def _preorder(self, node, detailed):
        if node is None:
            return
        if detailed:
            node.print_info()
        else:
            print(f"{node.value} ", end="")
        self._preorder(node.left, detailed)
        self._preorder(node.right, detailed)
class BstByLinkedList:
    def __init__(self):
        self.root = None
    def count_nodes(self):
        return self._count_nodes(self.root)
    def _count_nodes(self, subtree_root):
        if subtree_root is None:
            return 0
        return 1 + self._count_nodes(subtree_root.left) + self._count_nodes(subtree_root.right)
    def insert(self, key, value):
        if key is None or value is None:
            raise ValueError("Key and value must be provided.")
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(self.root, key, value)
    def _insert(self, subtree_root, key, value):
        if key == subtree_root.key:
            raise ValueError(f"Duplicate key {key}")
        elif key < subtree_root.key:
            if subtree_root.left is None:
                subtree_root.set_left(Node(key, value, subtree_root))
            else:
                self._insert(subtree_root.left, key, value)
        else:
            if subtree_root.right is None:
                subtree_root.set_right(Node(key, value, subtree_root))
            else:
                self._insert(subtree_root.right, key, value)
    def search(self, search_key):
        node = self._search(self.root, search_key)
        return node.value if node else None
    def _search(self, subtree_root, search_key):
        if subtree_root is None or search_key == subtree_root.key:
            return subtree_root
        if search_key < subtree_root.key:
            return self._search(subtree_root.left, search_key)
        return self._search(subtree_root.right, search_key)
    def find_max(self, subtree_root):
        current = subtree_root
        while current.right:
            current = current.right
        return current
    def delete(self, key):
        node_to_delete = self._search(self.root, key)
        if node_to_delete is None:
            raise ValueError(f"Node with key {key} not found in the tree.")
        if node_to_delete.is_leaf():
            self._delete_leaf(node_to_delete)
        elif node_to_delete.left is None:
            self._replace_with_child(node_to_delete, node_to_delete.right)
        elif node_to_delete.right is None:
            self._replace_with_child(node_to_delete, node_to_delete.left)
        else:
            self._delete_node_with_two_children(node_to_delete)
        return node_to_delete.value
    def _delete_leaf(self, node):
        if node.is_root():
            self.root = None
        else:
            node.parent.remove_child(node)
    def _replace_with_child(self, node, child):
        if node.is_root():
            self.root = child
        else:
            node.parent.replace_child(node, child)
    def _delete_node_with_two_children(self, node):
        max_node = self.find_max(node.left)
        if max_node.left:
            max_node.parent.replace_child(max_node, max_node.left)
        else:
            max_node.parent.remove_child(max_node)
        node.key = max_node.key
        node.value = max_node.value
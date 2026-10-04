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
        left_str = "        " if self.left is None else f"left: {self.left.value}"
        right_str = "         " if self.right is None else f"right: {self.right.value}"
        parent_str = "   ROOT" if self.parent is None else f"   parent: {self.parent.value}"
        print(f"Node({self.value})  {left_str}  {right_str}{parent_str}")
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
            raise ValueError("old_child node not found")
        old_child.parent = None
class TreePrinter:
    def __init__(self, bst):
        self.bst = bst
        self.center = 40
    def print_tree(self):
        print("foo")
    def print_preorder(self, nice_print=False):
        self._preorder(self.bst.root, nice_print)
    def _preorder(self, node, nice_print):
        if node is None:
            raise ValueError("Passing None as node to preorder print is not expected.")
        if nice_print:
            node.print_info()
        else:
            print(f"{node.value} ", end="")
        if node.left is not None:
            self._preorder(node.left, nice_print)
        if node.right is not None:
            self._preorder(node.right, nice_print)
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
            raise ValueError("Insert key or value is null.")
        elif self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(self.root, key, value)
    def _insert(self, subtree_root, key, value):
        if subtree_root.key == key:
            raise ValueError(f"Duplicate key {key}")
        elif key < subtree_root.key:
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
        if subtree_root is None:
            return None
        if subtree_root.key == search_key:
            return subtree_root
        elif search_key < subtree_root.key:
            return self._search(subtree_root.left, search_key)
        else:
            return self._search(subtree_root.right, search_key)
    def search(self, search_key):
        node = self._search(self.root, search_key)
        return node.value if node is not None else None
    def find_biggest_node_in_subtree(self, subtree_root):
        if subtree_root.right is None:
            return subtree_root
        else:
            return self.find_biggest_node_in_subtree(subtree_root.right)
    def delete(self, key_delete):
        node_to_delete = self._search(self.root, key_delete)
        if node_to_delete is None:
            raise ValueError(f"Can't delete node with key {key_delete} because it was not found in the tree.")
        deleted_value = node_to_delete.value
        if node_to_delete.is_leaf():
            node_to_delete.parent.remove_child(node_to_delete)
        elif node_to_delete.left is None:
            node_to_delete.parent.replace_child(node_to_delete, node_to_delete.right)
        else:
            replacement_node = self.find_biggest_node_in_subtree(node_to_delete.left)
            if replacement_node.left is not None:
                replacement_node.parent.replace_child(replacement_node, replacement_node.left)
            else:
                replacement_node.parent.remove_child(replacement_node)
            node_to_delete.key = replacement_node.key
            node_to_delete.value = replacement_node.value
        return deleted_value
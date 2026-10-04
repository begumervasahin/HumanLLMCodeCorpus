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
        left_str = f"left: {self.left.value}" if self.left else "left: None"
        right_str = f"right: {self.right.value}" if self.right else "right: None"
        parent_str = "ROOT" if self.parent is None else f"parent: {self.parent.value}"
        print(f"Node({self.value})  {left_str}  {right_str}  {parent_str}")
    def is_leaf(self):
        return not self.left and not self.right
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
            raise ValueError("The specified old child node was not found.")
class TreePrinter:
    def __init__(self, bst):
        self.bst = bst
    def print_preorder(self, detailed=False):
        self._preorder(self.bst.root, detailed)
    def _preorder(self, node, detailed):
        if node:
            if detailed:
                node.print_info()
            else:
                print(f"{node.value} ", end="")
            self._preorder(node.left, detailed)
            self._preorder(node.right, detailed)
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def count_nodes(self):
        return self._count_nodes(self.root)
    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)
    def insert(self, key, value):
        if key is None or value is None:
            raise ValueError("Key and value cannot be None.")
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(self.root, key, value)
    def _insert(self, node, key, value):
        if key == node.key:
            raise ValueError(f"Duplicate key {key} is not allowed.")
        elif key < node.key:
            if node.left is None:
                node.set_left(Node(key, value))
            else:
                self._insert(node.left, key, value)
        else:
            if node.right is None:
                node.set_right(Node(key, value))
            else:
                self._insert(node.right, key, value)
    def search(self, key):
        node = self._search(self.root, key)
        return node.value if node else None
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    def find_max(self, node):
        while node.right:
            node = node.right
        return node
    def delete(self, key):
        node_to_delete = self._search(self.root, key)
        if node_to_delete is None:
            raise ValueError(f"Key {key} not found in the tree.")
        if node_to_delete.is_leaf():
            if node_to_delete.is_root():
                self.root = None
            else:
                node_to_delete.parent.remove_child(node_to_delete)
        elif node_to_delete.left is None:
            self._replace_node(node_to_delete, node_to_delete.right)
        elif node_to_delete.right is None:
            self._replace_node(node_to_delete, node_to_delete.left)
        else:
            replacement_node = self.find_max(node_to_delete.left)
            if replacement_node.left:
                self._replace_node(replacement_node, replacement_node.left)
            else:
                replacement_node.parent.remove_child(replacement_node)
            node_to_delete.key = replacement_node.key
            node_to_delete.value = replacement_node.value
        return node_to_delete.value
    def _replace_node(self, node_to_replace, new_node):
        if node_to_replace.is_root():
            self.root = new_node
        else:
            node_to_replace.parent.replace_child(node_to_replace, new_node)
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10, "ten")
    bst.insert(5, "five")
    bst.insert(15, "fifteen")
    bst.insert(7, "seven")
    bst.insert(3, "three")
    printer = TreePrinter(bst)
    print("Tree in preorder (detailed):")
    printer.print_preorder(detailed=True)
    print(f"\nSearch for 7: {bst.search(7)}")
    print("\nDeleting node with key 5:")
    bst.delete(5)
    printer.print_preorder(detailed=True)
    print(f"\nNumber of nodes: {bst.count_nodes()}")
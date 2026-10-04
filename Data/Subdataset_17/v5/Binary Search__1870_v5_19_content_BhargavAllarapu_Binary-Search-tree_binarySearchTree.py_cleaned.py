class BinarySearchTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    def make_empty(self):
        if self.data is not None:
            self._recursive_make_empty(self)
            self.data = None
            print("Deleted every node... Now the tree is empty.")
        else:
            print("Tree is already empty.")
    def _recursive_make_empty(self, node):
        if node.left:
            node.left = self._recursive_make_empty(node.left)
        if node.right:
            node.right = self._recursive_make_empty(node.right)
        return None
    def find(self, key):
        if self.data is None:
            print("Nothing to find... Tree is empty.")
            return None
        if key < self.data:
            return self.left.find(key) if self.left else self._node_not_found(key)
        elif key > self.data:
            return self.right.find(key) if self.right else self._node_not_found(key)
        else:
            print(f"Node {key}: Found.")
            return self.data
    def _node_not_found(self, key):
        print(f"Node {key}: Not found.")
        return None
    def find_min(self):
        if self.data is None:
            print("Nothing to find... Tree is empty.")
            return None
        return self.left.find_min() if self.left else self.data
    def find_max(self):
        if self.data is None:
            print("Nothing to find... Tree is empty.")
            return None
        return self.right.find_max() if self.right else self.data
    def insert(self, key):
        if self.data is None:
            self.data = key
        elif key < self.data:
            if self.left is None:
                self.left = BinarySearchTree(key)
            else:
                self.left.insert(key)
        elif key > self.data:
            if self.right is None:
                self.right = BinarySearchTree(key)
            else:
                self.right.insert(key)
        else:
            print(f"Node {key} already exists. Insertion skipped.")
    def delete(self, key):
        if self.data is None:
            print("Nothing to delete... Tree is empty.")
            return None
        if key < self.data:
            if self.left:
                self.left = self.left.delete(key)
            else:
                self._node_not_found(key)
        elif key > self.data:
            if self.right:
                self.right = self.right.delete(key)
            else:
                self._node_not_found(key)
        elif key == self.data:
            return self._delete_current_node()
        return self
    def _delete_current_node(self):
        if self.left is None:
            return self.right
        if self.right is None:
            return self.left
        min_node_value = self.right.find_min()
        self.data = min_node_value
        self.right = self.right.delete(min_node_value)
        return self
    def print_tree(self):
        if self.data is None:
            print("Nothing to print... Tree is empty.")
        else:
            if self.left:
                self.left.print_tree()
            print(self.data)
            if self.right:
                self.right.print_tree()
    def print_root(self):
        if self.data is not None:
            print(f"Root = {self.data}")
        else:
            print("Tree is empty.")
if __name__ == "__main__":
    bst = BinarySearchTree(20)
    bst.insert(12)
    bst.insert(34)
    bst.insert(21)
    bst.insert(56)
    bst.insert(23)
    bst.insert(16)
    bst.insert(14)
    bst.insert(19)
    bst.insert(24)
    print("Tree structure:")
    bst.print_tree()
    print("\nSearching elements:")
    bst.find(78)
    print(f"Minimum value in tree: {bst.find_min()}")
    print(f"Maximum value in tree: {bst.find_max()}")
    bst.find(21)
    bst.find(201)
    print("\nDeleting nodes:")
    bst.delete(243)
    bst.delete(20)
    bst.print_tree()
    bst.print_root()
    print("\nMaking tree empty:")
    bst.make_empty()
    bst.print_tree()
    print("\nInsertion after making tree empty:")
    bst.insert(16)
    bst.print_tree()
    bst.insert(14)
    bst.insert(19)
    bst.print_tree()
class BinarySearchTree:
    def __init__(self, data):
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
        if node.left is not None:
            node.left = self._recursive_make_empty(node.left)
        if node.right is not None:
            node.right = self._recursive_make_empty(node.right)
        del node
        return None
    def find(self, key):
        if self.data is None:
            return "Nothing to find... Tree is empty."
        elif key < self.data and self.left is not None:
            return self.left.find(key)
        elif key > self.data and self.right is not None:
            return self.right.find(key)
        elif key == self.data:
            print(f"Node {key}: Found.")
            return self.data
        else:
            print(f"Node {key}: Not found.")
            return None
    def find_min(self):
        if self.data is None:
            return "Nothing to find... Tree is empty."
        elif self.left is not None:
            return self.left.find_min()
        else:
            return self.data
    def find_max(self):
        if self.data is None:
            return "Nothing to find... Tree is empty."
        elif self.right is not None:
            return self.right.find_max()
        else:
            return self.data
    def insert(self, key):
        if self.data:
            if key < self.data:
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
                print("Couldn't insert the node, as the node already exists.")
        else:
            self.data = key
    def delete(self, key):
        if self.data is None:
            print("Nothing to delete... Tree is empty.")
            return None
        elif key < self.data and self.left is not None:
            self.left = self.left.delete(key)
        elif key > self.data and self.right is not None:
            self.right = self.right.delete(key)
        elif key == self.data:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            min_node_value = self.right.find_min()
            self.data = min_node_value
            self.right = self.right.delete(min_node_value)
        return self
    def print_tree(self):
        if self.data is None:
            print("Nothing to print... Tree is empty.")
        else:
            if self.left is not None:
                self.left.print_tree()
            print(self.data)
            if self.right is not None:
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
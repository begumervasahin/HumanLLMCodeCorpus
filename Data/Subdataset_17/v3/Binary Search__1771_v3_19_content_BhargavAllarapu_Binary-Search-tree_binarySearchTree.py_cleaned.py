class BinarySearchTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    def make_empty(self):
        if self.data is None:
            print("Tree is already empty ...")
            return
        self._recursive_make_empty()
        self.data = None
        print("Deleted every node ... Now the tree is empty")
    def _recursive_make_empty(self):
        if self.left is not None:
            self.left._recursive_make_empty()
            self.left = None
        if self.right is not None:
            self.right._recursive_make_empty()
            self.right = None
    def find(self, key):
        if self.data is None:
            print("Nothing to find... Tree is empty.")
            return None
        if key < self.data:
            return self.left.find(key) if self.left else None
        elif key > self.data:
            return self.right.find(key) if self.right else None
        else:
            print(f"Node {key}: Found.")
            return self.data
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
    def insert_node(self, key):
        if self.data is None:
            self.data = key
        elif key < self.data:
            if self.left is None:
                self.left = BinarySearchTree(key)
            else:
                self.left.insert_node(key)
        elif key > self.data:
            if self.right is None:
                self.right = BinarySearchTree(key)
            else:
                self.right.insert_node(key)
        else:
            print(f"Couldn't insert node {key}, because it already exists.")
    def delete_node(self, key):
        if self.data is None:
            print("Nothing to delete... Tree is empty.")
            return self
        if key < self.data:
            if self.left:
                self.left = self.left.delete_node(key)
        elif key > self.data:
            if self.right:
                self.right = self.right.delete_node(key)
        else:
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete_node(min_value)
        return self
    def print_tree(self):
        if self.data is None:
            print("Nothing to print... Tree is empty")
            return
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
    def print_root(self):
        if self.data:
            print("Root =", self.data)
        else:
            print("Tree is empty.")
if __name__ == "__main__":
    bst = BinarySearchTree(20)
    bst.insert_node(12)
    bst.insert_node(34)
    bst.insert_node(21)
    bst.insert_node(56)
    bst.insert_node(23)
    bst.insert_node(16)
    bst.insert_node(14)
    bst.insert_node(19)
    bst.insert_node(24)
    print("Tree structure:")
    bst.print_tree()
    print("\nSearching for elements:")
    bst.find(78)
    print("Minimum value in tree:", bst.find_min())
    print("Maximum value in tree:", bst.find_max())
    bst.find(21)
    bst.find(201)
    print("\nDeleting nodes:")
    bst.delete_node(243)
    bst.delete_node(20)
    print("\nTree structure after deletions:")
    bst.print_tree()
    bst.print_root()
    print("\nEmptying the tree:")
    bst.make_empty()
    bst.print_tree()
    print("\nInsertion after making tree empty:")
    bst.insert_node(16)
    bst.print_tree()
    bst.insert_node(14)
    bst.insert_node(19)
    bst.print_tree()
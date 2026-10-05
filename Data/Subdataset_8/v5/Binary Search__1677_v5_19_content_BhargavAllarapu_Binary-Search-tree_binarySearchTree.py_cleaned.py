class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def make_empty(self):
        if self.data is not None:
            self._recursive_make_empty(self)
            self.data = None
            print("Deleted every node. Now the tree is empty")
        else:
            print("The tree is already empty")
    def _recursive_make_empty(self, node):
        if node is None:
            return None
        node.left = self._recursive_make_empty(node.left)
        node.right = self._recursive_make_empty(node.right)
        del node
    def find(self, key):
        if self is None:
            return "Nothing to find. The tree is empty."
        if self.data == key:
            print("Node {} found.".format(key))
            return None
        elif self.data > key and self.left:
            return self.left.find(key)
        elif self.data < key and self.right:
            return self.right.find(key)
        else:
            print("Node {} not found.".format(key))
            return None
    def find_min(self):
        if self is None:
            return "Nothing to find. The tree is empty."
        if self.left:
            return self.left.find_min()
        else:
            return self.data
    def find_max(self):
        if self is None:
            return "Nothing to find. The tree is empty."
        if self.right:
            return self.right.find_max()
        else:
            return self.data
    def insert_a_node(self, key):
        if self.data:
            if self.data > key:
                if self.left is None:
                    self.left = BinarySearchTree(key)
                else:
                    return self.left.insert_a_node(key)
            elif self.data < key:
                if self.right is None:
                    self.right = BinarySearchTree(key)
                else:
                    return self.right.insert_a_node(key)
            else:
                print("Couldn't insert the node because the node already exists.")
        else:
            self.data = key
    def delete_a_node(self, key):
        if self is None:
            print("Nothing to delete. The tree is empty.")
        else:
            if self.data > key and self.left:
                self.left = self.left.delete_a_node(key)
            elif self.data < key and self.right:
                self.right = self.right.delete_a_node(key)
            elif self.data == key:
                if self.left is None:
                    new_node = self.right
                    del self
                    return new_node
                elif self.right is None:
                    new_node = self.left
                    del self
                    return new_node
                minimum_node = self.right.find_min()
                self.data = minimum_node
                self.right = self.right.delete_a_node(minimum_node)
            else:
                return self
            return self
    def print_tree(self):
        if self is None:
            print("Nothing to print. The tree is empty")
            return
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
    def print_root(self):
        if self:
            print("Root = {}".format(self.data))
        else:
            print("The tree is empty.")
if __name__ == "__main__":
    r = BinarySearchTree(20)
    nodes_to_insert = [12, 34, 21, 56, 23, 16, 14, 19, 24]
    for node in nodes_to_insert:
        r.insert_a_node(node)
    r.print_tree()
    print("Element: {}".format(r.find(78)))
    print("Minimum value in tree is: {}".format(r.find_min()))
    print("Maximum value in tree is: {}".format(r.find_max()))
    r.find(21)
    r.find(201)
    r.delete_a_node(243)
    r.delete_a_node(20)
    r.print_tree()
    r.print_root()
    r.make_empty()
    r.print_tree()
    print("Insertion after making tree empty")
    r.insert_a_node(16)
    r.print_tree()
    r.insert_a_node(14)
    r.insert_a_node(19)
    r.print_tree()
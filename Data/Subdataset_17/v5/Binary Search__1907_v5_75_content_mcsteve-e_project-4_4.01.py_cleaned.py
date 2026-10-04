
class BinarySearchTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    def __init__(self):
        self.root = None
    def pretty_print(self):
        self._pretty_print_aux(self.root, 0)
    def _pretty_print_aux(self, node, indent_level):
        if node is None:
            return
        if node.right:
            self._pretty_print_aux(node.right, indent_level + 1)
        print("    " * indent_level + str(node.value))
        if node.left:
            self._pretty_print_aux(node.left, indent_level + 1)
    def find(self, target):
        return self._find_aux(self.root, target)
    def _find_aux(self, node, target):
        if node is None:
            return None
        if target == node.value:
            return node
        elif target < node.value:
            return self._find_aux(node.left, target)
        else:
            return self._find_aux(node.right, target)
    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._insert_aux(self.root, value)
    def _insert_aux(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._insert_aux(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._insert_aux(node.right, value)
    def flip(self):
        self._flip_aux(self.root)
    def _flip_aux(self, node):
        if node:
            node.left, node.right = node.right, node.left
            self._flip_aux(node.left)
            self._flip_aux(node.right)
def main():
    tree = BinarySearchTree()
    values = ["man", "dog", "zebra", "ape", "elephant", "yak", "zorse", "fly"]
    for value in values:
        tree.insert(value)
    print("Original tree:")
    tree.pretty_print()
    tree.flip()
    print("\nFlipped tree:")
    tree.pretty_print()
if __name__ == "__main__":
    main()

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
    def attach_in_order(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._attach_in_order_aux(self.root, value)
    def _attach_in_order_aux(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._attach_in_order_aux(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._attach_in_order_aux(node.right, value)
    def flip(self):
        self._flip_aux(self.root)
    def _flip_aux(self, node):
        if node:
            node.left, node.right = node.right, node.left
            self._flip_aux(node.left)
            self._flip_aux(node.right)
def main():
    tree = BinarySearchTree()
    tree.root = BinarySearchTree.Node("man")
    tree.attach_in_order("dog")
    tree.attach_in_order("zebra")
    tree.attach_in_order("ape")
    tree.attach_in_order("elephant")
    tree.attach_in_order("yak")
    tree.attach_in_order("zorse")
    tree.attach_in_order("fly")
    tree.pretty_print()
if __name__ == "__main__":
    main()
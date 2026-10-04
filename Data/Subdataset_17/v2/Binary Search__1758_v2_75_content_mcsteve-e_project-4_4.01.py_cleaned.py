class BST:
    class Node:
        def __init__(self, payload):
            self.payload = payload
            self.left = None
            self.right = None
    def __init__(self):
        self.root = None
    def prettyprint(self):
        self._prettyprint_aux(self.root, 0)
    def _prettyprint_aux(self, node, indent_level):
        if node is not None:
            if node.right is not None:
                self._prettyprint_aux(node.right, indent_level + 1)
            print("    " * indent_level + str(node.payload))
            if node.left is not None:
                self._prettyprint_aux(node.left, indent_level + 1)
    def find(self, target):
        return self._find_aux(self.root, target)
    def _find_aux(self, node, target):
        if node is None:
            return None
        if node.payload == target:
            return node
        elif target < node.payload:
            return self._find_aux(node.left, target)
        else:
            return self._find_aux(node.right, target)
    def attach_in_order(self, new_value):
        if self.root is None:
            self.root = BST.Node(new_value)
        else:
            self._attach_in_order_aux(self.root, new_value)
    def _attach_in_order_aux(self, node, new_value):
        if new_value < node.payload:
            if node.left is None:
                node.left = BST.Node(new_value)
            else:
                self._attach_in_order_aux(node.left, new_value)
        elif new_value > node.payload:
            if node.right is None:
                node.right = BST.Node(new_value)
            else:
                self._attach_in_order_aux(node.right, new_value)
    def flip(self):
        self._flip_aux(self.root)
    def _flip_aux(self, node):
        if node is not None:
            node.left, node.right = node.right, node.left
            self._flip_aux(node.left)
            self._flip_aux(node.right)
def main():
    tree = BST()
    tree.root = BST.Node("man")
    root_node = tree.find("man")
    if root_node:
        root_node.left = BST.Node("dog")
        root_node.right = BST.Node("zebra")
    tree.attach_in_order("ape")
    tree.attach_in_order("elephant")
    tree.attach_in_order("yak")
    tree.attach_in_order("zorse")
    tree.attach_in_order("fly")
    print("Tree before flipping:")
    tree.prettyprint()
    tree.flip()
    print("\nTree after flipping:")
    tree.prettyprint()
if __name__ == "__main__":
    main()
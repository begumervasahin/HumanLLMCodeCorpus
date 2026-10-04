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
    def _find_aux(self, treeptr, target):
        if treeptr is None:
            return None
        if treeptr.payload == target:
            return treeptr
        elif target < treeptr.payload:
            return self._find_aux(treeptr.left, target)
        else:
            return self._find_aux(treeptr.right, target)
    def attach_in_order(self, new_value):
        if self.root is None:
            self.root = BST.Node(new_value)
        else:
            self._attach_in_order_aux(self.root, new_value)
    def _attach_in_order_aux(self, treeptr, new_value):
        if new_value < treeptr.payload:
            if treeptr.left is None:
                treeptr.left = BST.Node(new_value)
            else:
                self._attach_in_order_aux(treeptr.left, new_value)
        elif new_value > treeptr.payload:
            if treeptr.right is None:
                treeptr.right = BST.Node(new_value)
            else:
                self._attach_in_order_aux(treeptr.right, new_value)
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
    somenode = tree.find("man")
    if somenode:
        somenode.left = BST.Node("dog")
        somenode.right = BST.Node("zebra")
    tree.attach_in_order("ape")
    tree.attach_in_order("elephant")
    tree.attach_in_order("yak")
    tree.attach_in_order("zorse")
    tree.attach_in_order("fly")
    tree.prettyprint()
if __name__ == "__main__":
    main()
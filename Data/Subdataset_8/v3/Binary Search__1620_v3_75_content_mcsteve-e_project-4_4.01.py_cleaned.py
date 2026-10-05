class BinarySearchTree:
    class Node:
        def __init__(self, payload):
            self.payload = payload
            self.left = None
            self.right = None
    def __init__(self):
        self.root = None
    def pretty_print(self):
        self._pretty_print_aux(self.root, 0)
    def _pretty_print_aux(self, current_node, indent_level):
        if current_node is not None:
            self._pretty_print_aux(current_node.right, indent_level + 1)
            print("    " * indent_level + str(current_node.payload))
            self._pretty_print_aux(current_node.left, indent_level + 1)
    def find(self, target):
        return self._find_aux(self.root, target)
    def _find_aux(self, current_node, target):
        if current_node is None or current_node.payload == target:
            return current_node
        elif target < current_node.payload:
            return self._find_aux(current_node.left, target)
        else:
            return self._find_aux(current_node.right, target)
    def attach_in_order(self, new_value):
        self.root = self._attach_in_order_aux(self.root, new_value)
    def _attach_in_order_aux(self, current_node, new_value):
        if current_node is None:
            return self.Node(new_value)
        if new_value < current_node.payload:
            current_node.left = self._attach_in_order_aux(current_node.left, new_value)
        elif new_value > current_node.payload:
            current_node.right = self._attach_in_order_aux(current_node.right, new_value)
        return current_node
    def flip(self):
        self._flip_aux(self.root)
    def _flip_aux(self, current_node):
        if current_node is not None:
            current_node.left, current_node.right = current_node.right, current_node.left
            self._flip_aux(current_node.left)
            self._flip_aux(current_node.right)
def main():
    bst = BinarySearchTree()
    bst.attach_in_order("man")
    bst.attach_in_order("dog")
    bst.attach_in_order("zebra")
    bst.attach_in_order("ape")
    bst.attach_in_order("elephant")
    bst.attach_in_order("yak")
    bst.attach_in_order("zorse")
    bst.attach_in_order("fly")
    bst.pretty_print()
if __name__ == "__main__":
    main()

class BST:
    class Node:
        def __init__(self, payload):
            self.payload = payload
            self.left = None
            self.right = None
    def __init__(self):
        self.root = None
    def pretty_print(self):
        BST.pretty_print_aux(self.root, 0)
    @staticmethod
    def pretty_print_aux(some_node, indent_level):
        if some_node.right:
            BST.pretty_print_aux(some_node.right, indent_level + 1)
        for _ in range(indent_level):
            print("    ", end="")
        print(some_node.payload)
        print()
        if some_node.left:
            BST.pretty_print_aux(some_node.left, indent_level + 1)
    def find(self, target):
        return BST.find_aux(self.root, target)
    @staticmethod
    def find_aux(tree_ptr, target):
        if tree_ptr is None:
            return None
        if tree_ptr.payload == target:
            return tree_ptr
        elif target < tree_ptr.payload:
            return BST.find_aux(tree_ptr.left, target)
        else:
            return BST.find_aux(tree_ptr.right, target)
    def attach_in_order(self, new_value):
        if self.root is None:
            self.root = BST.Node(new_value)
        else:
            BST.attach_in_order_aux(self.root, new_value)
    @staticmethod
    def attach_in_order_aux(tree_ptr, new_value):
        if new_value < tree_ptr.payload:
            if tree_ptr.left is None:
                tree_ptr.left = BST.Node(new_value)
            else:
                BST.attach_in_order_aux(tree_ptr.left, new_value)
        elif new_value > tree_ptr.payload:
            if tree_ptr.right is None:
                tree_ptr.right = BST.Node(new_value)
            else:
                BST.attach_in_order_aux(tree_ptr.right, new_value)
    def flip(self):
        BST.flip_aux(self.root)
    @staticmethod
    def flip_aux(some_node):
        pass
def main():
    tree = BST()
    tree.root = BST.Node("man")
    some_node = tree.find("man")
    some_node.left = BST.Node("dog")
    some_node.right = BST.Node("zebra")
    tree.attach_in_order("ape")
    tree.attach_in_order("elephant")
    tree.attach_in_order("yak")
    tree.attach_in_order("zorse")
    tree.attach_in_order("fly")
    tree.pretty_print()
if __name__ == "__main__":
    main()
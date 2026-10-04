
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left
    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
    def check_binary_search_tree_iterative(self):
        stack = [(self, -float('inf'), float('inf'))]
        while stack:
            node, lower_bound, upper_bound = stack.pop()
            if not lower_bound < node.value < upper_bound:
                return False
            if node.left:
                stack.append((node.left, lower_bound, node.value))
            if node.right:
                stack.append((node.right, node.value, upper_bound))
        return True
    def check_bst_recursive(self, node, lower_bound, upper_bound):
        if not node:
            return True
        if not lower_bound < node.value < upper_bound:
            return False
        return (self.check_bst_recursive(node.left, lower_bound, node.value) and
                self.check_bst_recursive(node.right, node.value, upper_bound))
if __name__ == "__main__":
    bt = BinaryTreeNode(5)
    bt.insert_left(3)
    bt.insert_right(7)
    bt.left.insert_left(1)
    bt.left.insert_right(9)
    print("Iterative check:", bt.check_binary_search_tree_iterative())
    print("Recursive check:", bt.check_bst_recursive(bt, -float('inf'), float('inf')))

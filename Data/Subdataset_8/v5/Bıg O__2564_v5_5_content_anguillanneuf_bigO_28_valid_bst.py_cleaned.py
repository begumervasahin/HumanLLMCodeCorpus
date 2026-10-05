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
    def is_binary_search_tree_iterative(self):
        stack = []
        stack.append((self, float('-inf'), float('inf')))
        while stack:
            node, lower_bound, upper_bound = stack.pop()
            if not lower_bound < node.value < upper_bound:
                return False
            if node.left:
                stack.append((node.left, lower_bound, node.value))
            if node.right:
                stack.append((node.right, node.value, upper_bound))
        return True
    @staticmethod
    def is_binary_search_tree_recursive(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        if not lower < node.value < upper:
            return False
        return (
            BinaryTreeNode.is_binary_search_tree_recursive(node.left, lower, node.value)
            and BinaryTreeNode.is_binary_search_tree_recursive(node.right, node.value, upper)
        )
bt = BinaryTreeNode(5)
bt.insert_left(3)
bt.insert_right(7)
bt.left.insert_left(1)
bt.left.insert_right(4)
print("Iterative approach:", bt.is_binary_search_tree_iterative())
print("Recursive approach:", BinaryTreeNode.is_binary_search_tree_recursive(bt))
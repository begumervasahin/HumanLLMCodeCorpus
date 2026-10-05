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
        stack = []
        stack.append((self, -float('inf'), float('inf')))
        while stack:
            node, lower, upper = stack.pop()
            if not lower < node.value < upper:
                return False
            if node.left:
                stack.append((node.left, lower, node.value))
            if node.right:
                stack.append((node.right, node.value, upper))
        return True
    def check_bst_recursive(self, node=None, lower=-float('inf'), upper=float('inf')):
        if node is None:
            node = self
        if not node:
            return True
        if not lower < node.value < upper:
            return False
        return self.check_bst_recursive(node.left, lower, node.value) and \
               self.check_bst_recursive(node.right, node.value, upper)
bt = BinaryTreeNode(5)
bt.insert_left(3)
bt.insert_right(7)
bt.left.insert_left(1)
bt.left.insert_right(4)
print("Iterative Check:", bt.check_binary_search_tree_iterative())
print("Recursive Check:", bt.check_bst_recursive())

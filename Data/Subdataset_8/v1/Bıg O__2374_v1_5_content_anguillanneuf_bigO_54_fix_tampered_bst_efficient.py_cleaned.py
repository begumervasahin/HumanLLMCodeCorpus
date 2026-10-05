class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.wrong1 = None
        self.wrong2 = None
        self.lastNode = None
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)
    def fix_swap(self, node):
        if not node:
            return
        if node.left:
            self.fix_swap(node.left)
        if not self.wrong1:
            if self.lastNode and node.value < self.lastNode.value:
                self.wrong1 = self.lastNode
                self.wrong2 = node
        else:
            if self.wrong2:
                if node.value < self.wrong2.value:
                    self.wrong2 = node
        self.lastNode = node
        if node.right:
            self.fix_swap(node.right)
    def swap(self, root):
        self.fix_swap(root)
        self.wrong1.value, self.wrong2.value = self.wrong2.value, self.wrong1.value
bt = BinaryTreeNode(7)
bt.left = BinaryTreeNode(4)
bt.left.left = BinaryTreeNode(1)
bt.left.right = BinaryTreeNode(5)
bt.right = BinaryTreeNode(11)
bt.value, bt.left.left.value = bt.left.left.value, bt.value
print("In-order traversal before swapping:")
bt.in_order(bt)
print("\nIn-order traversal after swapping:")
bt.swap(bt)
bt.in_order(bt)
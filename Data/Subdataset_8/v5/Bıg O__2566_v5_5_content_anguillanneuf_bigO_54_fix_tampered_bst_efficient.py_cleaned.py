class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def in_order_traversal(self, node=None):
        if node is None:
            node = self
        if node.left:
            self.in_order_traversal(node.left)
        print(node.value)
        if node.right:
            self.in_order_traversal(node.right)
    def find_swapped_nodes(self, node=None):
        if node is None:
            node = self
        if not node:
            return
        self.find_swapped_nodes(node.left)
        if not self.wrong1:
            if self.lastNode and node.value < self.lastNode.value:
                self.wrong1 = self.lastNode
                self.wrong2 = node
        else:
            if self.wrong2:
                if node.value < self.wrong2.value:
                    self.wrong2 = node
        self.lastNode = node
        self.find_swapped_nodes(node.right)
    def swap_wrongly_placed_nodes(self, root=None):
        if root is None:
            root = self
        self.find_swapped_nodes(root)
        if self.wrong1 and self.wrong2:
            self.wrong1.value, self.wrong2.value = self.wrong2.value, self.wrong1.value
bt = BinaryTreeNode(7)
bt.left = BinaryTreeNode(4)
bt.left.left = BinaryTreeNode(1)
bt.left.right = BinaryTreeNode(5)
bt.right = BinaryTreeNode(11)
print("Original In-order Traversal:")
bt.in_order_traversal()
bt.swap_wrongly_placed_nodes()
print("In-order Traversal after Swapping:")
bt.in_order_traversal()
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.wrong1 = None
        self.wrong2 = None
        self.last_node = None
    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.value)
            self.in_order_traversal(node.right)
    def find_swapped_nodes(self, node):
        if not node:
            return
        if node.left:
            self.find_swapped_nodes(node.left)
        if not self.wrong1:
            if self.last_node and node.value < self.last_node.value:
                self.wrong1 = self.last_node
                self.wrong2 = node
        else:
            if self.wrong2:
                if node.value < self.wrong2.value:
                    self.wrong2 = node
        self.last_node = node
        if node.right:
            self.find_swapped_nodes(node.right)
    def swap_wrongly_swapped_nodes(self, root):
        self.find_swapped_nodes(root)
        self.wrong1.value, self.wrong2.value = self.wrong2.value, self.wrong1.value
bt = BinaryTreeNode(7)
bt.left = BinaryTreeNode(4)
bt.left.left = BinaryTreeNode(1)
bt.left.right = BinaryTreeNode(5)
bt.right = BinaryTreeNode(11)
bt.value, bt.left.left.value = bt.left.left.value, bt.value
print("In-order traversal before swapping:")
bt.in_order_traversal(bt)
print("\nIn-order traversal after swapping:")
bt.swap_wrongly_swapped_nodes(bt)
bt.in_order_traversal(bt)
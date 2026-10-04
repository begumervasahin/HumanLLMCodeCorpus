
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.wrong1 = None
        self.wrong2 = None
        self.last_node = None
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value, end=" ")
            self.in_order(node.right)
    def fix_swap(self, node):
        if not node:
            return
        self.fix_swap(node.left)
        if self.last_node and node.value < self.last_node.value:
            if not self.wrong1:
                self.wrong1 = self.last_node
            self.wrong2 = node
        self.last_node = node
        self.fix_swap(node.right)
    def swap(self, root):
        self.fix_swap(root)
        if self.wrong1 and self.wrong2:
            self.wrong1.value, self.wrong2.value = self.wrong2.value, self.wrong1.value
if __name__ == "__main__":
    bt = BinaryTreeNode(7)
    bt.left = BinaryTreeNode(4)
    bt.left.left = BinaryTreeNode(1)
    bt.left.right = BinaryTreeNode(5)
    bt.right = BinaryTreeNode(11)
    bt.value, bt.left.left.value = bt.left.left.value, bt.value
    print("Before fixing the swap:")
    tree = BinaryTree()
    tree.in_order(bt)
    print()
    tree.swap(bt)
    print("After fixing the swap:")
    tree.in_order(bt)
    print()
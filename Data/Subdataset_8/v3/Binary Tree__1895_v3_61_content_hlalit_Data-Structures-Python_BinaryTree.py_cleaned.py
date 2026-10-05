class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
        self.node_list = []
    def add_node(self, data):
        self.node_list.append(data)
    def build_tree(self):
        self.root = self._build_tree_recursive(0)
    def _build_tree_recursive(self, index):
        if index >= len(self.node_list):
            return None
        node = TreeNode(self.node_list[index])
        node.left = self._build_tree_recursive(2 * index + 1)
        node.right = self._build_tree_recursive(2 * index + 2)
        return node
    def inorder_traversal(self, node):
        if node is None:
            return
        self.inorder_traversal(node.left)
        print(node.data)
        self.inorder_traversal(node.right)
    def level_order_traversal(self, node):
        if node is None:
            return
        queue = [node]
        while queue:
            current = queue.pop(0)
            print(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    def get_height(self, node):
        if node is None:
            return -1
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return max(left_height, right_height) + 1
binary_tree = BinaryTree()
binary_tree.add_node(2)
binary_tree.add_node(3)
binary_tree.add_node(5)
binary_tree.add_node(7)
binary_tree.add_node(1)
binary_tree.add_node(10)
binary_tree.add_node(9)
binary_tree.add_node(8)
binary_tree.build_tree()
print("Inorder Traversal:")
binary_tree.inorder_traversal(binary_tree.root)
print("\nLevel Order Traversal:")
binary_tree.level_order_traversal(binary_tree.root)
print("\nHeight of the tree:", binary_tree.get_height(binary_tree.root))
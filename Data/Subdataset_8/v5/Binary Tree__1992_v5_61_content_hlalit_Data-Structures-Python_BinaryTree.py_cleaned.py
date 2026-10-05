class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert_list(self, data_list):
        self.root = self._insert_tree(data_list, self.root, 0)
    def _insert_tree(self, data_list, current, index):
        if index < len(data_list):
            if data_list[index] is not None:
                new_node = Node(data_list[index])
                current = new_node
                current.left = self._insert_tree(data_list, current.left, 2 * index + 1)
                current.right = self._insert_tree(data_list, current.right, 2 * index + 2)
        return current
    def inorder_traversal(self, current):
        if current is None:
            return
        self.inorder_traversal(current.left)
        print(current.data)
        self.inorder_traversal(current.right)
    def level_order_traversal(self, current):
        if current is None:
            return
        queue = [current]
        while queue:
            node = queue.pop(0)
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    def calculate_height(self, current):
        if current is None:
            return -1
        left_height = self.calculate_height(current.left)
        right_height = self.calculate_height(current.right)
        return max(left_height, right_height) + 1
binary_tree = BinaryTree()
binary_tree.insert_list([2, 3, 5, 7, 1, 10, 9, 8])
binary_tree.inorder_traversal(binary_tree.root)
print()
binary_tree.level_order_traversal(binary_tree.root)
print()
print(binary_tree.calculate_height(binary_tree.root))
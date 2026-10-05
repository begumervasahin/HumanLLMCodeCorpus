class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        self.root = self._insert(self.root, data)
    def _insert(self, root, data):
        if root is None:
            return TreeNode(data)
        else:
            if data <= root.data:
                root.left = self._insert(root.left, data)
            else:
                root.right = self._insert(root.right, data)
        return root
    def get_height(self):
        return self._get_height(self.root)
    def _get_height(self, root):
        if root is None:
            return -1
        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)
        return max(left_height, right_height) + 1
    def inorder_traversal(self):
        self._inorder_traversal(self.root)
        print()
    def _inorder_traversal(self, root):
        if root is not None:
            self._inorder_traversal(root.left)
            print(root.data, end=" ")
            self._inorder_traversal(root.right)
    def postorder_traversal(self):
        self._postorder_traversal(self.root)
        print()
    def _postorder_traversal(self, root):
        if root is not None:
            self._postorder_traversal(root.left)
            self._postorder_traversal(root.right)
            print(root.data, end=" ")
    def preorder_traversal(self):
        self._preorder_traversal(self.root)
        print()
    def _preorder_traversal(self, root):
        if root is not None:
            print(root.data, end=" ")
            self._preorder_traversal(root.left)
            self._preorder_traversal(root.right)
    def level_order_traversal(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
binary_tree = BinaryTree()
values = [5, 3, 7, 2, 4, 6, 8]
for value in values:
    binary_tree.insert(value)
print("Inorder traversal:", end=" ")
binary_tree.inorder_traversal()
print("Postorder traversal:", end=" ")
binary_tree.postorder_traversal()
print("Preorder traversal:", end=" ")
binary_tree.preorder_traversal()
print("Level order traversal:", end=" ")
binary_tree.level_order_traversal()
print("Height of the tree:", binary_tree.get_height())
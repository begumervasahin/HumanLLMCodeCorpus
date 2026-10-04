class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        return root
    def get_height(self, root):
        if root is None:
            return -1
        else:
            left_height = self.get_height(root.left)
            right_height = self.get_height(root.right)
            return max(left_height, right_height) + 1
    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.data, end=" ")
            self.in_order(root.right)
    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data, end=" ")
    def pre_order(self, root):
        if root:
            print(root.data, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)
    def level_order(self, root):
        if root:
            queue = [root]
            while queue:
                current = queue.pop(0)
                print(current.data, end=" ")
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
if __name__ == "__main__":
    tree = Tree()
    root = None
    data_values = [5, 3, 8, 2, 4, 7, 9]
    for data in data_values:
        root = tree.insert(root, data)
    print("InOrder Traversal: ", end="")
    tree.in_order(root)
    print("\nPostOrder Traversal: ", end="")
    tree.post_order(root)
    print("\nPreOrder Traversal: ", end="")
    tree.pre_order(root)
    print("\nLevelOrder Traversal: ", end="")
    tree.level_order(root)
    print("\nTree Height:", tree.get_height(root))
class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
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
    def getHeight(self, root):
        if root is None:
            return -1
        else:
            left_height = self.getHeight(root.left)
            right_height = self.getHeight(root.right)
            return max(left_height, right_height) + 1
    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            print(root.data, end=" ")
            self.inOrder(root.right)
    def postOrder(self, root):
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data, end=" ")
    def preOrder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)
    def levelOrder(self, root):
        if root is None:
            return
        queue = [root]
        while queue:
            cur = queue.pop(0)
            print(cur.data, end=" ")
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
if __name__ == "__main__":
    tree = Tree()
    root = None
    data_values = [3, 5, 2, 1, 4, 6, 7]
    for data in data_values:
        root = tree.insert(root, data)
    print("In-order traversal:")
    tree.inOrder(root)
    print("\nPost-order traversal:")
    tree.postOrder(root)
    print("\nPre-order traversal:")
    tree.preOrder(root)
    print("\nLevel-order traversal:")
    tree.levelOrder(root)
    print("\nHeight of tree:", tree.getHeight(root))
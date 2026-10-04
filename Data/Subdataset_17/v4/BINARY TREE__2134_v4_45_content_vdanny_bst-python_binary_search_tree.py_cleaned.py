import sys
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
            sys.stdout.write(str(root.data) + " ")
            sys.stdout.flush()
            self.inOrder(root.right)
    def postOrder(self, root):
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            sys.stdout.write(str(root.data) + " ")
            sys.stdout.flush()
    def preOrder(self, root):
        if root is not None:
            sys.stdout.write(str(root.data) + " ")
            sys.stdout.flush()
            self.preOrder(root.left)
            self.preOrder(root.right)
    def levelOrder(self, root):
        if root is not None:
            queue = [root]
            i = 0
            while i < len(queue):
                cur = queue[i]
                sys.stdout.write(str(cur.data) + " ")
                sys.stdout.flush()
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                i += 1
if __name__ == "__main__":
    tree = Tree()
    root = None
    data_values = [5, 3, 8, 2, 4, 7, 9]
    for data in data_values:
        root = tree.insert(root, data)
    print("InOrder Traversal: ", end="")
    tree.inOrder(root)
    print("\nPostOrder Traversal: ", end="")
    tree.postOrder(root)
    print("\nPreOrder Traversal: ", end="")
    tree.preOrder(root)
    print("\nLevelOrder Traversal: ", end="")
    tree.levelOrder(root)
    print("\nTree Height:", tree.getHeight(root))
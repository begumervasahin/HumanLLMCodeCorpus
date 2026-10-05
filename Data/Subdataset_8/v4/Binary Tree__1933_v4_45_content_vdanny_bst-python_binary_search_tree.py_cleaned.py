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
        if root:
            self.inOrder(root.left)
            sys.stdout.write(str(root.data) + " ")
            self.inOrder(root.right)
    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            sys.stdout.write(str(root.data) + " ")
    def preOrder(self, root):
        if root:
            sys.stdout.write(str(root.data) + " ")
            self.preOrder(root.left)
            self.preOrder(root.right)
    def levelOrder(self, root):
        if root:
            queue = [root]
            while queue:
                current = queue.pop(0)
                sys.stdout.write(str(current.data) + " ")
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
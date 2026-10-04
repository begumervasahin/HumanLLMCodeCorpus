import sys
class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data
class Tree:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root
    def getHeight(self, root):
        if root is None:
            return -1
        else:
            left = self.getHeight(root.left)
            right = self.getHeight(root.right)
            if left > right:
                return left + 1
            else:
                return right + 1
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
        queue = []
        if root is not None:
            queue.append(root)
            i = 0
            cur = queue[i]
            while cur is not None:
                sys.stdout.write(str(cur.data) + " ")
                sys.stdout.flush()
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                i += 1
                if i < len(queue):
                    cur = queue[i]
                else:
                    cur = None
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
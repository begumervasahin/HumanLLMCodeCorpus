import sys
class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data
class Tree:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root
    def getHeight(self,root):
        if root == None:
            return -1
        else:
            left = self.getHeight(root.left)
            right = self.getHeight(root.right)
            if left > right:
                return left + 1
            else:
                return right + 1
    def inOrder(self, root):
        if root != None:
            self.inOrder(root.left)
            sys.stdout.write(str(root.data) + " ")
            sys.stdout.flush()
            self.inOrder(root.right)
    def postOrder(self, root):
        if root != None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            sys.stdout.write(str(root.data) + " ")
            sys.stdout.flush()
    def preOrder(self, root):
        if root != None:
            sys.stdout.write(str(root.data) + " ")
            sys.stdout.flush()
            self.preOrder(root.left)
            self.preOrder(root.right)
    queue = []
    def levelOrder(self, root):
        if root != None:
            self.queue.append(root)
            i = 0
            cur = self.queue[i]
            while cur != None:
                sys.stdout.write(str(cur.data) + " ")
                sys.stdout.flush()
                if cur.left != None:
                    self.queue.append(cur.left)
                if cur.right != None:
                    self.queue.append(cur.right)
                i+=1
                if i < len(self.queue):
                    cur = self.queue[i]
                else:
                    cur = None
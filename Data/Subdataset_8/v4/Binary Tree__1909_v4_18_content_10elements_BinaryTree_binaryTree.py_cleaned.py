from .treeNode import treeNode
from collections import deque
class binaryTree(object):
    def __init__(self, data=None):
        if data is None:
            self.root = None
        else:
            try:
                self.root = binaryTree.serialize(data)
            except Exception as e:
                raise e
    def __iter__(self):
        return self.preOrderIter()
    @staticmethod
    def serialize(data):
        if data is None:
            raise TypeError('Input cannot be None')
        if not isinstance(data, str):
            raise TypeError('Input must be a string')
        if len(data) < 3 or not data.startswith('[') or not data.endswith(']'):
            raise TypeError('Input must be surrounded by brackets and cannot be empty')
        data = data[1:-1]
        datas = data.split(', ')
        if datas[0] == '':
            return None
        i = 1
        l = len(datas)
        root = treeNode(datas[0])
        frontier = [root]
        while i < l:
            t = []
            for n in frontier:
                if datas[i] != '':
                    n.left = treeNode(datas[i])
                    t.append(n.left)
                i += 1
                if datas[i] != '':
                    n.right = treeNode(datas[i])
                    t.append(n.right)
                i += 1
            frontier = t
        return root
    def inOrderIter(self):
        if self.root:
            stack = [self.root]
            visited = {}
            while len(stack):
                cur = stack[-1]
                if not cur.left or cur.left in visited:
                    stack.pop()
                    visited[cur] = True
                    yield cur.val
                    if cur.right:
                        stack.append(cur.right)
                else:
                    stack.append(cur.left)
        raise StopIteration
    def preOrderIter(self):
        if self.root:
            stack = [self.root]
            while len(stack):
                cur = stack.pop()
                yield cur.val
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        raise StopIteration
    def postOrderIter(self):
        if self.root:
            stack = [self.root]
            visited = {}
            while len(stack):
                cur = stack[-1]
                if (not cur.left or cur.left in visited) and (not cur.right or cur.right in visited):
                    stack.pop()
                    visited[cur] = True
                    yield cur.val
                elif cur.left and cur.left not in visited:
                    stack.append(cur.left)
                else:
                    stack.append(cur.right)
        raise StopIteration
    def bfsIter(self):
        if self.root:
            queue = deque([self.root])
            while len(queue):
                front = queue.popleft()
                yield front.val
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
        raise StopIteration
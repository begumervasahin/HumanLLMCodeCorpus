from collections import deque
from .treeNode import TreeNode
class BinaryTree:
    def __init__(self, data=None):
        if data is None:
            self.root = None
        else:
            try:
                self.root = self.deserialize(data)
            except Exception as e:
                raise e
    def __iter__(self):
        return self.pre_order_iter()
    @staticmethod
    def deserialize(data):
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
        root = TreeNode(datas[0])
        frontier = [root]
        while i < l:
            next_frontier = []
            for node in frontier:
                if datas[i] != '':
                    node.left = TreeNode(datas[i])
                    next_frontier.append(node.left)
                i += 1
                if datas[i] != '':
                    node.right = TreeNode(datas[i])
                    next_frontier.append(node.right)
                i += 1
            frontier = next_frontier
        return root
    def in_order_iter(self):
        if self.root:
            stack = [self.root]
            visited = {}
            while stack:
                current = stack[-1]
                if (not current.left or current.left in visited) and (not current.right or current.right in visited):
                    stack.pop()
                    visited[current] = True
                    yield current.val
                elif current.left and current.left not in visited:
                    stack.append(current.left)
                else:
                    stack.append(current.right)
        raise StopIteration
    def pre_order_iter(self):
        if self.root:
            stack = [self.root]
            while stack:
                current = stack.pop()
                yield current.val
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
        raise StopIteration
    def post_order_iter(self):
        if self.root:
            stack = [self.root]
            visited = {}
            while stack:
                current = stack[-1]
                if (not current.left or current.left in visited) and (not current.right or current.right in visited):
                    stack.pop()
                    visited[current] = True
                    yield current.val
                elif current.right and current.right not in visited:
                    stack.append(current.right)
                elif current.left and current.left not in visited:
                    stack.append(current.left)
        raise StopIteration
    def bfs_iter(self):
        if self.root:
            queue = deque([self.root])
            while queue:
                front = queue.popleft()
                yield front.val
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
        raise StopIteration
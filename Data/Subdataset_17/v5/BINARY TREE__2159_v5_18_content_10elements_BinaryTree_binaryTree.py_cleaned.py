from collections import deque
from .treeNode import treeNode
class BinaryTree:
    def __init__(self, data=None):
        self.root = self._deserialize(data) if data else None
    def __iter__(self):
        return self.pre_order_iter()
    @staticmethod
    def _deserialize(data):
        if not isinstance(data, str):
            raise TypeError('Input must be a string')
        if not data.startswith('[') or not data.endswith(']'):
            raise ValueError('Input must be surrounded by brackets and cannot be empty')
        data = data[1:-1].split(', ')
        if data[0] == 'null':
            return None
        root = treeNode(data[0])
        frontier = [root]
        i = 1
        while i < len(data):
            temp = []
            for node in frontier:
                if i < len(data) and data[i] != 'null':
                    node.left = treeNode(data[i])
                    temp.append(node.left)
                i += 1
                if i < len(data) and data[i] != 'null':
                    node.right = treeNode(data[i])
                    temp.append(node.right)
                i += 1
            frontier = temp
        return root
    def in_order_iter(self):
        if not self.root:
            return
        stack, visited = [self.root], set()
        while stack:
            current = stack[-1]
            if not current.left or current.left in visited:
                stack.pop()
                visited.add(current)
                yield current.val
                if current.right:
                    stack.append(current.right)
            else:
                stack.append(current.left)
        raise StopIteration
    def pre_order_iter(self):
        if not self.root:
            return
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
        if not self.root:
            return
        stack, visited = [self.root], set()
        while stack:
            current = stack[-1]
            if (not current.left or current.left in visited) and (not current.right or current.right in visited):
                stack.pop()
                visited.add(current)
                yield current.val
            elif current.left and current.left not in visited:
                stack.append(current.left)
            else:
                stack.append(current.right)
        raise StopIteration
    def bfs_iter(self):
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            front = queue.popleft()
            yield front.val
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)
        raise StopIteration
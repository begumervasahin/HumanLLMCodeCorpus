from collections import deque
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue = deque([root])
        tree = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                for child in node.children:
                    queue.append(child)
            tree.append(level)
        return tree

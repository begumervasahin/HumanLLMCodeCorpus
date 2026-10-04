class Solution(object):
    def postorderTraversal(self, root):
        result = []
        stack = []
        node = root
        visited = set()
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and not(node.right in visited):
                    stack.append(node)
                    node = node.right
                else:
                    visited.add(node)
                    result.append(node.val)
                    node = None
        return result
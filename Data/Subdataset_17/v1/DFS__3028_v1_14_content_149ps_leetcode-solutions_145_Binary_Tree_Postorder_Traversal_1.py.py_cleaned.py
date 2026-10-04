class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
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
                if node.right and not (node.right in visited):
                    stack.append(node)
                    node = node.right
                else:
                    visited.add(node)
                    result.append(node.val)
                    node = None
        return result
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
solution = Solution()
result = solution.postorderTraversal(root)
print(result)

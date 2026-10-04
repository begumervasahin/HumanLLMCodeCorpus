class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        result = []
        stack = []
        visited = set()
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if current.right and current.right not in visited:
                stack.append(current)
                current = current.right
            else:
                visited.add(current)
                result.append(current.val)
                current = None
        return result
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
solution = Solution()
result = solution.postorderTraversal(root)
print(result)

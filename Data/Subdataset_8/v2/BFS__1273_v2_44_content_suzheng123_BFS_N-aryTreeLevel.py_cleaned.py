class TreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []
class Solution:
    def levelOrderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            level_values = []
            next_level = []
            for node in stack:
                level_values.append(node.value)
                next_level.extend(node.children)
            stack = next_level
            result.append(level_values)
        return result
if __name__ == "__main__":
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node3 = TreeNode(3, [node5, node6])
    node2 = TreeNode(2)
    node4 = TreeNode(4)
    root = TreeNode(1, [node3, node2, node4])
    solution = Solution()
    traversal_result = solution.levelOrderTraversal(root)
    print("Level order traversal:")
    for level_values in traversal_result:
        print(level_values)
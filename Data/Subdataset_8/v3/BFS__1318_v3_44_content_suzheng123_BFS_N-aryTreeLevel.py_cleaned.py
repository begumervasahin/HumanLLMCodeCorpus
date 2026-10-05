class TreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []
class Solution:
    def level_order_traversal(self, root):
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            level_values = []
            next_level = []
            for node in queue:
                level_values.append(node.value)
                next_level.extend(node.children)
            queue = next_level
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
    traversal_result = solution.level_order_traversal(root)
    print("Level order traversal:")
    for level_values in traversal_result:
        print(level_values)
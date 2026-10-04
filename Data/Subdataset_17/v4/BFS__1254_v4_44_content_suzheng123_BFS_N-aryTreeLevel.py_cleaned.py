
class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        current_level = [root]
        while current_level:
            level_values = []
            next_level = []
            for node in current_level:
                level_values.append(node.val)
                next_level.extend(node.children)
            result.append(level_values)
            current_level = next_level
        return result
if __name__ == "__main__":
    root = Node(1, [
        Node(3, [
            Node(5),
            Node(6)
        ]),
        Node(2),
        Node(4)
    ])
    solution = Solution()
    print("Level Order Traversal:", solution.levelOrder(root))
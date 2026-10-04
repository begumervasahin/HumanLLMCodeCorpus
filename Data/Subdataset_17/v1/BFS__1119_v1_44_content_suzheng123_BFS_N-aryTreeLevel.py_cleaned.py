class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children if children is not None else []
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        stack = [root]
        tree = []
        while stack:
            level = []
            temp_stack = []
            for node in stack:
                level.append(node.val)
                for child in node.children:
                    temp_stack.append(child)
            stack = temp_stack
            tree.append(level)
        return tree
if __name__ == "__main__":
    node5 = Node(5)
    node6 = Node(6)
    node3 = Node(3, [node5, node6])
    node2 = Node(2)
    node4 = Node(4)
    root = Node(1, [node3, node2, node4])
    solution = Solution()
    result = solution.levelOrder(root)
    print(result)

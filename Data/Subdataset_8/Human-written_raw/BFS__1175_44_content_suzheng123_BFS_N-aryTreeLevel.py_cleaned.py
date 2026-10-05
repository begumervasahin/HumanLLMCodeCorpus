44. Repository: suzheng123/BFS
   File: N-aryTreeLevel.py
   URL: https:
   Code Content:
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        stack = [root]
        tree = []
        while stack:
            level =  []
            temp_stack = []
            for node in stack:
                level.append(node.val)
                for child in node.children:
                    temp_stack.append(child)
            stack = temp_stack
            tree.append(level)
        return tree
   README Content:
algorithm problems
      1
     / \
    2   3
in order:      2 -> 1 -> 3
lever order:   1 -> 2 -> 3
post order:    2 -> 3 -> 1
N-ary Tree Level Order Traversal (3-ary example):
input:
            1
         /  |  \
        3   2   4
       / \
      5   6
output: [
          [1],
          [3,2,4],
          [5,6]
        ]

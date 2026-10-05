44. Repository: suzheng123/BFS
   File: N-aryTreeLevel.py
   URL: https:
   Code Content:
class class1(object):
    def fonk1(self, root):
        if not root:
            return []
        b1 = [root]
        b2 = []
        while b1:
            b3 = []
            b4 = []
            for node in b1:
                b3.append(node.val)
                for child in node.children:
                    b4.append(child)
            b1 = b4
            b2.append(b3)
        return b2
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

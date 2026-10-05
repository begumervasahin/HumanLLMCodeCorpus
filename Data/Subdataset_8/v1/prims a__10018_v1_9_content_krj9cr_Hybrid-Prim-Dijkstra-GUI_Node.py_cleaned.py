import sys
class Node(object):
    def __init__(self, x, y, i):
        self.x = x
        self.y = y
        self.idx = i
        self.key = sys.maxsize
        self.parent = None
    def __str__(self):
        return str(self.idx) + ': (' + str(self.x) + ',' + str(self.y) + ')'
node1 = Node(1, 2, 0)
print(node1)
print("Key:", node1.key)

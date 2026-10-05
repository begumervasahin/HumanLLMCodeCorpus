import sys
class Node:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
        self.key = sys.maxsize
        self.parent = None
    def __str__(self):
        return f"{self.idx}: ({self.x}, {self.y})"
node1 = Node(1, 2, 0)
print(node1)
print("Key:", node1.key)

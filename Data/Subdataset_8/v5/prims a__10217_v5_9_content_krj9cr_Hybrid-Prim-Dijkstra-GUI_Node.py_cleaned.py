import sys
class Node:
    def __init__(self, x_coordinate, y_coordinate, index):
        self.x = x_coordinate
        self.y = y_coordinate
        self.idx = index
        self.key = sys.maxsize
        self.parent = None
    def __str__(self):
        return f"Node {self.idx}: ({self.x}, {self.y})"
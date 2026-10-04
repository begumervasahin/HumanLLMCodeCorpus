class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        self.real_height = 0
        self.color = 1
    def __repr__(self):
        return f"Node(key={self.key}, left={self.left}, right={self.right}, " \
               f"parent={self.parent}, height={self.height}, real_height={self.real_height}, color={self.color})"
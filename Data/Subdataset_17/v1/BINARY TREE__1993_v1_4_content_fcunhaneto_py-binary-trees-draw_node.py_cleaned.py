class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        self.real_height = 0
        self.color = 1
if __name__ == "__main__":
    node = Node(10)
    node.left = Node(5)
    node.right = Node(15)
    node.left.parent = node
    node.right.parent = node
    print("Node key:", node.key)
    print("Left child key:", node.left.key)
    print("Right child key:", node.right.key)
    print("Parent of left child:", node.left.parent.key)
    print("Parent of right child:", node.right.parent.key)
    print("Node height:", node.height)
    print("Node real height:", node.real_height)
    print("Node color:", node.color)
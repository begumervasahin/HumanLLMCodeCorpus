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
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.parent = root
    root.right.parent = root
    print(f"Node key: {root.key}")
    print(f"Left child key: {root.left.key}")
    print(f"Right child key: {root.right.key}")
    print(f"Parent of left child: {root.left.parent.key}")
    print(f"Parent of right child: {root.right.parent.key}")
    print(f"Node height: {root.height}")
    print(f"Node real height: {root.real_height}")
    print(f"Node color: {root.color}")
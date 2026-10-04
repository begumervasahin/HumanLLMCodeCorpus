class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def in_order_print(root):
    if root is None:
        return
    in_order_print(root.left)
    print(root.value)
    in_order_print(root.right)
def pre_order_print(root):
    if root is None:
        return
    print(root.value)
    pre_order_print(root.left)
    pre_order_print(root.right)
def post_order_print(root):
    if root is None:
        return
    post_order_print(root.left)
    post_order_print(root.right)
    print(root.value)
def level_order_print(root):
    if root is None:
        return
    level = [root]
    level_number = 1
    while level:
        next_level = []
        print(f'Level {level_number}:')
        for node in level:
            print(node.value)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
        level_number += 1
if __name__ == "__main__":
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    root.left.right.left = Node(4)
    root.left.right.right = Node(15)
    print('In-Order Traversal:')
    in_order_print(root)
    print('\nPre-Order Traversal:')
    pre_order_print(root)
    print('\nPost-Order Traversal:')
    post_order_print(root)
    print('\nLevel-Order Traversal:')
    level_order_print(root)
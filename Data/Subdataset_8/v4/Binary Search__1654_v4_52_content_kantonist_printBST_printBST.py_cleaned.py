
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def in_order_print(root):
    if not root:
        return
    in_order_print(root.left)
    print(root.val)
    in_order_print(root.right)
def pre_order_print(root):
    if not root:
        return
    print(root.val)
    pre_order_print(root.left)
    pre_order_print(root.right)
def post_order_print(root):
    if not root:
        return
    post_order_print(root.left)
    post_order_print(root.right)
    print(root.val)
def level_print(root):
    level = [root]
    counter = 1
    while len(level) > 0:
        next_level = []
        print('Level ', counter)
        for node in level:
            print(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
        counter += 1
test = Node(8)
test.left = Node(3)
test.right = Node(10)
test.left.left = Node(1)
test.left.right = Node(6)
test.right.right = Node(14)
test.right.right.left = Node(13)
test.left.right.left = Node(4)
test.left.right.right = Node(15)
print('In-Order Traversal and print:')
in_order_print(test)
print('Pre-Order Traversal and print:')
pre_order_print(test)
print('Post-Order Traversal and print:')
post_order_print(test)
print('Level Traversal and print:')
level_print(test)
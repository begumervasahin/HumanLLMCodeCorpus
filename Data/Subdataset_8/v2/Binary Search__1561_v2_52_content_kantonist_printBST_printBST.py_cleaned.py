class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def inOrderPrint(root):
    if not root:
        return
    inOrderPrint(root.left)
    print(root.val)
    inOrderPrint(root.right)
def preOrderPrint(root):
    if not root:
        return
    print(root.val)
    preOrderPrint(root.left)
    preOrderPrint(root.right)
def postOrderPrint(root):
    if not root:
        return
    postOrderPrint(root.left)
    postOrderPrint(root.right)
    print(root.val)
def levelPrint(root):
    level = [root]
    counter = 1
    while len(level) > 0:
        next_level = []
        print('Level ', counter)
        for leaf in level:
            print(leaf.val)
            if leaf.left:
                next_level.append(leaf.left)
            if leaf.right:
                next_level.append(leaf.right)
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
inOrderPrint(test)
print('Pre-Order Traversal and print:')
preOrderPrint(test)
print('Post-Order Traversal and print:')
postOrderPrint(test)
print('Level Traversal and print:')
levelPrint(test)
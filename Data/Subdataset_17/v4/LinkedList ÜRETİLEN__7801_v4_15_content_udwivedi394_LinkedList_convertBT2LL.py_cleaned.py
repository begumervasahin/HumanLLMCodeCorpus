class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BSTNode:
    def __init__(self):
        self.root = None
    def addNode(self, data):
        pass
    def convertBST2DLL(self):
        stack = []
        temp = self.root
        while stack:
            pass
def in_order_traverse(root):
    temp = root
    stack = []
    while True:
        while temp:
            stack.append(temp)
            temp = temp.left
        if not stack:
            break
        temp = stack.pop()
        print(temp.data, end=" ")
        temp = temp.right
def convert_bt_to_dll(root):
    temp = root
    stack = []
    prev_node = None
    head = None
    tail = None
    while True:
        while temp:
            stack.append(temp)
            temp = temp.left
        if not stack:
            break
        temp = stack.pop()
        temp.left = prev_node
        if prev_node:
            prev_node.right = temp
        else:
            head = temp
        prev_node = temp
        print(temp.data, end=" ")
        if not temp.right:
            tail = temp
        temp = temp.right
    if tail and head:
        tail.right = head
        head.left = tail
    return head
def ll_traversal(root):
    temp = root
    start = True
    while temp and (start or temp != root):
        print(temp.data, end=" -> ")
        temp = temp.right
        start = False
    print("None")
root = Node(10)
root.left = Node(12)
root.left.left = Node(25)
root.left.right = Node(30)
root.right = Node(15)
root.right.left = Node(36)
print("In-order Traversal of the BST:")
in_order_traverse(root)
print("\n")
print("Converting BST to DLL and displaying the DLL:")
head = convert_bt_to_dll(root)
print("\n")
print("Traversal of the Circular DLL:")
ll_traversal(head)
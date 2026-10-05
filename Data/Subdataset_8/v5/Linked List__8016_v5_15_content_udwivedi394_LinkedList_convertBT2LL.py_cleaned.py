class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def add_node(self, data):
        pass
    def convert_bst_to_dll(self):
        stack = []
        temp = self.root
        while len(stack):
            pass
def in_order_traverse(root):
    temp = root
    stack = []
    while True:
        while temp:
            stack.append(temp)
            temp = temp.left
        while not temp and len(stack):
            temp = stack.pop()
            print(temp.data, end=' ')
            temp = temp.right
        if not stack and not temp:
            break
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
        while not temp and len(stack):
            temp = stack.pop()
            temp.left = prev_node
            if prev_node:
                prev_node.right = temp
            else:
                head = temp
            prev_node = temp
            print(temp.data, end=' ')
            if not temp.right:
                tail = temp
            temp = temp.right
        if not stack and not temp:
            tail.right = head
            head.left = tail
            break
    return head
def dll_traversal(root):
    temp = root
    start = True
    while temp and (start or temp != root):
        print(temp.data, "->", end=' ')
        temp = temp.right
        start = False
    print("None")
root = Node(10)
root.left = Node(12)
root.left.left = Node(25)
root.left.right = Node(30)
root.right = Node(15)
root.right.left = Node(36)
print("In-order traversal of the binary tree:")
in_order_traverse(root)
print("\nDoubly linked list traversal:")
head = convert_bt_to_dll(root)
dll_traversal(head)
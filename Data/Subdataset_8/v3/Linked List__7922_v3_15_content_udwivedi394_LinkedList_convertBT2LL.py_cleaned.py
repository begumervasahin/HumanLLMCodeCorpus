class TreeNode:
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
        current = self.root
        while len(stack) or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
        print()
def in_order_traverse(root):
    stack = []
    temp = root
    while True:
        while temp:
            stack.append(temp)
            temp = temp.left
        if not stack:
            break
        temp = stack.pop()
        print(temp.data, end=" ")
        temp = temp.right
    print()
def convert_bt_to_dll(root):
    stack = []
    prev_node = None
    head = None
    tail = None
    temp = root
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
    tail.right = head
    head.left = tail
    print()
    return head
def dll_traversal(root):
    current = root
    start = True
    while current and (start or current != root):
        print(current.data, "->", end=" ")
        current = current.right
        start = False
    print("None")
root = TreeNode(10)
root.left = TreeNode(12)
root.left.left = TreeNode(25)
root.left.right = TreeNode(30)
root.right = TreeNode(15)
root.right.left = TreeNode(36)
print("In-order Traversal of the Binary Tree:")
in_order_traverse(root)
print("\nConversion of Binary Tree to Doubly Linked List:")
head = convert_bt_to_dll(root)
print("\nTraversal of the Doubly Linked List:")
dll_traversal(head)
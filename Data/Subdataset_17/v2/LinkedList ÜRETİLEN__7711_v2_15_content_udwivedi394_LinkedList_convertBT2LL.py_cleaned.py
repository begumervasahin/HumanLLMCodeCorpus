class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BSTNode:
    def __init__(self):
        self.root = None
    def add_node(self, data):
        pass
    def convert_bst_to_dll(self):
        stack = []
        current = self.root
        while stack:
            pass
def in_order_traverse(root):
    current = root
    stack = []
    while True:
        while current:
            stack.append(current)
            current = current.left
        if not stack:
            break
        current = stack.pop()
        print(current.data, end=' ')
        current = current.right
def convert_bt_to_dll(root):
    current = root
    stack = []
    prev_node = None
    head = None
    tail = None
    while True:
        while current:
            stack.append(current)
            current = current.left
        if not stack:
            break
        current = stack.pop()
        current.left = prev_node
        if prev_node:
            prev_node.right = current
        else:
            head = current
        prev_node = current
        if not current.right:
            tail = current
        current = current.right
    if head and tail:
        head.left = tail
        tail.right = head
    return head
def traverse_dll(head):
    if not head:
        return
    current = head
    while True:
        print(f"{current.data} ->", end=' ')
        current = current.right
        if current == head:
            break
    print("None")
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(12)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right = Node(15)
    root.right.left = Node(36)
    print("In-order Traversal of Binary Tree:")
    in_order_traverse(root)
    print("\n")
    print("Converting Binary Tree to Circular Doubly Linked List:")
    head = convert_bt_to_dll(root)
    print("\n")
    print("Traversal of Circular Doubly Linked List:")
    traverse_dll(head)
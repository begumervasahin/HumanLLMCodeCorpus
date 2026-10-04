class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def add_node(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._add_node_recursive(self.root, data)
    def _add_node_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left:
                self._add_node_recursive(current_node.left, data)
            else:
                current_node.left = Node(data)
        else:
            if current_node.right:
                self._add_node_recursive(current_node.right, data)
            else:
                current_node.right = Node(data)
    def convert_bst_to_dll(self):
        if not self.root:
            return None
        stack = []
        current = self.root
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
        if tail and head:
            tail.right = head
            head.left = tail
        return head
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
        print(current.data, end=" ")
        current = current.right
def ll_traversal(head):
    current = head
    start = True
    while current and (start or current != head):
        print(current.data, end=" -> ")
        current = current.right
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
bst = BST()
bst.root = root
head = bst.convert_bst_to_dll()
print("\n")
print("Traversal of the Circular DLL:")
ll_traversal(head)
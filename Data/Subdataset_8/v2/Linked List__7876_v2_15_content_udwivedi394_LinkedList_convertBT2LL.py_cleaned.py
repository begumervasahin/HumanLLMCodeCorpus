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
        while len(stack) or temp:
            while temp:
                stack.append(temp)
                temp = temp.left
            temp = stack.pop()
            print(temp.data, end=" ")
            temp = temp.right
def inOrderTraverse(root):
    temp = root
    stack = []
    while True:
        while temp:
            stack.append(temp)
            temp = temp.left
        while temp is None and stack:
            temp = stack.pop()
            print(temp.data, end=" ")
            temp = temp.right
        if not stack and temp is None:
            break
    print()
def convertBT2DLL(root):
    temp = root
    stack = []
    prevNode = None
    head = None
    tail = None
    while True:
        while temp:
            stack.append(temp)
            temp = temp.left
        while temp is None and stack:
            temp = stack.pop()
            temp.left = prevNode
            if prevNode:
                prevNode.right = temp
            else:
                head = temp
            prevNode = temp
            print(temp.data, end=" ")
            if temp.right is None:
                tail = temp
            temp = temp.right
        if not stack and temp is None:
            tail.right = head
            head.left = tail
            break
    print()
    return head
def llTraversal(root):
    temp = root
    start = True
    while temp and (start or temp != root):
        print(temp.data, "->", end=" ")
        temp = temp.right
        start = False
    print("None")
root = Node(10)
root.left = Node(12)
root.left.left = Node(25)
root.left.right = Node(30)
root.right = Node(15)
root.right.left = Node(36)
print("In-order Traversal of the Binary Tree:")
inOrderTraverse(root)
print("\nConversion of Binary Tree to Doubly Linked List:")
head = convertBT2DLL(root)
print("\nTraversal of the Doubly Linked List:")
llTraversal(head)
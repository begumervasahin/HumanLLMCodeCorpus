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
        while len(stack):
            pass
def inOrderTraverse(root):
    temp = root
    stack = []
    while 1:
        while temp:
            stack.append(temp)
            temp = temp.left
        while temp == None and len(stack):
            temp = stack.pop()
            print(temp.data, end=' ')
            temp = temp.right
        if len(stack) == 0 and temp == None:
            break
def convertBT2DLL(root):
    temp = root
    stack = []
    prevNode = None
    head = None
    tail = None
    while 1:
        while temp:
            stack.append(temp)
            temp = temp.left
        while temp == None and len(stack):
            temp = stack.pop()
            temp.left = prevNode
            if prevNode:
                prevNode.right = temp
            else:
                head = temp
            prevNode = temp
            print(temp.data, end=' ')
            if temp.right == None:
                tail = temp
            temp = temp.right
        if len(stack) == 0 and temp == None:
            tail.right = head
            head.left = tail
            break
    return head
def llTraversal(root):
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
inOrderTraverse(root)
print("\nDoubly linked list traversal:")
head = convertBT2DLL(root)
llTraversal(head)
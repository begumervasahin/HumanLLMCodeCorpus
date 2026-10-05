class Node:
    def __init__(self, value):
        self.v = value
        self.l = None
        self.r = None
    def addLeft(self, node):
        self.l = node
    def addRight(self, node):
        self.r = node
def countdown(x):
    print(x)
    if x > 0:
        countdown(x - 1)
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
def tailFactorial(x, acc=1):
    if x == 0:
        return acc
    else:
        return tailFactorial(x - 1, acc * x)
rootNode = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
rootNode.addLeft(node1)
rootNode.addRight(node2)
node1.addLeft(node3)
node2.addLeft(node4)
node2.addRight(node5)
def treeTraverse(root):
    print(root.v)
    if root.l:
        print("Left")
        treeTraverse(root.l)
    if root.r:
        print("Right")
        treeTraverse(root.r)
def treeSearch(root, val):
    if root.v == val:
        print("Found")
    elif root.l:
        treeSearch(root.l, val)
    elif root.r:
        treeSearch(root.r, val)
def msort3(x):
    result = []
    if len(x) < 2:
        return x
    mid = len(x)
    y = msort3(x[:mid])
    z = msort3(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result
if __name__ == "__main__":
    countdown(5)
    print(factorial(5))
    print(tailFactorial(5))
    treeTraverse(rootNode)
    treeSearch(rootNode, 3)
    print(msort3([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
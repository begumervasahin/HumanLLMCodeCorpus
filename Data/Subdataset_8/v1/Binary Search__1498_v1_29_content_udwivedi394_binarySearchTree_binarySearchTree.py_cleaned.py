class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def addNode(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        temp = self.root
        while temp:
            prevNode = temp
            if data < temp.data:
                temp = temp.left
            elif data >= temp.data:
                temp = temp.right
        if data < prevNode.data:
            prevNode.left = Node(data)
        else:
            prevNode.right = Node(data)
    def inOrder(self):
        if self.root is None:
            print("Nothing to print")
            return
        print("\nIn Order:", end=" ")
        stack = []
        temp = self.root
        while True:
            while temp:
                stack.append(temp)
                temp = temp.left
            while temp is None and stack:
                temp = stack.pop()
                print(temp.data, end=" ")
                temp = temp.right
            if temp is None and not stack:
                break
        print()
    def levelOrder(self):
        if self.root is None:
            print("No Tree")
            return
        print("\nLevel Order:")
        queue = []
        temp = self.root
        queue.append(temp)
        while queue:
            n = len(queue)
            while n:
                temp = queue.pop(0)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                print(temp.data, end=" ")
                n -= 1
            print()
    def searchData(self, data, del_operation):
        temp = self.root
        prevNode = None
        print()
        while temp:
            if temp.data == data:
                print("%d found!" % data)
                if del_operation:
                    return prevNode
                return True
            prevNode = temp
            if data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        print("%d not present" % data)
        if del_operation:
            return None
        return False
    def deleteNode(self, data):
        prevNode = self.searchData(data, True)
        if prevNode is None and self.root.data != data:
            print("Node to be deleted not found!")
            return False
        left = True
        if prevNode is None:
            node = self.root
        elif data < prevNode.data:
            node = prevNode.left
        elif data > prevNode.data:
            node = prevNode.right
            left = False
        if prevNode and ((node.left is None) ^ (node.right is None) or node.left is None):
            print("I'm coming here")
            if left:
                prevNode.left = node.left
            else:
                prevNode.right = node.right
            return
        if prevNode is None:
            if node.left is None and node.right is None:
                self.root = None
            elif node.left is None:
                self.root = node.right
            elif node.right is None:
                self.root = node.left
            return
        temp = node.right
        prevNode = node
        while temp and temp.left:
            prevNode = temp
            temp = temp.left
        node.data ^= temp.data
        temp.data ^= node.data
        node.data ^= temp.data
        prevNode.left = None
        return None
    def searchKthNode(self, k):
        stack = []
        temp = self.root
        while True:
            while temp:
                stack.append(temp)
                temp = temp.left
            while temp is None and stack:
                temp = stack.pop()
                k -= 1
                if k <= 0:
                    print(temp.data, end=" ")
                    return
                temp = temp.right
            if temp is None and not stack:
                break
    def inOrderSuccessor(self, k):
        temp = self.root
        successor = None
        found = False
        while temp:
            if k == temp.data:
                found = True
                break
            elif k < temp.data:
                successor = temp
                temp = temp.left
            else:
                temp = temp.right
        if not found:
            print("Element not found")
            return False
        if successor is None:
            print("Last Node, no successor present!")
            return False
        if temp.right:
            temp = temp.right
            while temp.left:
                temp = temp.left
            return temp.data
        return successor.data
    def getRoot(self):
        return self.root
bst = BST()
bst.addNode(50)
bst.addNode(30)
bst.addNode(20)
bst.addNode(40)
bst.addNode(70)
bst.addNode(60)
bst.addNode(80)
print("Inorder Traversal:")
bst.inOrder()
print("\nLevel Order Traversal:")
bst.levelOrder()
bst.deleteNode(20)
bst.deleteNode(30)
print("\nInorder Traversal after deleting 20 and 30:")
bst.inOrder()
print("\nKth node (2nd) in Inorder Traversal:")
bst.searchKthNode(2)
print("\nInorder Successor of 50:")
print(bst.inOrderSuccessor(50))
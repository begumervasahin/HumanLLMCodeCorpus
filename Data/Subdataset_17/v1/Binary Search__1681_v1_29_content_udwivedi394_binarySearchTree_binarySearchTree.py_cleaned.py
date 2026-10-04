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
            else:
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
            if not stack:
                break
            temp = stack.pop()
            print(temp.data, end=" ")
            temp = temp.right
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
    def searchData(self, data, del_operation=False):
        temp = self.root
        prevNode = None
        while temp:
            if temp.data == data:
                print(f"{data} found!")
                if del_operation:
                    return prevNode
                return True
            prevNode = temp
            if data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        print(f"{data} not present")
        if del_operation:
            return None
        return False
    def deleteNode(self, data):
        prevNode = self.searchData(data, True)
        if prevNode is None and (self.root is None or self.root.data != data):
            print("Node to be deleted not found!")
            return False
        left = True
        if prevNode is None:
            node = self.root
        elif data < prevNode.data:
            node = prevNode.left
        else:
            node = prevNode.right
            left = False
        if node and (node.left is None or node.right is None):
            if left:
                prevNode.left = node.left if node.left else node.right
            else:
                prevNode.right = node.left if node.left else node.right
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
        node.data, temp.data = temp.data, node.data
        if prevNode.left == temp:
            prevNode.left = temp.right
        else:
            prevNode.right = temp.right
    def searchKthNode(self, k):
        stack = []
        temp = self.root
        while True:
            while temp:
                stack.append(temp)
                temp = temp.left
            if not stack:
                break
            temp = stack.pop()
            k -= 1
            if k == 0:
                print(temp.data)
                return
            temp = temp.right
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
if __name__ == "__main__":
    bst = BST()
    bst.addNode(10)
    bst.addNode(5)
    bst.addNode(20)
    bst.addNode(15)
    bst.addNode(25)
    bst.inOrder()
    bst.levelOrder()
    bst.searchData(15)
    bst.searchKthNode(3)
    successor = bst.inOrderSuccessor(15)
    if successor:
        print(f"In-order successor of 15: {successor}")
    bst.deleteNode(20)
    bst.levelOrder()
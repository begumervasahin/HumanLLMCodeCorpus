class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        if value == self.value:
            return False
        elif value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = Node(value)
                return True
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = Node(value)
                return True
    def find(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            return self.left.find(value) if self.left else False
        else:
            return self.right.find(value) if self.right else False
    def preorder(self):
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value)
    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
            else:
                print(f'Node with value {value} not found!')
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
            else:
                print(f'Node with value {value} not found!')
        else:
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            successor = self._find_min()
            self.value = successor.value
            self.right = self.right.delete(successor.value)
        return self
    def _find_min(self):
        current = self
        while current.left:
            current = current.left
        return current
if __name__ == "__main__":
    root = Node(10)
    root.insert(5)
    root.insert(15)
    root.insert(3)
    root.insert(7)
    root.insert(13)
    root.insert(17)
    print("In-order traversal:")
    root.inorder()
    print("\nPre-order traversal:")
    root.preorder()
    print("\nPost-order traversal:")
    root.postorder()
    print("\nSearching for 7 in the tree:")
    print("Found!" if root.find(7) else "Not found!")
    print("\nDeleting 15 from the tree:")
    root.delete(15)
    root.inorder()
    print("\nDeleting 10 from the tree (root):")
    root = root.delete(10)
    if root:
        root.inorder()
    else:
        print("Tree is empty.")
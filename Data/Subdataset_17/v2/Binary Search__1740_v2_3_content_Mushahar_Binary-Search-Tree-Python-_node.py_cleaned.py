class _Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
    def insert(self, val):
        if self.value == val:
            return False
        elif val < self.value:
            if self.left:
                return self.left.insert(val)
            else:
                self.left = _Node(val)
                return True
        else:
            if self.right:
                return self.right.insert(val)
            else:
                self.right = _Node(val)
                return True
    def find(self, val):
        if self.value == val:
            return True
        elif val < self.value:
            return self.left.find(val) if self.left else False
        else:
            return self.right.find(val) if self.right else False
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
    def delete(self, val):
        if val < self.value:
            if self.left:
                self.left = self.left.delete(val)
            else:
                print('Node not found!')
        elif val > self.value:
            if self.right:
                self.right = self.right.delete(val)
            else:
                print('Node not found!')
        else:
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            successor = self.right._find_min()
            self.value = successor.value
            self.right = self.right.delete(successor.value)
        return self
    def _find_min(self):
        current = self
        while current.left:
            current = current.left
        return current
if __name__ == "__main__":
    root = _Node(10)
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
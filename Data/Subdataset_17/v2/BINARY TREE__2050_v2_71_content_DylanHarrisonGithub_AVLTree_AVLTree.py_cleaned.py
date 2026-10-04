class AVLTreeNode:
    def __init__(self, keyData):
        self.keyData = keyData
        self.count = 1
        self.depth = 0
        self.height = 0
        self.order = -1
        self.parent = None
        self.left = None
        self.right = None
    def isLeftChild(self):
        return self.parent and self.parent.left == self
    def isRightChild(self):
        return self.parent and self.parent.right == self
    def isLeaf(self):
        return not self.left and not self.right
    def isRoot(self):
        return not self.parent
    def hasGrandParent(self):
        return self.parent and self.parent.parent
    def leftSubTreeHeight(self):
        return self.left.height if self.left else -1
    def rightSubTreeHeight(self):
        return self.right.height if self.right else -1
    def maxSubTreeHeight(self):
        return max(self.leftSubTreeHeight(), self.rightSubTreeHeight())
    def isBalanced(self):
        return abs(self.leftSubTreeHeight() - self.rightSubTreeHeight()) <= 1
    def rightMostNodeInLeftSubtree(self):
        current = self
        if current.left:
            current = current.left
            while current.right:
                current = current.right
            return current
        return None
    def leftMostNodeInRightSubtree(self):
        current = self
        if current.right:
            current = current.right
            while current.left:
                current = current.left
            return current
        return None
    def parentOfNearestAncestorThatIsLeftChild(self):
        current = self
        if current.isRightChild():
            while current.isRightChild():
                current = current.parent
            if current.isLeftChild():
                return current.parent
        return None
    def parentOfNearestAncestorThatIsRightChild(self):
        current = self
        if current.isLeftChild():
            while current.isLeftChild():
                current = current.parent
            if current.isRightChild():
                return current.parent
        return None
    def next(self):
        if self.isRoot():
            return self.leftMostNodeInRightSubtree() if self.right else None
        if self.isLeftChild():
            return self.leftMostNodeInRightSubtree() if self.right else self.parent
        return self.leftMostNodeInRightSubtree() if self.right else self.parentOfNearestAncestorThatIsLeftChild()
    def prev(self):
        if self.isRoot():
            return self.rightMostNodeInLeftSubtree() if self.left else None
        if self.isLeftChild():
            return self.rightMostNodeInLeftSubtree() if self.left else self.parentOfNearestAncestorThatIsRightChild()
        return self.rightMostNodeInLeftSubtree() if self.left else self.parent
    def insert(self, tree, keyData):
        if self.keyData == keyData:
            self.count += 1
            return None
        if self.keyData > keyData:
            if not self.left:
                self.left = AVLTreeNode(keyData)
                self.left.parent = self
                self.left.depth = self.depth + 1
                tree.numNodes += 1
                return self.left
            return self.left.insert(tree, keyData)
        if not self.right:
            self.right = AVLTreeNode(keyData)
            self.right.parent = self
            self.right.depth = self.depth + 1
            tree.numNodes += 1
            return self.right
        return self.right.insert(tree, keyData)
    def remove(self, tree):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
                self.parent.bubbleUp(tree)
            elif self.isRightChild():
                self.parent.right = None
                self.parent.bubbleUp(tree)
            else:
                tree.rootNode = None
        else:
            if self.left and self.right:
                if self.prev().isLeaf():
                    self.swapIn(tree, self.prev().remove(tree))
                else:
                    self.swapIn(tree, self.next().remove(tree))
            elif self.right:
                self.swapIn(tree, self.next().remove(tree))
            else:
                self.swapIn(tree, self.prev().remove(tree))
        return self
    def swapIn(self, tree, newNode):
        newNode.parent = self.parent
        newNode.left = self.left
        newNode.right = self.right
        newNode.height = self.height
        newNode.depth = self.depth
        if self.left:
            self.left.parent = newNode
        if self.right:
            self.right.parent = newNode
        if self.isLeftChild():
            self.parent.left = newNode
        if self.isRightChild():
            self.parent.right = newNode
        if self.isRoot():
            tree.rootNode = newNode
    def bubbleUp(self, tree):
        self.height = self.maxSubTreeHeight() + 1
        if not self.isBalanced():
            self.rotate(tree)
        if self.parent:
            self.parent.bubbleUp(tree)
    def rotate(self, tree):
        parent = self.parent
        if self.leftSubTreeHeight() > self.rightSubTreeHeight():
            if self.left.leftSubTreeHeight() > self.left.rightSubTreeHeight():
                z = self
                y = self.left
                x = self.left.left
                T0, T1, T2, T3 = x.left, x.right, y.right, z.right
            else:
                z = self
                y = self.left.right
                x = self.left
                T0, T1, T2, T3 = x.left, y.left, y.right, z.right
            if z.isLeftChild():
                parent.left = y
            elif z.isRightChild():
                parent.right = y
            else:
                tree.rootNode = y
        else:
            if self.right.rightSubTreeHeight() > self.right.leftSubTreeHeight():
                z = self.right.right
                y = self.right
                x = self
                T0, T1, T2, T3 = x.left, y.left, z.left, z.right
            else:
                z = self.right
                y = self.right.left
                x = self
                T0, T1, T2, T3 = x.left, y.left, y.right, z.right
            if x.isLeftChild():
                parent.left = y
            elif x.isRightChild():
                parent.right = y
            else:
                tree.rootNode = y
        y.parent = parent
        y.left = x
        y.right = z
        x.parent = y
        z.parent = y
        x.left = T0
        x.right = T1
        z.left = T2
        z.right = T3
        if T0:
            T0.parent = x
        if T1:
            T1.parent = x
        if T2:
            T2.parent = z
        if T3:
            T3.parent = z
        x.height = x.maxSubTreeHeight() + 1
        z.height = z.maxSubTreeHeight() + 1
        y.height = y.maxSubTreeHeight() + 1
        if parent:
            y.setDepth(parent.depth + 1)
        else:
            y.setDepth(0)
    def setDepth(self, depth):
        self.depth = depth
        if self.left:
            self.left.setDepth(depth + 1)
        if self.right:
            self.right.setDepth(depth + 1)
class AVLTree:
    def __init__(self):
        self.rootNode = None
        self.numNodes = 0
    def find(self, keyData):
        current = self.rootNode
        while current:
            if current.keyData == keyData:
                return current
            if current.keyData > keyData:
                current = current.left
            else:
                current = current.right
        return None
    def insert(self, keyData):
        if not self.rootNode:
            self.rootNode = AVLTreeNode(keyData)
            self.rootNode.height = 0
            self.rootNode.depth = 0
            self.numNodes = 1
        else:
            newNode = self.rootNode.insert(self, keyData)
            if newNode:
                newNode.bubbleUp(self)
    def remove(self, keyData):
        node_to_remove = self.find(keyData)
        if node_to_remove:
            node_to_remove.remove(self)
            self.numNodes -= 1
        return node_to_remove
    def printTree(self):
        current = self.getFirst()
        while current:
            print(current.keyData)
            current = current.next()
    def getFirst(self):
        current = self.rootNode
        while current and current.left:
            current = current.left
        return current
    def markOrder(self):
        current = self.getFirst()
        order = 0
        while current:
            current.order = order
            order += 1
            current = current.next()
if __name__ == "__main__":
    avl_tree = AVLTree()
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    avl_tree.insert(40)
    avl_tree.insert(50)
    avl_tree.insert(25)
    print("AVL Tree in order:")
    avl_tree.printTree()
    avl_tree.remove(30)
    print("AVL Tree after removing 30:")
    avl_tree.printTree()
    first_node = avl_tree.getFirst()
    if first_node:
        print("First node:", first_node.keyData)
    avl_tree.markOrder()
    print("Nodes with order marked:")
    avl_tree.printTree()
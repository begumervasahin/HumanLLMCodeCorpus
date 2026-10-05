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
        return (self.parent is not None) and (self.parent.left == self)
    def isRightChild(self):
        return (self.parent is not None) and (self.parent.right == self)
    def isLeaf(self):
        return (self.left is None) and (self.right is None)
    def isRoot(self):
        return self.parent is None
    def hasGrandParent(self):
        return (self.parent is not None) and (self.parent.parent is not None)
    def leftSubTreeHeight(self):
        return self.left.height if (self.left is not None) else -1
    def rightSubTreeHeight(self):
        return self.right.height if (self.right is not None) else -1
    def maxSubTreeHeight(self):
        leftSubTreeHeight = self.leftSubTreeHeight()
        rightSubTreeHeight = self.rightSubTreeHeight()
        return max(leftSubTreeHeight, rightSubTreeHeight)
    def isBalanced(self):
        leftHeight = self.leftSubTreeHeight()
        rightHeight = self.rightSubTreeHeight()
        return abs(rightHeight - leftHeight) <= 1
    def rightMostNodeInLeftSubtree(self):
        current = self
        if self.left:
            current = current.left
            while current.right:
                current = current.right
            return current
        else:
            return None
    def leftMostNodeInRightSubtree(self):
        current = self
        if self.right:
            current = current.right
            while current.left:
                current = current.left
            return current
        else:
            return None
    def parentOfNearestAncestorThatIsLeftChild(self):
        current = self
        if current.isRightChild():
            while current.isRightChild():
                current = current.parent
            if current.isLeftChild():
                return current.parent
            else:
                return None
        else:
            return None
    def parentOfNearestAncestorThatIsRightChild(self):
        current = self
        if current.isLeftChild():
            while current.isLeftChild():
                current = current.parent
            if current.isRightChild():
                return current.parent
            else:
                return None
        else:
            return None
    def next(self):
        if self.isRoot():
            if self.right:
                return self.leftMostNodeInRightSubtree()
            else:
                return None
        elif self.isLeftChild():
            if self.right:
                return self.leftMostNodeInRightSubtree()
            else:
                return self.parent
        else:
            if self.right:
                return self.leftMostNodeInRightSubtree()
            else:
                return self.parentOfNearestAncestorThatIsLeftChild()
    def prev(self):
        if self.isRoot():
            if self.left:
                return self.rightMostNodeInLeftSubtree()
            else:
                return None
        elif self.isLeftChild():
            if self.left:
                return self.rightMostNodeInLeftSubtree()
            else:
                return self.parentOfNearestAncestorThatIsRightChild()
        else:
            if self.left:
                return self.rightMostNodeInLeftSubtree()
            else:
                return self.parent
    def insert(self, delegateTree, keyData):
        if self.keyData == keyData:
            self.count += 1
            return None
        elif self.keyData > keyData:
            if not self.left:
                self.left = AVLTreeNode(keyData)
                self.left.parent = self
                self.left.depth = self.depth + 1
                delegateTree.numNodes += 1
                return self.left
            else:
                return self.left.insert(delegateTree, keyData)
        else:
            if not self.right:
                self.right = AVLTreeNode(keyData)
                self.right.parent = self
                self.right.depth = self.depth + 1
                delegateTree.numNodes += 1
                return self.right
            else:
                return self.right.insert(delegateTree, keyData)
    def remove(self, delegateTree):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
                self.parent.bubbleUp(delegateTree)
            elif self.isRightChild():
                self.parent.right = None
                self.parent.bubbleUp(delegateTree)
            else:
                delegateTree.rootNode = None
        else:
            if self.left and self.right:
                if self.prev().isLeaf():
                    self.swapIn(delegateTree, self.prev().remove(delegateTree))
                else:
                    self.swapIn(delegateTree, self.next().remove(delegateTree))
            else:
                if self.right:
                    self.swapIn(delegateTree, self.next().remove(delegateTree))
                else:
                    self.swapIn(delegateTree, self.prev().remove(delegateTree))
        return self
    def swapIn(self, delegateTree, newNode):
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
            delegateTree.rootNode = newNode
    def bubbleUp(self, delegateTree):
        self.height = self.maxSubTreeHeight() + 1
        if not self.isBalanced():
            self.rotate(delegateTree)
        if self.parent:
            self.parent.bubbleUp(delegateTree)
    def rotate(self, delegateTree):
        p = self.parent
        if self.leftSubTreeHeight() > self.rightSubTreeHeight():
            if self.left.leftSubTreeHeight() > self.left.rightSubTreeHeight():
                z = self
                y = self.left
                x = self.left.left
                T_0 = x.left
                T_1 = x.right
                T_2 = y.right
                T_3 = z.right
            else:
                z = self
                y = self.left.right
                x = self.left
                T_0 = x.left
                T_1 = y.left
                T_2 = y.right
                T_3 = z.right
            if z.isLeftChild():
                p.left = y
            elif z.isRightChild():
                p.right = y
            else:
                delegateTree.rootNode = y
        else:
            if self.right.rightSubTreeHeight() > self.right.leftSubTreeHeight():
                z = self.right.right
                y = self.right
                x = self
                T_0 = x.left
                T_1 = y.left
                T_2 = z.left
                T_3 = z.right
            else:
                z = self.right
                y = self.right.left
                x = self
                T_0 = x.left
                T_1 = y.left
                T_2 = y.right
                T_3 = z.right
            if x.isLeftChild():
                p.left = y
            elif x.isRightChild():
                p.right = y
            else:
                delegateTree.rootNode = y
        y.parent = p
        y.left = x
        y.right = z
        x.parent = y
        z.parent = y
        if T_0:
            T_0.parent = x
        if T_1:
            T_1.parent = x
        if T_2:
            T_2.parent = z
        if T_3:
            T_3.parent = z
        x.left = T_0
        x.right = T_1
        z.left = T_2
        z.right = T_3
        x.height = x.maxSubTreeHeight() + 1
        z.height = z.maxSubTreeHeight() + 1
        y.height = y.maxSubTreeHeight() + 1
        if p:
            y.setDepth(p.depth + 1)
        else:
            y.setDepth(0)
    def setDepth(self, depth):
        if self.left:
            self.left.setDepth(depth + 1)
        self.depth = depth
        if self.right:
            self.right.setDepth(depth + 1)
class AVLTree:
    def __init__(self):
        self.rootNode = None
        self.numNodes = 0
        self.currentNode = None
    def find(self, keyData):
        if self.rootNode:
            current = self.rootNode
            while current:
                if current.keyData == keyData:
                    return current
                elif current.keyData > keyData:
                    current = current.left
                else:
                    current = current.right
            return current
        else:
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
        removedNode = self.find(keyData)
        if removedNode:
            removedNode.remove(self)
            self.numNodes -= 1
        return removedNode
    def printTree(self):
        if self.rootNode:
            current = self.rootNode
            while current.left:
                current = current.left
            while current:
                print(current.keyData)
                current = current.next()
    def getFirst(self):
        if self.rootNode:
            current = self.rootNode
            while current.left:
                current = current.left
            return current
        else:
            return None
    def markOrder(self):
        if self.rootNode:
            current = self.getFirst()
            n = 0
            while current:
                current.order = n
                n += 1
                current = current.next()
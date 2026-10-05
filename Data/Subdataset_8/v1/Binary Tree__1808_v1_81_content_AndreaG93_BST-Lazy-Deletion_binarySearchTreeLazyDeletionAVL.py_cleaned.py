class binarySearchTreeNodeAVLwithLazyDeletion:
    def __init__(self, key, value):
        self._key = key
        self._value = value
        self._leftSon = None
        self._rightSon = None
        self._parent = None
        self._isValid = True
    def hasRightSon(self):
        return self._rightSon is not None
    def hasLeftSon(self):
        return self._leftSon is not None
    def hasOnlyOneSon(self):
        return (self.hasLeftSon() and not self.hasRightSon()) or (self.hasRightSon() and not self.hasLeftSon())
class binarySearchTreeAVL:
    def __init__(self, rootNode=None):
        self._rootNode = rootNode
    def _updateNodeSubtreesHeightAlongTree(self, node):
        pass
class binarySearchTreeLazyDeletionAVL(binarySearchTreeAVL):
    def __init__(self, rootNode=None):
        super().__init__(rootNode)
    def insert(self, key, value):
        if not self._rootNode:
            self._rootNode = binarySearchTreeNodeAVLwithLazyDeletion(key, value)
            return
        else:
            currentNode = self._rootNode
            parentNode = None
            insertToLeft = True
            while currentNode is not None:
                parentNode = currentNode
                if currentNode._isValid:
                    if key <= currentNode._key:
                        currentNode = currentNode._leftSon
                        insertToLeft = True
                    else:
                        currentNode = currentNode._rightSon
                        insertToLeft = False
                else:
                    if currentNode.hasRightSon() and key > currentNode._rightSon._key:
                        currentNode = currentNode._rightSon
                        insertToLeft = False
                    elif currentNode.hasLeftSon() and key < currentNode._leftSon._key:
                        currentNode = currentNode._leftSon
                        insertToLeft = True
                    else:
                        currentNode._isValid = True
                        currentNode._key = key
                        currentNode._value = value
                        return
            newNode = binarySearchTreeNodeAVLwithLazyDeletion(key, value)
            newNode._parent = parentNode
            if insertToLeft:
                parentNode._leftSon = newNode
                newNode._isLeftSon = True
            else:
                parentNode._rightSon = newNode
                newNode._isLeftSon = False
            if parentNode.hasOnlyOneSon():
                self._updateNodeSubtreesHeightAlongTree(newNode)
    def delete(self, key):
        currentNode = self._rootNode
        while currentNode:
            if key < currentNode._key:
                currentNode = currentNode._leftSon
            elif key > currentNode._key:
                currentNode = currentNode._rightSon
            else:
                if currentNode._isValid:
                    currentNode._isValid = False
                    return True
                else:
                    currentNode = currentNode._leftSon
        return False
    def search(self, key, allowRestructuring):
        invalidNodeList = []
        currentNode = self._rootNode
        while currentNode:
            if allowRestructuring and not currentNode._isValid:
                invalidNodeList.append(currentNode)
            if key < currentNode._key:
                currentNode = currentNode._leftSon
            elif key > currentNode._key:
                currentNode = currentNode._rightSon
            else:
                if currentNode._isValid:
                    break
                else:
                    currentNode = currentNode._leftSon
        for item in invalidNodeList:
            self.deleteNode(item)
        return currentNode
if __name__ == "__main__":
    pass
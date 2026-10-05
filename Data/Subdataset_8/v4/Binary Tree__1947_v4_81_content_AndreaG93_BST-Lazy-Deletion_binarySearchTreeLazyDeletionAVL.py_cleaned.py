from binarySearchTreeNode import BinarySearchTreeNodeAVLWithLazyDeletion
from binarySearchTreeAVL import BinarySearchTreeAVL
class BinarySearchTreeLazyDeletionAVL(BinarySearchTreeAVL):
    def __init__(self, rootNode=None):
        super().__init__(rootNode)
    def insert(self, key, value):
        if not self._rootNode:
            self._rootNode = BinarySearchTreeNodeAVLWithLazyDeletion(key, value)
            return
        else:
            currentNode = self._rootNode
            parentNode = None
            insertToLeft = True
            while currentNode:
                parentNode = currentNode
                if currentNode.is_valid:
                    if key <= currentNode.key:
                        currentNode = currentNode.left_son
                        insertToLeft = True
                    else:
                        currentNode = currentNode.right_son
                        insertToLeft = False
                else:
                    if currentNode.has_right_son() and (key > currentNode.right_son.key):
                        currentNode = currentNode.right_son
                        insertToLeft = False
                    elif currentNode.has_left_son() and (key < currentNode.left_son.key):
                        currentNode = currentNode.left_son
                        insertToLeft = True
                    else:
                        currentNode.is_valid = True
                        currentNode.key = key
                        currentNode.value = value
                        return
            newNode = BinarySearchTreeNodeAVLWithLazyDeletion(key, value)
            newNode.parent = parentNode
            if insertToLeft:
                parentNode.left_son = newNode
                newNode.is_left_son = True
            else:
                parentNode.right_son = newNode
                newNode.is_left_son = False
            if parentNode.has_only_one_son():
                self._update_node_subtrees_height_along_tree(newNode)
    def delete(self, key):
        currentNode = self._rootNode
        while currentNode:
            if key < currentNode.key:
                currentNode = currentNode.left_son
            elif key > currentNode.key:
                currentNode = currentNode.right_son
            else:
                if currentNode.is_valid:
                    currentNode.is_valid = False
                    return True
                else:
                    currentNode = currentNode.left_son
        return False
    def search(self, key, allow_restructuring):
        invalidNodeList = []
        currentNode = self._rootNode
        while currentNode:
            if allow_restructuring and (not currentNode.is_valid):
                invalidNodeList.append(currentNode)
            if key < currentNode.key:
                currentNode = currentNode.left_son
            elif key > currentNode.key:
                currentNode = currentNode.right_son
            else:
                if currentNode.is_valid:
                    break
                else:
                    currentNode = currentNode.left_son
        for item in invalidNodeList:
            self.delete_node(item)
        return currentNode
'''
Created on Nov 29, 2017
Author: Andrea Graziani - matricola 0189326
Version: 1.0
'''
from binarySearchTreeNode import binarySearchTreeNodeAVLwithLazyDeletion
from binarySearchTreeAVL import binarySearchTreeAVL
class class1(binarySearchTreeAVL):
    def fonk1(self, b1 = None):
        super().fonk1(b1)
    def fonk2(self, key, value):
        if not self.b2:
            self.b2 = binarySearchTreeNodeAVLwithLazyDeletion(key, value)
            return
        b3 = self.b2
        b4 = None
        b5 = True
        while b3 is not None:
            b4 = b3
            if b3.b6:
                if key <= b3.b7:
                    b3 = b3.b11
                    b5 = True
                else:
                    b3 = b3.b13
                    b5 = False
            else:
                if b3.hasRightSon() and key > b3.b13.b7:
                    b3 = b3.b13
                    b5 = False
                elif b3.hasLeftSon() and key < b3.b11.b7:
                    b3 = b3.b11
                    b5 = True
                else:
                    b3.b6 = True
                    b3.b7 = key
                    b3.b8 = value
                    return
        b9 = binarySearchTreeNodeAVLwithLazyDeletion(key, value)
        b9.b10 = b4
        if b5:
            b4.b11 = b9
            b9.b12 = True
        else:
            b4.b13 = b9
            b9.b12 = False
        if b4.hasOnlyOneSon():
            self._updateNodeSubtreesHeightAlongTree(b9)
    def fonk3(self, key):
        b3 = self.b2
        while b3:
            if key < b3.b7:
                b3 = b3.b11
            elif key > b3.b7:
                b3 = b3.b13
            else:
                if b3.b6:
                    b3.b6 = False
                    return True
                else:
                    b3 = b3.b11
        return False
    def fonk4(self, key, allow_restructuring):
        b14 = []
        b3 = self.b2
        while b3:
            if allow_restructuring and not b3.b6:
                b14.append(b3)
            if key < b3.b7:
                b3 = b3.b11
            elif key > b3.b7:
                b3 = b3.b13
            else:
                if b3.b6:
                    break
                else:
                    b3 = b3.b11
        for item in b14:
            self.deleteNode(item)
        return b3
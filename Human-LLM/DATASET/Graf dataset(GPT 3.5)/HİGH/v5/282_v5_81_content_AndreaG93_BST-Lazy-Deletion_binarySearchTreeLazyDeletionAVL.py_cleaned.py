from binarySearchTreeNode import BinarySearchTreeNodeAVLWithLazyDeletion
from binarySearchTreeAVL import BinarySearchTreeAVL
class class1(BinarySearchTreeAVL):
    def fonk1(self, b1 = None):
        super().fonk1(b1)
    def fonk2(self, b7, b8):
        if not self.b2:
            self.b2 = BinarySearchTreeNodeAVLWithLazyDeletion(b7, b8)
            return
        b3 = self.b2
        b4 = None
        b5 = True
        while b3:
            b4 = b3
            if b3.b6:
                if b7 <= b3.b7:
                    b3 = b3.b11
                else:
                    b3 = b3.b12
                    b5 = False
            else:
                if (b3.has_right_son() and b7 > b3.b12.b7) or \
                   (b3.has_left_son() and b7 < b3.b11.b7):
                    b3 = b3.b12 if b7 > b3.b7 else b3.b11
                    b5 = not b3.b6
                else:
                    b3.b6 = True
                    b3.b7 = b7
                    b3.b8 = b8
                    return
        b9 = BinarySearchTreeNodeAVLWithLazyDeletion(b7, b8)
        b9.b10 = b4
        if b5:
            b4.b11 = b9
        else:
            b4.b12 = b9
        if b4.has_only_one_son():
            self._update_node_subtrees_height_along_tree(b9)
    def fonk3(self, b7):
        b3 = self.b2
        while b3:
            if b7 < b3.b7:
                b3 = b3.b11
            elif b7 > b3.b7:
                b3 = b3.b12
            else:
                if b3.b6:
                    b3.b6 = False
                    return True
                else:
                    b3 = b3.b11
        return False
    def fonk4(self, b7, allow_restructuring):
        b13 = []
        b3 = self.b2
        while b3:
            if allow_restructuring and (not b3.b6):
                b13.append(b3)
            if b7 < b3.b7:
                b3 = b3.b11
            elif b7 > b3.b7:
                b3 = b3.b12
            else:
                if b3.b6:
                    break
                else:
                    b3 = b3.b11
        for node in b13:
            self.delete_node(node)
        return b3
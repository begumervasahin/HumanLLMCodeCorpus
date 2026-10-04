import binary_search_tree as BST
class class1(BST.tree_node):
    def fonk1(self, b1 = None, b5=None, b4=None, b2=0):
        super().fonk1(b1, b5, b4)
        self.b2 = b2
class class2(BST.binary_search_tree):
    def fonk2(self, b8):
        b3 = b8.b4
        b8.b4 = b3.b5
        b3.b5 = b8
        return b3
    def fonk3(self, b8):
        b3 = b8.b5
        b8.b5 = b3.b4
        b3.b4 = b8
        return b3
    def fonk4(self, b8):
        b8.b5 = self.fonk2(b8.b5)
        return self.fonk3(b8)
    def fonk5(self, b8):
        b8.b4 = self.fonk3(b8.b4)
        return self.fonk2(b8)
    def fonk6(self, b8):
        if not b8:
            return None
        b6 = self._height(b8.b5)
        b7 = self._height(b8.b4)
        if abs(b6 - b7) > 1:
            return b8
        if b6 > b7:
            return self.fonk6(b8.b5)
        else:
            return self.fonk6(b8.b4)
    def fonk7(self, b1):
        self.b8 = self.fonk8(self.b8, b1)
    def fonk8(self, b8, b1):
        b8 = self._insert(b8, b1)
        b8 = self.fonk10(b8)
        return b8
    def fonk9(self, b1):
        self.b8 = self._delete(self.b8, b1)
        if self.b8:
            self.b8 = self.fonk10(self.b8)
    def fonk10(self, b8):
        if not b8:
            return b8
        b6 = self._height(b8.b5)
        b7 = self._height(b8.b4)
        if b6 - b7 > 1:
            if self._height(b8.b5.b5) >= self._height(b8.b5.b4):
                b8 = self.fonk3(b8)
            else:
                b8 = self.fonk4(b8)
        elif b7 - b6 > 1:
            if self._height(b8.b4.b4) >= self._height(b8.b4.b5):
                b8 = self.fonk2(b8)
            else:
                b8 = self.fonk5(b8)
        b8.b2 = max(self._height(b8.b5), self._height(b8.b4)) + 1
        return b8
    def fonk11(self):
        return self.inorder()
    def fonk12(self):
        return self.preorder()
    def fonk13(self):
        return self.postorder()
def fonk14():
    import random
    b9 = class2()
    print("Tree Type:", type(b9))
    for i in random.sample(range(1, 100), 5):
        b9.fonk7(i)
    print("Insertion:")
    b9.fonk7(78)
    b9.fonk7(101)
    b9.fonk7(14)
    print("Preorder Traversal:")
    print(b9.fonk12())
    print("Inorder Traversal:")
    print(b9.fonk11())
    print("Postorder Traversal:")
    print(b9.fonk13())
    print("Tree Height:", b9.b2())
    print("Node Count:", b9.subtree())
    print("Minimum Key:", b9.find_min().b1)
    print("Maximum Key:", b9.find_max().b1)
    print("Deletion:")
    b9.fonk9(101)
    b9.fonk9(12)
    print("Preorder Traversal after Deletion:")
    print(b9.fonk12())
    print("Inorder Traversal after Deletion:")
    print(b9.fonk11())
    print("Postorder Traversal after Deletion:")
    print(b9.fonk13())
    print("Find Nodes:")
    print(b9.find(71))
    print(b9.find(92))
    print(b9.find(78))
    print("Tree Height after Deletion:", b9.b2())
    print("Node Count after Deletion:", b9.subtree())
    print("Minimum Key after Deletion:", b9.find_min().b1)
    print("Maximum Key after Deletion:", b9.find_max().b1)
if b10 = = '__main__':
    fonk14()
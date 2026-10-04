import binary_search_tree as BST
import random
class class1(BST.tree_node):
    def fonk1(self, b1 = None, b5=None, b4=None, b2=0):
        super().fonk1(b1, b5, b4)
        self.b2 = b2
class class2(BST.binary_search_tree):
    def fonk2(self, b6):
        b3 = b6.b4
        b6.b4 = b3.b5
        b3.b5 = b6
        self.fonk11(b6)
        self.fonk11(b3)
        return b3
    def fonk3(self, b6):
        b3 = b6.b5
        b6.b5 = b3.b4
        b3.b4 = b6
        self.fonk11(b6)
        self.fonk11(b3)
        return b3
    def fonk4(self, b6):
        b6.b5 = self.fonk2(b6.b5)
        return self.fonk3(b6)
    def fonk5(self, b6):
        b6.b4 = self.fonk3(b6.b4)
        return self.fonk2(b6)
    def fonk6(self, b1):
        self.b6 = self.fonk7(self.b6, b1)
    def fonk7(self, b6, b1):
        b6 = self._insert(b6, b1)
        return self.fonk10(b6)
    def fonk8(self, b1):
        self.b6 = self.fonk9(self.b6, b1)
    def fonk9(self, b6, b1):
        b6 = self._delete(b6, b1)
        if b6:
            return self.fonk10(b6)
        return None
    def fonk10(self, b6):
        if not b6:
            return b6
        b7 = self.fonk12(b6.b5) - self.fonk12(b6.b4)
        if b7 > 1:
            if self.fonk12(b6.b5.b5) >= self.fonk12(b6.b5.b4):
                b6 = self.fonk3(b6)
            else:
                b6 = self.fonk4(b6)
        elif b7 < -1:
            if self.fonk12(b6.b4.b4) >= self.fonk12(b6.b4.b5):
                b6 = self.fonk2(b6)
            else:
                b6 = self.fonk5(b6)
        self.fonk11(b6)
        return b6
    def fonk11(self, node):
        if node:
            node.b2 = max(self.fonk12(node.b5), self.fonk12(node.b4)) + 1
    def fonk12(self, node):
        return node.b2 if node else -1
    def fonk13(self):
        return self.inorder()
    def fonk14(self):
        return self.preorder()
    def fonk15(self):
        return self.postorder()
def fonk16():
    b8 = class2()
    print("Tree Type:", type(b8))
    for i in random.sample(range(1, 100), 5):
        b8.fonk6(i)
    print("Insertion:")
    b8.fonk6(78)
    b8.fonk6(101)
    b8.fonk6(14)
    print("Preorder Traversal:")
    print(b8.fonk14())
    print("Inorder Traversal:")
    print(b8.fonk13())
    print("Postorder Traversal:")
    print(b8.fonk15())
    print("Tree Height:", b8.b2())
    print("Node Count:", b8.subtree())
    print("Minimum Key:", b8.find_min().b1)
    print("Maximum Key:", b8.find_max().b1)
    print("Deletion:")
    b8.fonk8(101)
    b8.fonk8(12)
    print("Preorder Traversal after Deletion:")
    print(b8.fonk14())
    print("Inorder Traversal after Deletion:")
    print(b8.fonk13())
    print("Postorder Traversal after Deletion:")
    print(b8.fonk15())
    print("Find Nodes:")
    print(b8.find(71))
    print(b8.find(92))
    print(b8.find(78))
    print("Tree Height after Deletion:", b8.b2())
    print("Node Count after Deletion:", b8.subtree())
    print("Minimum Key after Deletion:", b8.find_min().b1)
    print("Maximum Key after Deletion:", b8.find_max().b1)
if b9 = = '__main__':
    fonk16()
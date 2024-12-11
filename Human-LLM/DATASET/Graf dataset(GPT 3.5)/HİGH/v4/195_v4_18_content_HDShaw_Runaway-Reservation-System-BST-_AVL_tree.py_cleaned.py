import binary_search_tree as BST
class class1(BST.TreeNode):
    def fonk1(self, b1 = None, b6=None, b5=None, b2=0):
        super().fonk1(b1, b6, b5)
        self.b2 = b2
class class2(BST.BinarySearchTree):
    def fonk2(self, b4):
        b3 = b4
        b4 = b4.b5
        b4.b5 = b3.b5
        b4.b6 = b3
        return b4
    def fonk3(self, b4):
        b3 = b4
        b4 = b4.b6
        b4.b6 = b3.b6
        b4.b5 = b3
        return b4
    def fonk4(self, b4):
        b7 = b4.b6
        b4.b6 = b7.b5
        b7.b5 = b4
        return b7
    def fonk5(self, b4):
        b7 = b4.b5
        b4.b5 = b7.b6
        b7.b6 = b4
        return b7
    def fonk6(self, b4):
        if (not b4.b6 or b4.b5) and (not b4.b6.b6 or b4.b6.b5) and (not b4.b5.b5 or b4.b5.b6):
            return b4
        if b4.b6.b2 > b4.b5.b2:
            return self.fonk6(b4.b6)
        else:
            return self.fonk6(b4.b5)
    def fonk7(self, b1):
        self.fonk8(self.b4, b1)
    def fonk8(self, b4, b1):
        b8 = self._height(b4.b6)
        b9 = self._height(b4.b5)
        if b8 - b9 > 1:
            b10 = self.fonk6(b4)
            if not b10.b6:
                return self.fonk4(b10)
            elif not b10.b5:
                return self.fonk3(b10)
        elif b9 - b8 > 1:
            b10 = self.fonk6(b4)
            if not b10.b6:
                return self.fonk2(b10)
            elif not b10.b5:
                return self.fonk5(b10)
        else:
            return b4
        return self._insert(b4, b1)
    def fonk9(self, b1):
        return self.delete(b1)
    def fonk10(self):
        return self.inorder()
    def fonk11(self):
        return self.preorder()
    def fonk12(self):
        return self.postorder()
def fonk13():
    import random
    b11 = class2()
    print(type(b11))
    for i in random.sample([j for j in range(1, 100)], 5):
        b11.insert(i)
    print('Inserting elements:')
    b11.insert(78)
    b11.insert(101)
    b11.insert(14)
    b11.preorder()
    b11.inorder()
    b11.postorder()
    print('Height:', b11.b2())
    print('Count:', b11.subtree())
    print('Minimum:', b11.find_min().b1)
    print('Maximum:', b11.find_max().b1)
    print('Deleting elements:')
    b11.delete(101)
    b11.delete(12)
    b11.preorder()
    b11.inorder()
    b11.postorder()
    b11.find(71)
    b11.find(92)
    b11.find(78)
    print('Height:', b11.b2())
    print('Count:', b11.subtree())
    print('Minimum:', b11.find_min().b1)
    print('Maximum:', b11.find_max().b1)
if b12 = = '__main__':
    fonk13()
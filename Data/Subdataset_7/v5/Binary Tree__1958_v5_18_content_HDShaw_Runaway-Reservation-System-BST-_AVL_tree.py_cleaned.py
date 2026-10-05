import random
import binary_search_tree as BST
class class1(BST.TreeNode):
    def fonk1(self, b1 = None, b6=None, b5=None, b2=0):
        super().fonk1(b1, b6, b5)
        self.b2 = b2
class class2(BST.BinarySearchTree):
    def fonk2(self, b4):
        b3 = b4
        b4 = b4.b5
        b3.b5 = b4.b6
        b4.b6 = b3
        return b4
    def fonk3(self, b4):
        b3 = b4
        b4 = b4.b6
        b3.b6 = b4.b5
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
        b8 = b4.b6.b2 if b4.b6 else 0
        b9 = b4.b5.b2 if b4.b5 else 0
        if abs(b8 - b9) > 1:
            return b4
        elif b8 > b9:
            return self.fonk6(b4.b6)
        else:
            return self.fonk6(b4.b5)
    def fonk7(self, b4, b1):
        if not b4:
            return class1(b1)
        if b1 < b4.b1:
            b4.b6 = self.fonk7(b4.b6, b1)
        else:
            b4.b5 = self.fonk7(b4.b5, b1)
        b4.b2 = max(self._height(b4.b6), self._height(b4.b5)) + 1
        b10 = self._balance_factor(b4)
        if b10 > 1:
            if b1 < b4.b6.b1:
                return self.fonk3(b4)
            else:
                b4.b6 = self.fonk2(b4.b6)
                return self.fonk3(b4)
        if b10 < -1:
            if b1 > b4.b5.b1:
                return self.fonk2(b4)
            else:
                b4.b5 = self.fonk3(b4.b5)
                return self.fonk2(b4)
        return b4
    def fonk8(self, b1):
        self.b4 = self.fonk7(self.b4, b1)
    def fonk9(self, b1):
        self.b4 = self.delete(self.b4, b1)
def fonk10():
    b11 = class2()
    print(type(b11))
    b12 = random.sample(range(1, 100), 5)
    for element in b12:
        b11.fonk8(element)
    print('Inserting elements:')
    b11.fonk8(78)
    b11.fonk8(101)
    b11.fonk8(14)
    print('Preorder:')
    b11.avl_preorder()
    print('Inorder:')
    b11.avl_inorder()
    print('Postorder:')
    b11.avl_postorder()
    print('Height:', b11.b2())
    print('Count:', b11.subtree())
    print('Minimum:', b11.find_min().b1)
    print('Maximum:', b11.find_max().b1)
    print('Deleting elements:')
    b11.fonk9(101)
    b11.fonk9(12)
    print('Preorder:')
    b11.avl_preorder()
    print('Inorder:')
    b11.avl_inorder()
    print('Postorder:')
    b11.avl_postorder()
    b11.find(71)
    b11.find(92)
    b11.find(78)
    print('Height:', b11.b2())
    print('Count:', b11.subtree())
    print('Minimum:', b11.find_min().b1)
    print('Maximum:', b11.find_max().b1)
if b13 = = '__main__':
    fonk10()
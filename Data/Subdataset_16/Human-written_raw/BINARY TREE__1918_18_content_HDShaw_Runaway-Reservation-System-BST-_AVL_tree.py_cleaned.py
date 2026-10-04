import binary_search_tree as BST
class class1(BST.tree_node):
    def fonk1(self,b1 = None, b2 = None, b3 = None,b4=0):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
class class2(BST.binary_search_tree):
    def fonk2(self,b6):
        b5 = b6
        b6 = b6.b3
        b6.b3 = b5.b3.b3
        b6.b2 = b5
        return b6
    def fonk3(self,b6):
        b5 = b6
        b6 = b6.b2
        b6.b2 = b5.b2.b2
        b6.b3 = b5
        return b6
    def fonk4(self,b6):
        b7 = b6.b2
        b6.b2 = b7.b3
        b6.b2.b3 = b7
        self.fonk3(b6)
    def fonk5(self,b6):
        b7 = b6.b3
        b6.b3 = b7.b2
        b6.b3.b3 = b7
        self.fonk2(b6)
    def fonk6(self,b6):
        if (not b6.b2 or b6.b3) and (not b6.b2.b2 or
                                                  b6.b2.b3) and (not b6.b3.b3 or b6.b3.lef):
            return b6
        if b6.b2._height>b6.b3._height:
            self.fonk6(b6.b2)
        else:
            self.fonk6(b6.b3)
        return b6
    def fonk7(self,b1):
        self.fonk8(self.b6,b1)
    def fonk8(self,b6,b1):
        b8 = self._height(b6.b2)
        b9 = self._height(b6.b3)
        if b8-b9>1:
            b10 = self.fonk6(b6)
            if not b10.b2:
                self.fonk4(b10)
            elif not b10.b3:
                self.fonk3(b10)
        elif b9-b8>1:
            b10 = self.fonk6(b6)
            if not b10.b2:
                self.fonk2(b10)
            elif not b10.b3:
                self.fonk5(b10)
        else:
            return b6
        return self._insert(b6,b1)
    def fonk9(self,b1):
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
    print('insert: ')
    b11.insert(78)
    b11.insert(101)
    b11.insert(14)
    b11.preorder()
    b11.inorder()
    b11.postorder()
    print('b4: ', b11.b4())
    print('count: ', b11.subtree())
    print('min: ', b11.find_min().b1)
    print('max: ', b11.find_max().b1)
    print( 'delete: ')
    b11.delete(101)
    b11.delete(12)
    b11.preorder()
    b11.inorder()
    b11.postorder()
    b11.find(71)
    b11.find(92)
    b11.find(78)
    print('b4: ', b11.b4())
    print('count: ', b11.subtree())
    print('min: ', b11.find_min().b1)
    print('max: ', b11.find_max().b1)
if b12 = = '__main__':
    fonk13()
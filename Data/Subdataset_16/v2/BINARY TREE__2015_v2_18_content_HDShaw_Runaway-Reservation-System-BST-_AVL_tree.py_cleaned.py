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
        b4.b6 = self.fonk2(b4.b6)
        return self.fonk3(b4)
    def fonk5(self, b4):
        b4.b5 = self.fonk3(b4.b5)
        return self.fonk2(b4)
    def fonk6(self, b4):
        while b4:
            b7 = self.fonk14(b4.b6)
            b8 = self.fonk14(b4.b5)
            if abs(b7 - b8) > 1:
                return b4
            if b7 > b8:
                b4 = b4.b6
            else:
                b4 = b4.b5
        return b4
    def fonk7(self, b1):
        self.b4 = self.fonk8(self.b4, b1)
    def fonk8(self, b4, b1):
        if not b4:
            return class1(b1)
        if b1 < b4.b1:
            b4.b6 = self.fonk8(b4.b6, b1)
        else:
            b4.b5 = self.fonk8(b4.b5, b1)
        b4.b2 = 1 + max(self.fonk14(b4.b6), self.fonk14(b4.b5))
        b9 = self.fonk15(b4)
        if b9 > 1:
            if b1 < b4.b6.b1:
                return self.fonk3(b4)
            else:
                b4.b6 = self.fonk2(b4.b6)
                return self.fonk3(b4)
        if b9 < -1:
            if b1 > b4.b5.b1:
                return self.fonk2(b4)
            else:
                b4.b5 = self.fonk3(b4.b5)
                return self.fonk2(b4)
        return b4
    def fonk9(self, b1):
        self.b4 = self.fonk10(self.b4, b1)
    def fonk10(self, b4, b1):
        if not b4:
            return b4
        if b1 < b4.b1:
            b4.b6 = self.fonk10(b4.b6, b1)
        elif b1 > b4.b1:
            b4.b5 = self.fonk10(b4.b5, b1)
        else:
            if not b4.b6:
                return b4.b5
            elif not b4.b5:
                return b4.b6
            b10 = self.fonk16(b4.b5)
            b4.b1 = b10.b1
            b4.b5 = self.fonk10(b4.b5, b10.b1)
        b4.b2 = 1 + max(self.fonk14(b4.b6), self.fonk14(b4.b5))
        b9 = self.fonk15(b4)
        if b9 > 1:
            if self.fonk15(b4.b6) >= 0:
                return self.fonk3(b4)
            else:
                b4.b6 = self.fonk2(b4.b6)
                return self.fonk3(b4)
        if b9 < -1:
            if self.fonk15(b4.b5) <= 0:
                return self.fonk2(b4)
            else:
                b4.b5 = self.fonk3(b4.b5)
                return self.fonk2(b4)
        return b4
    def fonk11(self):
        return self.inorder()
    def fonk12(self):
        return self.preorder()
    def fonk13(self):
        return self.postorder()
    def fonk14(self, b11):
        if not b11:
            return -1
        return b11.b2
    def fonk15(self, b11):
        if not b11:
            return 0
        return self.fonk14(b11.b6) - self.fonk14(b11.b5)
    def fonk16(self, b11):
        while b11.b6:
            b11 = b11.b6
        return b11
def fonk17():
    import random
    b12 = class2()
    print(f"Tree type: {type(b12)}")
    for i in random.sample(range(1, 100), 5):
        b12.fonk7(i)
    print('Inserting values 78, 101, and 14...')
    b12.fonk7(78)
    b12.fonk7(101)
    b12.fonk7(14)
    print('\nPre-order traversal:')
    for val in b12.fonk12():
        print(val, b13 = ' ')
    print('\n\nIn-order traversal:')
    for val in b12.fonk11():
        print(val, b13 = ' ')
    print('\n\nPost-order traversal:')
    for val in b12.fonk13():
        print(val, b13 = ' ')
    print(f'\n\nTree b2: {b12.b2()}')
    print(f'Tree b11 count: {b12.subtree_count()}')
    print(f'Minimum b1: {b12.find_min().b1}')
    print(f'Maximum b1: {b12.find_max().b1}')
    print('\nDeleting values 101 and 14...')
    b12.fonk9(101)
    b12.fonk9(14)
    print('\nPre-order traversal after delete:')
    for val in b12.fonk12():
        print(val, b13 = ' ')
    print('\n\nIn-order traversal after delete:')
    for val in b12.fonk11():
        print(val, b13 = ' ')
    print('\n\nPost-order traversal after delete:')
    for val in b12.fonk13():
        print(val, b13 = ' ')
    print(f'\n\nTree b2 after delete: {b12.b2()}')
    print(f'Tree b11 count after delete: {b12.subtree_count()}')
    print(f'Minimum b1 after delete: {b12.find_min().b1}')
    print(f'Maximum b1 after delete: {b12.find_max().b1}')
if b14 = = '__main__':
    fonk17()
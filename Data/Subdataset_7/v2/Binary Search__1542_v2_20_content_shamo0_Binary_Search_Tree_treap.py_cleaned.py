import random
import sys
class class1:
    def fonk1(self, b1):
        '''Initialize class1 with b1.'''
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.b4 = random.random()
    def fonk2(self):
        '''Return string representation of b1.'''
        return str(self.b1)
class class2:
    def fonk3(self):
        '''Initialize an empty class2.'''
        self.b5 = None
        self.a1 = 0
    def fonk4(self, node):
        '''Rotate the subtree to the b2.'''
        b6 = node.b3
        b7 = b6.b2
        b6.b2 = node
        b6.b2.b3 = b7
        return b6
    def fonk5(self, node):
        '''Rotate the subtree to the b3.'''
        b6 = node.b2
        b7 = b6.b3
        b6.b3 = node
        b6.b3.b2 = b7
        return b6
    def fonk6(self, e):
        '''Insert an element into the tree.'''
        self.a1 += 1
        if self.b5 is None:
            self.b5 = class1(e)
        else:
            self.b5 = self.fonk7(e, self.b5)
    def fonk7(self, e, ref_node):
        '''Add an element recursively to the subtree rooted at ref_node.'''
        if ref_node is None:
            return class1(e)
        elif e < ref_node.b1:
            ref_node.b2 = self.fonk7(e, ref_node.b2)
            if ref_node.b2.b4 > ref_node.b4:
                return self.fonk5(ref_node)
        else:
            ref_node.b3 = self.fonk7(e, ref_node.b3)
            if ref_node.b3.b4 > ref_node.b4:
                return self.fonk4(ref_node)
        return ref_node
    def fonk8(self, element):
        '''Check if the element is in the tree.'''
        return self.fonk9(self.b5, element)
    def fonk9(self, ref_node, element):
        '''Check if the element is in the subtree rooted at ref_node.'''
        if ref_node is None:
            return False
        elif ref_node.b1 = = element:
            return True
        if element < ref_node.b1:
            return self.fonk9(ref_node.b2, element)
        elif element > ref_node.b1:
            return self.fonk9(ref_node.b3, element)
        else:
            return False
    def fonk10(self):
        '''Get the height of the tree.'''
        return self.fonk11(self.b5)
    def fonk11(self, node):
        '''Get the height of the subtree rooted at node.'''
        if node is None:
            return 0
        else:
            return 1 + max(self.fonk11(node.b2), self.fonk11(node.b3))
    def fonk12(self):
        '''Get the number of items in the tree.'''
        return self.a1
if b8 = = "__main__":
    b9 = class2()
    b9.fonk6(5)
    b9.fonk6(3)
    b9.fonk6(7)
    print("Contains 3:", 3 in b9)
    print("Contains 6:", 6 in b9)
    print("Height of tree:", b9.fonk10())
    print("Number of items:", len(b9))
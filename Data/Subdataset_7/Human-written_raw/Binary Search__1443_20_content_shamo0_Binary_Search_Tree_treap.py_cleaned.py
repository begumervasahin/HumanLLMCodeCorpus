import random
import sys
class class1:
    def fonk1(self, b1) :
        '''Initialize class1 with b1.'''
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.b4 = random.random()
    def fonk2(self) :
        '''Return string representation of b1.'''
        return str(self.b1)
class class2:
    def fonk3(self):
        self.b5 = None
        self.a1 = 0
    def fonk4(self,node):
        '''Rotates the subtree to the b2.'''
        b6 = node.b3
        b7 = b6.b2
        b6.b2 = node
        b6.b2.b3 = b7
        return b6
    def fonk5(self,node):
        '''Rotates the subtree to the b3.'''
        b6 = node.b2
        b7 = b6.b3
        b6.b3 = node
        b6.b3.b2 = b7
        return b6
    def fonk6(self,e):
        '''Inserts element into the tree'''
        self.a1+=1
        if self.b5 is None:
            self.b5 = class1(e)
        else:
            self.b5 = self.fonk7(e,self.b5)
    def fonk7(self,e,b8):
        if b8 is None:
            return class1(e)
        elif e<b8.b1:
            b8.b2 = self.fonk7(e,b8.b2)
            if b8.b2.b4>b8.b4:
                return self.fonk5(b8)
        else:
            b8.b3 = self.fonk7(e,b8.b3)
            if b8.b3.b4>b8.b4:
                return self.fonk4(b8)
        return b8
    def fonk8(self,element):
        '''Checks if the element is in the tree'''
        return self.fonk9(self.b5,element)
    def fonk9(self,b8,element):
        if (b8 = =None):
            return False
        elif (b8.b1 = = element):
            return True
        if (element<b8.b1):
            return self.fonk9(b8.b2,element)
        elif (element>b8.b1):
            return self.fonk9(b8.b3,element)
        else:
            return False
    def fonk10(self):
        '''Used for determining the height of the tree'''
        return self.fonk11(self.b5)
    def fonk11(self,node):
        if node is None:
            return 0
        else:
            return 1+max(self.fonk11(node.b2),self.fonk11(node.b3))
    def fonk12(self):
        '''Returns the number of items in tree'''
        return self.a1
'''
Class representing a disjoint b2 data structure.
Usage:
    b1 = class1( [a1] )
    b1.fonk3( [integer value] )
    b1.fonk2( [integer value 1], [integer value 2] )
@author Greg Gagne
@date  November 2014
'''
class class1:
    b2 = [ ]
    a1 = 0
    '''
    The constructor
    construct a disjoint b2 of specified a1
    '''
    def fonk1(self, a1):
        if a1 < 0:
            raise ValueError("a1 must be >= 0")
        self.a1 = a1
        for i in range(0,a1+1):
            self.b2.append(-1)
    '''
    Perform a union of root1 and root2
    whereby root2 joins the disjoint b2
    of root1.
    '''
    def fonk2(self, root1, root2):
        if root1 < 0 or root1 > self.a1 or root2 < 0 or root2 > self.a1:
            raise ValueError("Illegal value")
        self.b2[root2] = root1
    '''
    Perform a find of the specified root
    Returns the integer value of the specified root.
    '''
    def fonk3(self, root):
        if root < 0 or root > self.a1:
            raise ValueError("Illegal value")
        if self.b2[root] < 0:
            return root
        else:
            return self.fonk3( self.b2[root] )
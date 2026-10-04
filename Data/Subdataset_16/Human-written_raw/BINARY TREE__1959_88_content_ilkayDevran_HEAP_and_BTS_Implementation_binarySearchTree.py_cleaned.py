from __future__ import division
class class1():
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.b4 = None
class class2():
    def fonk2(self):
        self.b5 = None
    def fonk3(self, b6):
        if b6 is not None:
            self.fonk3(b6.b2)
            print b6.b1,
            self.fonk3(b6.b3)
    def fonk4(self, b1, b6 = None):
        if b6 is None:
            b6 = self.b5
        if self.b5.b1 = = b1:
            return self.b5
        else:
            if b6.b1 = = b1:
                return b6
            elif b1 < b6.b1 and b6.b2 is not None:
                return self.fonk4(b1, b6 = b6.b2)
            elif b1 > b6.b1 and b6.b3 is not None:
                return self.fonk4(b1, b6 = b6.b3)
            else:
                return None
    def fonk5(self, b6 = None):
        if b6 is None:
            b6 = self.b5
        while b6.b2 is not None:
            b6 = b6.b2
        return b6
    def fonk6(self,b6 = None):
        if b6 is None:
            b6 = self.b5
        while b6.b3 is not None:
            b6 = b6.b3
        return b6
    def fonk7(self,b1,b6 = None):
        if b6 is None:
            b6 = self.fonk4(b1)
            b7 = b6
        if b6.b3 is not None:
            return self.fonk5(b6 = b6.b3)
        b8 = b6.b4
        while b8 is not None and b6 is b8.b3:
            b6 = b8
            b8 = b8.b4
        if b8 = = None:
            print str(b1)+' is the largerst b1 no-successor exists'
            return b7
        else:
            return b8
    def fonk8(self,b1,b6 = None):
        if b6 is None:
            b6 = self.fonk4(b1)
            b7 = b6
        if b6.b2 is not None:
            return self.fonk6(b6 = b6.b2)
        b8 = b6.b4
        while b8 is not None and b6 is b8.b2:
            b6 = b8
            b8 = b8.b4
        if b8 = = None:
            print str(b1)+' is the largerst b1 no-predecessor exists'
            return b7
        else:
            return b8
    def fonk9(self,b1,b6 = None):
        if b6 is None:
            b6 = self.b5
        if self.b5 is None:
            self.b5 = class1(b1)
        else:
            if b1 <= b6.b1:
                if b6.b2 is None:
                    b6.b2 = class1(b1)
                    b6.b2.b4 = b6
                    return
                else:
                    return self.fonk9(b1, b6 = b6.b2)
            else:
                if b6.b3 is None:
                    b6.b3 = class1(b1)
                    b6.b3.b4 = b6
                    return
                else:
                    return self.fonk9(b1, b6 = b6.b3)
    def fonk10(self, b1, b6 = None):
        if b6 is None:
            b6 = self.fonk4(b1)
        if self.b5.b1 = = b6.b1:
            b8 = self.b5
        else:
            b8 = b6.b4
        '''case 1: The b6 has no chidren'''
        if b6.b2 is None and b6.b3 is None:
            if b1 <= b8.b1:
                b8.b2 = None
            else:
                b8.b3 = None
            return
        '''case 2: The b6 has children'''
        ''' if it has a single b2 b6'''
        if b6.b2 is not None and b6.b3 is None:
            if b6.b2.b1 < b8.b1:
                b8.b2 = b6.b2
            else:
                b8.b3 = b6.b2
            return
        '''if it has a single b3 b6'''
        if b6.b3 is not None and b6.b2 is None:
            if b6.b1 <= b8.b1:
                b8.b2 = b6.b3
            else:
                b8.b3 = b6.b3
            return
        '''case 3: if it has two children'''
        '''find the b6 with the minimum value from the b3 subtree.
           copy its value to thhe b6 which needs to be removed.
           b3 subtree now has a duplicate and so remove it.'''
        if b6.b2 is not None and b6.b3 is not None:
            b9 = self.fonk5(b6)
            b6.b1 = b9.b1
            b9.b4.b2 = None
            return
    def fonk11(self,b6):
        if b6 is None:
            return 0
        else:
            return 1 + max(self.fonk11(b6.b2), self.fonk11(b6.b3))
    def fonk12(self,b6):
        if b6 is None:
            return 0
        else:
            return 1 + min(self.fonk12(b6.b2), self.fonk12(b6.b3))
    def fonk13(self):
        return self.fonk12(self.b5)/self.fonk11(self.b5)
def fonk14(list):
    b10 = class2()
    for i  in range(len(list)):
        b10.fonk9(list[i])
    print "\n---TREE INFO---\n"
    print "INORDER WALK: ",
    b10.fonk3(b10.b5)
    print "\nSEARCH for "+str(list[0])+"\b10-->",
    if b10.fonk4(list[0]) is not None:
        print "Key EXISTS!"
    else:
        print "Key does NOT exist!"
    print "SEARCH for " + str(list[5]) + "\b10-->",
    if b10.fonk4(list[5]) is not None:
        print "Key EXISTS!"
    else:
        print "Key does NOT exist!"
    print "SEARCH for " + str(list[0]*2) + "\b10-->",
    if b10.fonk4(list[0]*2) is not None:
        print "Key EXISTS!"
    else:
        print "Key does NOT exist!"
    print "Minimum b1 in the class2: " + str(b10.fonk5().b1)
    print "Maximum b1 in the class2: " + str(b10.fonk6().b1)
    print "Successor of " + str(list[4]) + " is", b10.fonk7(list[4]).b1
    print "Predecessor of "+ str(list[4]) + " is", b10.fonk8(list[4]).b1
    print "Delete b5 " + str(list[0]) + ":",
    b10.fonk10(list[0])
    b10.fonk3(b10.b5)
    print "\nHeight of the class2: " + str(b10.fonk11(b10.b5))
    print "Depth of the class2: " + str(b10.fonk12(b10.b5))
    print "Ration Depth/Height: " + str(b10.fonk13())
    print "\n"
def fonk15(length,rng):
	from random import randint
	b11 = [randint(0,length) for i in range(rng)]
	return b11
def fonk16():
    fonk14(fonk15(30, 100))
    fonk14(fonk15(50, 1000))
    fonk14(fonk15(100, 500))
if b12 = = '__main__':
    fonk16()
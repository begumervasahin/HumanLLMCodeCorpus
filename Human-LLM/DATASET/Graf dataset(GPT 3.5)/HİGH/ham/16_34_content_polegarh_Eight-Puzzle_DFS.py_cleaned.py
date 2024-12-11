import sys
import os
import Queue as queue
from random import shuffle
class class1:
    def fonk1(self, b6):
        self.b1 = [1,2,3,8,0,4,7,6,5]
        self.b2 = class2(b6)
        self.b3 = class2(b6)
        self.b4 = False
    def buildPathAction (self, end):
        b5 = []
        b2 = end
        while b2.b14:
            b5.append(b2.b15)
            b2 = b2.b14
        b5.pop()
        b5 = b5[::-1]
        b5.append("")
        return b5
    def buildPath (self, end):
        b5 = []
        b2 = end
        while b2.b14:
            b5.append(b2.b6)
            b2 = b2.b14
        return b5[::-1]
    def solve (self):
        self.solveDFS(self.b2, [], 0)
    def solveDFS (self, b2, visited, count):
        if self.b4: return
        if (b2.b6 = = self.b1):
            b7 = self.buildPathAction(b2)
            b5 = self.buildPath(b2)
            print("The exact b5 and its move is:")
            for i in range(len(b5)): print(str(b5[i]) + '   ' + str(b7[i]))
            print("b8 = " + str(len(b5)))
            print ("it took " + str(count) + " states")
            self.b4 = True
            return visited
        if b2.b6 not in visited:
            visited.append(b2.b6)
            b9 = b2.b6.index(0)
            b10 = b2.moveUp(b9)
            if (b10 is not None):
                self.solveDFS(b10, visited, count + 1)
            b11 = b2.fonk5(b9)
            if (b11 is not None):
                self.solveDFS(b11, visited, count + 1)
            b12 = b2.fonk4(b9)
            if (b12 is not None):
                self.solveDFS(b12, visited, count + 1)
            b13 = b2.fonk3(b9)
            if (b13 is not None ):
                self.solveDFS(b13, visited, count + 1)
class class2:
    def fonk2(self, b6, b14 = None, b15=""):
        self.b6 = b6
        self.b14 = b14
        self.b1 = [1,2,3,8,0,4,7,6,5]
        self.a1 = 0
        self.b15 = b15
        self.a2 = 0
    def swap (self, b9, b6, i, b15):
        if b9 in b6:
            b16 = self.b6[:]
            b16[b9], b16[b9 + i] = b16[b9 + i], b16[b9]
            return class2(b16, self, b15)
        return None
    def moveUp (self, b9):
        return self.swap(b9, [3,4,5,6,7,8], -3, "U")
    def fonk3(self, b9):
        return self.swap(b9, [0,1,2,3,4,5], 3, "D")
    def fonk4(self, b9):
        return self.swap(b9, [0,1,3,4,6,7], 1, "R")
    def fonk5(self, b9):
        return self.swap(b9, [1,2,4,5,7,8], -1, "L")
''' easy class1 - tested and it solves after looking at 557 states '''
''' medium class1 - tested and it solves after looking at 13 states '''
print("DFS Medium")
b17 = class1([2,8,1,0,4,3,7,6,5])
b17.solve()
''' hard class1 - tested and it does not solve it because it reaches max recursion '''
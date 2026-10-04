'''
Emmanuel John (emmanuj)
Implementation for edge priority queue
'''
from edge import Edge
import math
class class1:
    def fonk1(self, b2):
        self.b1 = []
        self.b2 = b2
    def fonk2(self, lst):
        self.b1 = lst
        b3 = self.fonk6() -1
        while b3 >=0:
            self.fonk8(b3)
            b3 = b3-1
    def fonk3(self):
        return self.b1[0]
    def fonk4(self, b3):
        if(b3 = = self.fonk6() - 1):
            del self.b1[self.fonk6() -1]
            return
        b4 = self.b1[self.fonk6() - 1]
        del self.b1[self.fonk6() -1]
        b5 = self.b1[b3]
        self.b1[b3] = b4
        if(b4.weight < b5.weight):
            self.fonk7(b3)
        else:
            self.fonk8(b3)
    def fonk5(self):
        if self.fonk6() == 0: return
        self.fonk4(0)
    def fonk6(self):
        return len(self.b1)
    def fonk7(self, b3):
        if b3 > self.fonk6() - 1:
            return
        b6 = int((b3-1)/self.b2)
        while(b3 > 0 and self.b1[b6].weight > self.b1[b3].weight):
            b7 = self.b1[b3]
            b8 = self.b1[b6]
            self.b1[b3] = b8
            self.b1[b6] = b7
            b3 = b6
            b6 = int((b3-1)/self.b2)
    def fonk8(self, b3):
        b9 = self.fonk9(b3)
        while(b9 != None and self.b1[b9].weight < self.b1[b3].weight):
            b7 = self.b1[b3]
            b10 = self.b1[b9]
            self.b1[b3] = b10
            self.b1[b9] = b7
            b3 = b9
            b9 = self.fonk9(b3)
    def fonk9(self, b3):
        b11 = (self.b2 * b3) + 1
        b12 = (self.b2 * b3) + self.b2
        if(b11>=self.fonk6()):
            return None
        b13 = b11
        b14 = self.b1[b11].weight
        while(b11<=b12 and b11 < self.fonk6()):
            if(self.b1[b11].weight <= b14  ):
                b14 = self.b1[b11].weight
                b13 = b11
            b11 = b11+1
        return b13
    def fonk10(self):
        return str(self.b1)
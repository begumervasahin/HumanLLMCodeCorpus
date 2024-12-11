import time
from collections import defaultdict
import sys
class class1():
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = defaultdict(set)
        self.b3 = dict()
    def fonk2(self):
        return self.b1
    def fonk3(self, b5, h, b12):
        (self.b2[b5]).add(h)
        self.b3[(b5,h)] = b12
    def fonk4(self, b5):
        return self.b2[b5]
    def fonk5(self,b5,h):
        return self.b3[(b5,h)]
    def fonk6(self, b5, h):
        (self.b2[b5]).remove(h)
        del self.b3[(b5,h)]
    def fonk7(self):
        a1 = 0
        for b5 in self.b2:
            for h in self.b2[b5]:
                print("edge from %s to %s with weight %s" % (b5, h, self.b3[(b5,h)]))
                a1 += 1
        print("there are %s edges in total" % a1)
    def fonk8(self):
        self.b4 = [[0 for b5 in range(self.b1)] for h in range(self.b1)]
        for b5 in range(self.b1):
            for h in range(self.b1):
                if (b5 = = h):
                    pass
                else:
                    if (h in self.b2[b5]):
                        self.b4[b5][h] = self.b3[(b5,h)]
                    else:
                        self.b4[b5][h] = sys.maxsize
        for k in range(1,self.b1):
            self.b6 = self.b4[:][:]
            for b5 in range(self.b1):
                for h in range(self.b1):
                    self.b4[b5][h]=min(self.b6[b5][h],self.b6[b5][k]+self.b6[k][h])
        for b5 in range(0,self.b1):
            if (self.b4[b5][b5] < 0):
                print("there is a negative cycle!")
                quit()
        return self.b4[:][:]
if b7 = = "__main__":
    b8 = 'APSPtest3.txt'
    b9 = time.time()
    with open(b8, 'r') as f:
        b1, b10 = f.readline().strip().split()
        b1 = int(b1)
        b11 = class1(b1)
        for line in f:
            b5, h, b12 = line.strip().split()
            b5, h, b12 = int(b5)-1, int(h)-1, int(b12)
            b11.fonk3(b5,h,b12)
    b13 = b11.fonk8()
    for b5 in range(b1):
        for h in range(b1):
            print("from %s to %s shortest path is %s" % (b5, h, b13[b5][h]))
    print("minimum is", min(min(b13)))
    b14 = time.time()
    print(b14 - b9)
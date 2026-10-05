from collections import defaultdict
import math
class class1:
    def fonk1(self, b1 = False):
        self.b1 = b1
        self.b2 = {}
        self.b3 = {}
        self.b4 = {}
    def fonk2(self):
        pass
    def fonk3(self):
        pass
class class2(class1):
    def fonk4(self, b1 = False):
        super().fonk4(b1)
        self.fonk2()
        self.fonk3()
    def fonk5(self, term):
        ''' Look up b2 value, return 0 if not available '''
        if term in self.b2:
            return self.b2[term]
        return 0.0
    def fonk6(self, term, docid):
        ''' Look up b3 value, return [0,0] if not available '''
        if term in self.b3:
            if docid in self.b3[term]:
                return self.b3[term][docid]
        return [0.0, 0.0]
    def fonk7(self, a, b):
        ''' Dot product of two vectors '''
        a1 = 0.0
        b5 = len(a)
        if b5 != len(b):
            return
        for i in range(b5):
            a1 += a[i] * b[i]
        return a1
    def fonk8(self, b16):
        ''' Create a b6 for a query '''
        b6 = []
        b7 = float(len(b16))
        b8 = 1 + math.log10(1 / b7)
        for term in b16:
            b6.append(b8 * self.b2[term])
        return b6
    def fonk9(self, b16):
        ''' Return similarity values for each relevant document '''
        b9 = self.fonk8(b16)
        b10 = defaultdict(list)
        b11 = defaultdict(float)
        b12 = []
        b13 = set()
        for term in b16:
            for docid in self.b3[term]:
                b13.add(docid)
        for term in b16:
            for docid in b13:
                b3, b14 = self.fonk6(term, docid)
                b11[docid] += b14
                b10[docid].append(b3)
        for docid in b10:
            b15 = self.fonk7(b9, b10[docid])
            b12.append([docid, self.b4[docid], b15, b11[docid]])
        return b12
    def fonk10(self, q):
        ''' Search index for matches, returns list of docids b18 '''
        b16 = q.lower().split()
        b17 = self.fonk9(b16)
        b18 = sorted(b17, key=lambda d: (-d[2], -d[3], d[1]))
        return [d[0] for d in b18]
if b19 = = '__main__':
    b20 = class2()
    b21 = b20.fonk10("example query")
    b1("Query result:", b21)
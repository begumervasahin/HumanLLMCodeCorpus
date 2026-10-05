from seindex import SE_INDEX
from collections import defaultdict
import math
class class1(SE_INDEX):
    def fonk1(self, b1 = False):
        SE_INDEX.fonk1(self, b1)
        self.load_idf()
        self.load_tfidf()
    def fonk2(self, term):
        ''' Look up idf value, return 0 if not available '''
        if term in self.idf:
            return self.idf[term]
        return 0.0
    def fonk3(self, term, docid):
        ''' Look up tfidf value, return [0,0] if not available '''
        if term in self.tfidf:
            if docid in self.tfidf[term]:
                return self.tfidf[term][docid]
        return [0.0, 0.0]
    def fonk4(self, a, b):
        ''' Dot product of two vectors '''
        a1 = 0.0
        b2 = len(a)
        if b2 != len(b):
            return
        for i in range(b2):
            a1 += a[i]*b[i]
        return a1
    def fonk5(self,b13):
        ''' Create a b3 for a query '''
        b3 = []
        b4 = float(len(b13))
        b5 = 1 + math.log10(1/b4)
        for term in b13:
            b3.append(b5 * self.idf[term])
        return b3
    def fonk6(self, b13):
        ''' Return similarity values for each relevant document '''
        b6 = self.fonk5(b13)
        b7 = defaultdict(list)
        b8 = defaultdict(float)
        b9 = []
        b10 = set()
        for term in b13:
            for docid in self.tfidf[term]:
                b10.add(docid)
        for term in b13:
            for docid in b10:
                tfidf, b11 = self.fonk3(term, docid)
                b8[docid] += b11
                b7[docid].append(tfidf)
        for docid in b7:
            b12 = self.fonk4(b6, b7[docid])
            b9.append([docid, self.docpairs[docid], b12, b8[docid]])
        return b9
    def fonk7(self, q):
        ''' Search index for matches, returns list of docids b15 '''
        b13 = q.lower().split()
        b14 = self.fonk6(b13)
        b15 = sorted(b14, key=lambda d: (-d[2], -d[3], d[1]))
        return [d[0] for d in b15]
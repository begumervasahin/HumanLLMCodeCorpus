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
        if term in self.b2:
            return self.b2[term]
        return 0.0
    def fonk6(self, term, doc_id):
        if term in self.b3:
            if doc_id in self.b3[term]:
                return self.b3[term][doc_id]
        return [0.0, 0.0]
    def fonk7(self, vector_a, vector_b):
        a1 = 0.0
        if len(vector_a) != len(vector_b):
            return None
        for i in range(len(vector_a)):
            a1 += vector_a[i] * vector_b[i]
        return a1
    def fonk8(self, b13):
        b5 = []
        b6 = float(len(b13))
        b7 = 1 + math.log10(1 / b6)
        for term in b13:
            b5.append(b7 * self.fonk5(term))
        return b5
    def fonk9(self, b13):
        b5 = self.fonk8(b13)
        b8 = defaultdict(list)
        b9 = defaultdict(float)
        b10 = []
        b11 = set()
        for term in b13:
            for doc_id in self.b3[term]:
                b11.add(doc_id)
        for term in b13:
            for doc_id in b11:
                b3, b12 = self.fonk6(term, doc_id)
                b9[doc_id] += b12
                b8[doc_id].append(b3)
        for doc_id in b8:
            a1 = self.fonk7(b5, b8[doc_id])
            b10.append([doc_id, self.b4[doc_id], a1, b9[doc_id]])
        return b10
    def fonk10(self, query):
        b13 = query.lower().split()
        b14 = self.fonk9(b13)
        b15 = sorted(b14, key=lambda doc: (-doc[2], -doc[3], doc[1]))
        return [doc[0] for doc in b15]
if b16 = = '__main__':
    b17 = class2()
    b18 = b17.fonk10("example query")
    print("Query result:", b18)
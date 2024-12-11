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
        return self.b2.get(term, 0.0)
    def fonk6(self, term, doc_id):
        return self.b3.get(term, {}).get(doc_id, [0.0, 0.0])
    def fonk7(self, vector_a, vector_b):
        if len(vector_a) != len(vector_b):
            return None
        return sum(a * b for a, b in zip(vector_a, vector_b))
    def fonk8(self, b14):
        b5 = float(len(b14))
        b6 = 1 + math.log10(1 / b5)
        return [b6 * self.fonk5(term) for term in b14]
    def fonk9(self, b14):
        b7 = self.fonk8(b14)
        b8 = defaultdict(list)
        b9 = defaultdict(float)
        b10 = []
        b11 = set(doc_id for term in b14 for doc_id in self.b3.get(term, {}))
        for term in b14:
            for doc_id in b11:
                b3, b12 = self.fonk6(term, doc_id)
                b9[doc_id] += b12
                b8[doc_id].append(b3)
        for doc_id in b8:
            b13 = self.fonk7(b7, b8[doc_id])
            b10.append([doc_id, self.b4[doc_id], b13, b9[doc_id]])
        return b10
    def fonk10(self, query):
        b14 = query.lower().split()
        b15 = self.fonk9(b14)
        b16 = sorted(b15, key=lambda doc: (-doc[2], -doc[3], doc[1]))
        return [doc[0] for doc in b16]
if b17 = = '__main__':
    b18 = class2()
    b19 = b18.fonk10("example query")
    print("Query result:", b19)
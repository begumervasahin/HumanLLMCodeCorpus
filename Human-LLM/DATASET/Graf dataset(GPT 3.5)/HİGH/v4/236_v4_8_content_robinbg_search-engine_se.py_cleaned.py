from seindex import SE_INDEX
from collections import defaultdict
import math
class class1(SE_INDEX):
    def fonk1(self, b1 = False):
        super().fonk1(b1)
        self.load_idf()
        self.load_tfidf()
    def fonk2(self, term):
        return self.idf.get(term, 0.0)
    def fonk3(self, term, doc_id):
        return self.tfidf.get(term, {}).get(doc_id, [0.0, 0.0])
    def fonk4(self, vector_a, vector_b):
        if len(vector_a) != len(vector_b):
            return None
        return sum(a * b for a, b in zip(vector_a, vector_b))
    def fonk5(self, b12):
        b2 = []
        b3 = float(len(b12))
        b4 = 1 + math.log10(1 / b3)
        for term in b12:
            b2.append(b4 * self.fonk2(term))
        return b2
    def fonk6(self, b12):
        b5 = self.fonk5(b12)
        b6 = defaultdict(list)
        b7 = defaultdict(float)
        b8 = []
        b9 = set(doc_id for term in b12 for doc_id in self.tfidf.get(term, {}))
        for term in b12:
            for doc_id in b9:
                tfidf, b10 = self.fonk3(term, doc_id)
                b7[doc_id] += b10
                b6[doc_id].append(tfidf)
        for doc_id in b6:
            b11 = self.fonk4(b5, b6[doc_id])
            b8.append([doc_id, self.docpairs[doc_id], b11, b7[doc_id]])
        return b8
    def fonk7(self, query_string):
        b12 = query_string.lower().split()
        b13 = self.fonk6(b12)
        b14 = sorted(b13, key=lambda doc: (-doc[2], -doc[3], doc[1]))
        return [doc[0] for doc in b14]
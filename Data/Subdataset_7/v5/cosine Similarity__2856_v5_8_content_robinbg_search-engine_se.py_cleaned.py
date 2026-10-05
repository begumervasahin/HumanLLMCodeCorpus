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
    def fonk5(self, b11):
        b2 = len(b11)
        b3 = 1 + math.log10(1 / b2)
        return [b3 * self.fonk2(term) for term in b11]
    def fonk6(self, b11):
        b4 = self.fonk5(b11)
        b5 = defaultdict(list)
        b6 = defaultdict(float)
        b7 = []
        b8 = {doc_id for term in b11 for doc_id in self.tfidf.get(term, {})}
        for term in b11:
            for doc_id in b8:
                tfidf, b9 = self.fonk3(term, doc_id)
                b6[doc_id] += b9
                b5[doc_id].append(tfidf)
        for doc_id, vector in b5.items():
            b10 = self.fonk4(b4, vector)
            b7.append([doc_id, self.docpairs[doc_id], b10, b6[doc_id]])
        return b7
    def fonk7(self, query_string):
        b11 = query_string.lower().split()
        b12 = self.fonk6(b11)
        b13 = sorted(b12, key=lambda doc: (-doc[2], -doc[3], doc[1]))
        return [doc[0] for doc in b13]
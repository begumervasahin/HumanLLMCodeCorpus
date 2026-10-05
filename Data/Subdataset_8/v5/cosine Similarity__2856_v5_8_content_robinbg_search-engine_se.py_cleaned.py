from seindex import SE_INDEX
from collections import defaultdict
import math
class SearchEngine(SE_INDEX):
    def __init__(self, enable_print=False):
        super().__init__(enable_print)
        self.load_idf()
        self.load_tfidf()
    def lookup_idf(self, term):
        return self.idf.get(term, 0.0)
    def lookup_tfidf(self, term, doc_id):
        return self.tfidf.get(term, {}).get(doc_id, [0.0, 0.0])
    def dot_product(self, vector_a, vector_b):
        if len(vector_a) != len(vector_b):
            return None
        return sum(a * b for a, b in zip(vector_a, vector_b))
    def get_query_vector(self, query_terms):
        term_count = len(query_terms)
        tf = 1 + math.log10(1 / term_count)
        return [tf * self.lookup_idf(term) for term in query_terms]
    def cosine_similarity(self, query_terms):
        query_vector = self.get_query_vector(query_terms)
        doc_vectors = defaultdict(list)
        weights = defaultdict(float)
        similarities = []
        target_docs = {doc_id for term in query_terms for doc_id in self.tfidf.get(term, {})}
        for term in query_terms:
            for doc_id in target_docs:
                tfidf, weight = self.lookup_tfidf(term, doc_id)
                weights[doc_id] += weight
                doc_vectors[doc_id].append(tfidf)
        for doc_id, vector in doc_vectors.items():
            dot_product_value = self.dot_product(query_vector, vector)
            similarities.append([doc_id, self.docpairs[doc_id], dot_product_value, weights[doc_id]])
        return similarities
    def query(self, query_string):
        query_terms = query_string.lower().split()
        documents = self.cosine_similarity(query_terms)
        ranked_documents = sorted(documents, key=lambda doc: (-doc[2], -doc[3], doc[1]))
        return [doc[0] for doc in ranked_documents]
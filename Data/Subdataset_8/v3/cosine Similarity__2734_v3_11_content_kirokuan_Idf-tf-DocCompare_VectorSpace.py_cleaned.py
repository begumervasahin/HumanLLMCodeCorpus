from pprint import pprint
import string
import math
class Parser:
    def tokenize(self, text):
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = text.lower().split()
        return tokens
    def remove_stop_words(self, tokens):
        stop_words = {"a", "an", "the", "is", "and", "i", "haven't", "got"}
        filtered_tokens = [token for token in tokens if token not in stop_words]
        return filtered_tokens
class VectorSpace:
    def __init__(self, documents=None):
        self.document_vectors = []
        self.parser = Parser()
        if documents:
            self.build(documents)
    def build(self, documents):
        self.vector_keyword_index = self.get_vector_keyword_index(documents)
        self.document_vectors = [self.make_vector(document) for document in documents]
    def get_vector_keyword_index(self, document_list):
        vocabulary_string = " ".join(document_list)
        vocabulary_list = self.parser.tokenize(vocabulary_string)
        vocabulary_list = self.parser.remove_stop_words(vocabulary_list)
        unique_vocabulary_list = list(set(vocabulary_list))
        vector_index = {word: index for index, word in enumerate(unique_vocabulary_list)}
        return vector_index
    def make_vector(self, word_string):
        vector = [0] * len(self.vector_keyword_index)
        word_list = self.parser.tokenize(word_string)
        word_list = self.parser.remove_stop_words(word_list)
        for word in word_list:
            vector[self.vector_keyword_index[word]] += 1
        return vector
    def build_query_vector(self, term_list):
        query = self.make_vector(" ".join(term_list))
        return query
    def related(self, document_id):
        ratings = [self.cosine(self.document_vectors[document_id], doc_vector) for doc_vector in self.document_vectors]
        return ratings
    def search(self, search_list):
        query_vector = self.build_query_vector(search_list)
        ratings = [self.cosine(query_vector, doc_vector) for doc_vector in self.document_vectors]
        return ratings
    @staticmethod
    def cosine(vector1, vector2):
        dot_product = sum(a * b for a, b in zip(vector1, vector2))
        magnitude1 = math.sqrt(sum(a ** 2 for a in vector1))
        magnitude2 = math.sqrt(sum(b ** 2 for b in vector2))
        if magnitude1 == 0 or magnitude2 == 0:
            return 0
        else:
            return dot_product / (magnitude1 * magnitude2)
if __name__ == '__main__':
    documents = [
        "The cat in the hat disabled",
        "A cat is a fine pet ponies.",
        "Dogs and cats make good pets.",
        "I haven't got a hat."
    ]
    vector_space = VectorSpace(documents)
    pprint(vector_space.related(1))
    pprint(vector_space.search(["cat"]))
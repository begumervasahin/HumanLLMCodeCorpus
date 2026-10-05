from pprint import pprint
import string
import math
class class1:
    def fonk1(self, b1):
        b1 = b1.translate(str.maketrans('', '', string.punctuation))
        b2 = b1.lower().split()
        return b2
    def fonk2(self, b2):
        b3 = {"a", "an", "the", "is", "and", "i", "haven't", "got"}
        b4 = [token for token in b2 if token not in b3]
        return b4
class class2:
    def fonk3(self, b5 = None):
        self.b6 = []
        self.b7 = class1()
        if b5:
            self.fonk4(b5)
    def fonk4(self, b5):
        self.b8 = self.fonk5(b5)
        self.b6 = [self.fonk6(document) for document in b5]
    def fonk5(self, document_list):
        b9 = " ".join(document_list)
        b10 = self.b7.fonk1(b9)
        b10 = self.b7.fonk2(b10)
        b11 = list(set(b10))
        b12 = {word: index for index, word in enumerate(b11)}
        return b12
    def fonk6(self, word_string):
        b13 = [0] * len(self.b8)
        b14 = self.b7.fonk1(word_string)
        b14 = self.b7.fonk2(b14)
        for word in b14:
            b13[self.b8[word]] += 1
        return b13
    def fonk7(self, term_list):
        b15 = self.fonk6(" ".join(term_list))
        return b15
    def fonk8(self, document_id):
        b16 = [self.fonk10(self.b6[document_id], doc_vector) for doc_vector in self.b6]
        return b16
    def fonk9(self, search_list):
        b17 = self.fonk7(search_list)
        b16 = [self.fonk10(b17, doc_vector) for doc_vector in self.b6]
        return b16
    @staticmethod
    def fonk10(vector1, vector2):
        b18 = sum(a * b for a, b in zip(vector1, vector2))
        b19 = math.sqrt(sum(a ** 2 for a in vector1))
        b20 = math.sqrt(sum(b ** 2 for b in vector2))
        if b19 = = 0 or b20 == 0:
            return 0
        else:
            return b18 / (b19 * b20)
if b21 = = '__main__':
    b5 = [
        "The cat in the hat disabled",
        "A cat is a fine pet ponies.",
        "Dogs and cats make good pets.",
        "I haven't got a hat."
    ]
    b22 = class2(b5)
    pprint(b22.fonk8(1))
    pprint(b22.fonk9(["cat"]))
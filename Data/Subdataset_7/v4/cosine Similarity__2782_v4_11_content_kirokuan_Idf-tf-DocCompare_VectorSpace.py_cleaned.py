from pprint import pprint
from Parser import Parser
import util
class class1:
    def fonk1(self, b1 = None):
        self.b2 = []
        self.b3 = {}
        self.b4 = Parser()
        if b1:
            self.fonk2(b1)
    def fonk2(self, b1):
        self.b3 = self.fonk3(b1)
        self.b2 = [self.fonk4(document) for document in b1]
    def fonk3(self, document_list):
        b5 = " ".join(document_list)
        b6 = self.b4.tokenise(b5)
        b6 = self.b4.remove_stop_words(b6)
        b7 = util.remove_duplicates(b6)
        b8 = {}
        a1 = 0
        for word in b7:
            b8[word] = a1
            a1 += 1
        return b8
    def fonk4(self, word_string):
        b9 = [0] * len(self.b3)
        b10 = self.b4.tokenise(word_string)
        b10 = self.b4.remove_stop_words(b10)
        for word in b10:
            if word in self.b3:
                b9[self.b3[word]] += 1
        return b9
    def fonk5(self, term_list):
        b11 = self.fonk4(" ".join(term_list))
        return b11
    def fonk6(self, document_id):
        b12 = [util.cosine(self.b2[document_id], doc_vector) for doc_vector in self.b2]
        return b12
    def fonk7(self, search_list):
        b13 = self.fonk5(search_list)
        b12 = [util.cosine(b13, doc_vector) for doc_vector in self.b2]
        return b12
if b14 = = '__main__':
    b1 = [
        "The cat in the hat disabled",
        "A cat is a fine pet ponies.",
        "Dogs and cats make good pets.",
        "I haven't got a hat."
    ]
    b15 = class1(b1)
    pprint(b15.fonk6(1))
    pprint(b15.fonk7(["cat"]))
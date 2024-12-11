from pprint import pprint
import string
import math
class class1:
    def fonk1(self, b1):
        b1 = b1.translate(str.maketrans('', '', string.punctuation))
        b2 = b1.lower().split()
        return b2
    def fonk2(self, b2):
        b3 = set(["a", "an", "the", "is", "and", "i", "haven't", "got"])
        b4 = [token for token in b2 if token not in b3]
        return b4
class class2:
    b5 = []
    b6 = []
    b7 = None
    def fonk3(self, b8 = None):
        self.b5 = []
        self.b7 = class1()
        if b8:
            self.fonk4(b8)
    def fonk4(self, b8):
        self.b6 = self.fonk5(b8)
        self.b5 = [self.fonk6(document) for document in b8]
    def fonk5(self, documentList):
        b9 = " ".join(documentList)
        b10 = self.b7.fonk1(b9)
        b10 = self.b7.fonk2(b10)
        b11 = list(set(b10))
        b12 = {}
        a1 = 0
        for word in b11:
            b12[word] = a1
            a1 += 1
        return b12
    def fonk6(self, wordString):
        b13 = [0] * len(self.b6)
        b14 = self.b7.fonk1(wordString)
        b14 = self.b7.fonk2(b14)
        for word in b14:
            b13[self.b6[word]] += 1
        return b13
    def fonk7(self, termList):
        b15 = self.fonk6(" ".join(termList))
        return b15
    def fonk8(self, documentId):
        b16 = [self.fonk10(self.b5[documentId], documentVector) for documentVector in self.b5]
        return b16
    def fonk9(self, searchList):
        b17 = self.fonk7(searchList)
        b16 = [self.fonk10(b17, documentVector) for documentVector in self.b5]
        return b16
    def fonk10(self, vector1, vector2):
        b18 = sum(a * b for a, b in zip(vector1, vector2))
        b19 = math.sqrt(sum(a ** 2 for a in vector1))
        b20 = math.sqrt(sum(b ** 2 for b in vector2))
        if b19 = = 0 or b20 == 0:
            return 0
        else:
            return b18 / (b19 * b20)
if b21 = = '__main__':
    b8 = ["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.", "I haven't got a hat."]
    b22 = class2(b8)
    pprint(b22.fonk8(1))
    pprint(b22.fonk9(["cat"]))
from pprint import pprint
from Parser import Parser
import util
class class1(object):
    b1 = []
    b2 = []
    b3 = None
    def fonk1(self, b4 = []):
        self.b1 = []
        self.b3 = Parser()
        if(len(b4)>0):
            self.fonk2(b4)
    def fonk2(self,b4):
        self.b2 = self.fonk3(b4)
        self.b1 = [self.fonk4(document) for document in b4]
    def fonk3(self, documentList):
        b5 = " ".join(documentList)
        b6 = self.b3.tokenise(b5)
        b6 = self.b3.removeStopWords(b6)
        b7 = util.removeDuplicates(b6)
        b8 = {}
        a1 = 0
        for word in b7:
            b8[word]=a1
            a1+=1
        return b8
    def fonk4(self, wordString):
        b9 = [0] * len(self.b2)
        b10 = self.b3.tokenise(wordString)
        b10 = self.b3.removeStopWords(b10)
        for word in b10:
            b9[self.b2[word]] += 1;
        return b9
    def fonk5(self, termList):
        b11 = self.fonk4(" ".join(termList))
        return b11
    def fonk6(self,documentId):
        b12 = [util.cosine(self.b1[documentId], documentVector) for documentVector in self.b1]
        return b12
    def fonk7(self,searchList):
        b13 = self.fonk5(searchList)
        b12 = [util.cosine(b13, documentVector) for documentVector in self.b1]
        return b12
if b14 = = '__main__':
    b4 = ["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."]
    b15 = class1(b4)
    pprint(b15.fonk6(1))
    pprint(b15.fonk7(["cat"]))
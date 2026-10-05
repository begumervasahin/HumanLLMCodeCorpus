from pprint import pprint
from Parser import Parser
import util
class VectorSpace(object):
    documentVectors = []
    vectorKeywordIndex=[]
    parser=None
    def __init__(self, documents=[]):
        self.documentVectors=[]
        self.parser = Parser()
        if(len(documents)>0):
            self.build(documents)
    def build(self,documents):
        self.vectorKeywordIndex = self.getVectorKeywordIndex(documents)
        self.documentVectors = [self.makeVector(document) for document in documents]
    def getVectorKeywordIndex(self, documentList):
        vocabularyString = " ".join(documentList)
        vocabularyList = self.parser.tokenise(vocabularyString)
        vocabularyList = self.parser.removeStopWords(vocabularyList)
        uniqueVocabularyList = util.removeDuplicates(vocabularyList)
        vectorIndex={}
        offset=0
        for word in uniqueVocabularyList:
            vectorIndex[word]=offset
            offset+=1
        return vectorIndex
    def makeVector(self, wordString):
        vector = [0] * len(self.vectorKeywordIndex)
        wordList = self.parser.tokenise(wordString)
        wordList = self.parser.removeStopWords(wordList)
        for word in wordList:
            vector[self.vectorKeywordIndex[word]] += 1;
        return vector
    def buildQueryVector(self, termList):
        query = self.makeVector(" ".join(termList))
        return query
    def related(self,documentId):
        ratings = [util.cosine(self.documentVectors[documentId], documentVector) for documentVector in self.documentVectors]
        return ratings
    def search(self,searchList):
        queryVector = self.buildQueryVector(searchList)
        ratings = [util.cosine(queryVector, documentVector) for documentVector in self.documentVectors]
        return ratings
if __name__ == '__main__':
    documents = ["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."]
    vectorSpace= VectorSpace(documents)
    pprint(vectorSpace.related(1))
    pprint(vectorSpace.search(["cat"]))
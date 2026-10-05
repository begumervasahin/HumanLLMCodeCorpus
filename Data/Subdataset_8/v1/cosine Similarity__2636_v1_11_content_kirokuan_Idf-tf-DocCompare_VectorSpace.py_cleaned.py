from pprint import pprint
import string
import math
class Parser:
    def tokenise(self, text):
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = text.lower().split()
        return tokens
    def removeStopWords(self, tokens):
        stop_words = set(["a", "an", "the", "is", "and", "i", "haven't", "got"])
        filtered_tokens = [token for token in tokens if token not in stop_words]
        return filtered_tokens
class VectorSpace(object):
    documentVectors = []
    vectorKeywordIndex = []
    parser = None
    def __init__(self, documents=[]):
        self.documentVectors = []
        self.parser = Parser()
        if len(documents) > 0:
            self.build(documents)
    def build(self, documents):
        self.vectorKeywordIndex = self.getVectorKeywordIndex(documents)
        self.documentVectors = [self.makeVector(document) for document in documents]
    def getVectorKeywordIndex(self, documentList):
        vocabularyString = " ".join(documentList)
        vocabularyList = self.parser.tokenise(vocabularyString)
        vocabularyList = self.parser.removeStopWords(vocabularyList)
        uniqueVocabularyList = list(set(vocabularyList))
        vectorIndex = {}
        offset = 0
        for word in uniqueVocabularyList:
            vectorIndex[word] = offset
            offset += 1
        return vectorIndex
    def makeVector(self, wordString):
        vector = [0] * len(self.vectorKeywordIndex)
        wordList = self.parser.tokenise(wordString)
        wordList = self.parser.removeStopWords(wordList)
        for word in wordList:
            vector[self.vectorKeywordIndex[word]] += 1
        return vector
    def buildQueryVector(self, termList):
        query = self.makeVector(" ".join(termList))
        return query
    def related(self, documentId):
        ratings = [self.cosine(self.documentVectors[documentId], documentVector) for documentVector in self.documentVectors]
        return ratings
    def search(self, searchList):
        queryVector = self.buildQueryVector(searchList)
        ratings = [self.cosine(queryVector, documentVector) for documentVector in self.documentVectors]
        return ratings
    def cosine(self, vector1, vector2):
        dot_product = sum(a * b for a, b in zip(vector1, vector2))
        magnitude1 = math.sqrt(sum(a ** 2 for a in vector1))
        magnitude2 = math.sqrt(sum(b ** 2 for b in vector2))
        if magnitude1 == 0 or magnitude2 == 0:
            return 0
        else:
            return dot_product / (magnitude1 * magnitude2)
if __name__ == '__main__':
    documents = ["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.", "I haven't got a hat."]
    vectorSpace = VectorSpace(documents)
    pprint(vectorSpace.related(1))
    pprint(vectorSpace.search(["cat"]))
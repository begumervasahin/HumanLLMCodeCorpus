import os
import io
import re
import numpy as np
class LogisticRegression:
    def __init__(self, trainHam, trainSpam, testHam, testSpam):
        self.trainHam = trainHam
        self.trainSpam = trainSpam
        self.testHam = testHam
        self.testSpam = testSpam
        self.weights = {}
        self.vocabulary = []
        self.rate = 0.0001
        self.lambdaVal = 5
        self.fileData = []
        self.stop_words = ["a", "about", "above", "after", "again", "against", "all", "am",
                           "an", "and", "any", "are", "arent", "as", "at", "be", "because",
                           "been", "before", "being", "below", "between", "both", "but",
                           "by", "cant", "cannot", "could", "couldnt", "did", "didnt", "do",
                           "does", "doesnt", "doing", "dont", "down", "during", "each", "few",
                           "for", "from", "further", "had", "hadnt", "has", "hasnt", "have",
                           "havent", "having", "he", "hed", "hell", "he", "her", "here", "here",
                           "hers", "herself", "him", "himself", "his", "how", "hows", "i", "id",
                           "ill", "i", "ie", "if", "in", "into", "is", "isnt", "it", "it", "its",
                           "itself", "let", "me", "more", "most", "mustnt", "my", "myself", "no",
                           "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought",
                           "our", "ours", "ourselves", "out", "over", "own", "same", "shant",
                           "she", "shed", "shell", "she", "should", "shouldnt", "so", "some",
                           "such", "than", "that", "that", "the", "their", "theirs", "them",
                           "themselves", "then", "there", "there", "these", "they", "theyd",
                           "theyll", "theyre", "theye", "this", "those", "through", "to", "too",
                           "under", "until", "up", "very", "was", "wasnt", "we", "wed", "well",
                           "were", "wee", "werent", "what", "when", "where", "which", "while",
                           "who", "whom", "why", "with", "wont", "would", "wouldnt", "you",
                           "youd", "youll", "youre", "youve", "your", "yours", "yourself",
                           "yourselves"]
    def run(self):
        self.createVocab()
        self.train()
    def countWords(self, path, wordCount):
        with io.open(path, 'r', encoding='iso-8859-1') as f:
            lines = f.readlines()
            for line in lines:
                lettersOnly = re.sub("[^a-zA-Z0-9\s]", "", line).lower().split()
                for word in lettersOnly:
                    if word not in self.stop_words:
                        if word in wordCount:
                            wordCount[word] += 1
                        else:
                            wordCount[word] = 1
    def createVocab(self):
        hamWords = {}
        for each in os.listdir(self.trainHam):
            self.countWords(os.path.join(self.trainHam, each), hamWords)
        spamWords = {}
        for each in os.listdir(self.trainSpam):
            self.countWords(os.path.join(self.trainSpam, each), spamWords)
        self.vocabulary = set(hamWords.keys()) | set(spamWords.keys())
        self.weights = {word: 0.0 for word in self.vocabulary}
    def processFile(self, file, classification):
        wordCount = {}
        self.countWords(file, wordCount)
        self.fileData.append({'fileName': file, 'token': wordCount, 'class': classification})
    def train(self):
        for _ in range(500):
            self.updateError()
            self.updateWeights()
    def updateError(self):
        for eachFile in self.fileData:
            token = eachFile["token"]
            value = 1
            for everyToken in token:
                value += token[everyToken] * self.weights[everyToken]
            eachFile["error"] = self.sigmoid(value)
    def sigmoid(self, x):
        denom = 1 + np.exp(-x)
        return 1 / denom
    def updateWeights(self):
        for token in self.weights.keys():
            val = 0
            for eachFile in self.fileData:
                tokens = eachFile["token"]
                trueValue = eachFile["class"]
                if token in tokens:
                    temp = trueValue - eachFile["error"]
                    val += tokens[token] * temp
            self.weights[token] += ((val * self.rate) - (self.rate * self.lambdaVal * self.weights[token]))
    def test(self):
        hamFolder = os.listdir(self.testHam)
        hamCorrect = 0
        for each in hamFolder:
            hamDict = {}
            self.countWords(os.path.join(self.testHam, each), hamDict)
            value = sum(self.weights.get(token, 0) * count for token, count in hamDict.items())
            result = self.sigmoid(value)
            if result > 0.5:
                hamCorrect += 1
        hamAccuracy = (hamCorrect / len(hamFolder)) * 100
        print("Ham accuracy is ", hamAccuracy)
        spamFolder = os.listdir(self.testSpam)
        spamCorrect = 0
        for each in spamFolder:
            spamDict = {}
            self.countWords(os.path.join(self.testSpam, each), spamDict)
            value = sum(self.weights.get(token, 0) * count for token, count in spamDict.items())
            result = self.sigmoid(value)
            if result < 0.5:
                spamCorrect += 1
        spamAccuracy = (spamCorrect / len(spamFolder)) * 100
        print("Spam accuracy is ", spamAccuracy)
        totalAccuracy = ((spamCorrect + hamCorrect) / (len(hamFolder) + len(spamFolder))) * 100
        print("Total accuracy is ", totalAccuracy)
if __name__ == "__main__":
    trainHam_folder = "train/ham"
    trainSpam_folder = "train/spam"
    testHam_folder = "test/ham"
    testSpam_folder = "test/spam"
    model = LogisticRegression(trainHam_folder, trainSpam_folder, testHam_folder, testSpam_folder)
    model.run()
    model.test()
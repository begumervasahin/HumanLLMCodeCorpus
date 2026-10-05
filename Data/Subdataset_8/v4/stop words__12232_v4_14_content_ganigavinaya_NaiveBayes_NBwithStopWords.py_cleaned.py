import os
import re
import io
import math
class NaiveBayes:
    def __init__(self, trainingHam, trainingSpam, testHam, testSpam):
        self.trainingHam = trainingHam
        self.trainingSpam = trainingSpam
        self.HAM = 0
        self.SPAM = 1
        self.totalWordList = []
        self.hamCountDict = {}
        self.totalHamWordCount = 0
        self.spamCountDict = {}
        self.totalSpamWordCount = 0
        self.prior = {}
        self.totalCondProb = {}
        self.testHam = testHam
        self.testSpam = testSpam
        self.stop_words = ["a", "about", "above", "after", "again", "against", "all", "am",
                          "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before",
                          "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't",
                          "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few",
                          "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he",
                          "he'd", "he'll", "he", "her", "here", "here", "hers", "herself", "him", "himself", "his",
                          "how", "how's", "i", "i'd", "i'll", "i", "ie", "if", "in", "into", "is", "isn't", "it", "it",
                          "it's", "itself", "let", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not",
                          "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out",
                          "over", "own", "same", "shan't", "she", "she'd", "she'll", "she", "should", "shouldn't",
                          "so", "some", "such", "than", "that", "that", "the", "their", "theirs", "them", "themselves",
                          "then", "there", "there", "these", "they", "they'd", "they'll", "they're", "they've", "this",
                          "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd",
                          "we'll", "were", "we", "we're", "weren't", "what", "what", "when", "when", "where",
                          "where", "which", "while", "who", "who", "whom", "why", "why", "with", "won't", "would",
                          "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves",
                          "nt", "d", "ll", "re", "ve", "r", "t", "nd", "s"]
    def getWordCountList(self, flag):
        filepath = self.trainingHam if flag == self.HAM else self.trainingSpam
        trainingFileList = os.listdir(filepath)
        countDict = {}
        totalWordCount = 0
        for fileName in trainingFileList:
            with io.open(os.path.join(filepath, fileName), 'r', encoding='iso-8859-1') as file:
                lines = file.readlines()
                for line in lines:
                    lettersOnly = re.sub("[^a-zA-Z\s]", "", line).lower().split()
                    for word in lettersOnly:
                        if word not in self.stop_words:
                            countDict[word] = countDict.get(word, 0) + 1
                            totalWordCount += 1
        self.totalWordList = list(set(self.totalWordList + list(countDict.keys())))
        if flag == self.HAM:
            self.hamCountDict = countDict
            self.totalHamWordCount += totalWordCount
        else:
            self.spamCountDict = countDict
            self.totalSpamWordCount += totalWordCount
    def calculateCondProb(self):
        for word in self.totalWordList:
            hamCount = self.hamCountDict.get(word, 0) + 1
            spamCount = self.spamCountDict.get(word, 0) + 1
            self.totalCondProb[word] = [(hamCount / self.totalHamWordCount), (spamCount / self.totalSpamWordCount)]
    def run(self):
        self.getWordCountList(self.HAM)
        self.getWordCountList(self.SPAM)
    def train(self):
        totalHamFiles = len(os.listdir(self.trainingHam))
        totalSpamFiles = len(os.listdir(self.trainingSpam))
        totalTrainingFiles = totalHamFiles + totalSpamFiles
        self.prior[self.HAM] = totalHamFiles / totalTrainingFiles
        self.prior[self.SPAM] = totalSpamFiles / totalTrainingFiles
        self.calculateCondProb()
    def getClassification(self, path):
        correctCount = 0
        testFileList = os.listdir(path)
        for fileName in testFileList:
            with io.open(os.path.join(path, fileName), 'r', encoding='iso-8859-1') as file:
                fileData = file.read().lower()
                lettersOnly = re.sub("[^a-zA-Z\s]", "", fileData)
                wordList = set(lettersOnly.split())
                score = {self.HAM: math.log2(self.prior[self.HAM]), self.SPAM: math.log2(self.prior[self.SPAM])}
                for word in wordList:
                    if word in self.totalWordList:
                        score[self.HAM] += math.log2(self.totalCondProb[word][self.HAM])
                        score[self.SPAM] += math.log2(self.totalCondProb[word][self.SPAM])
                if score[self.HAM] > score[self.SPAM]:
                    if path == self.testHam:
                        correctCount += 1
                else:
                    if path == self.testSpam:
                        correctCount += 1
        return correctCount
    def test(self):
        hamTestResult = self.getClassification(self.testHam)
        hamTestFiles = len(os.listdir(self.testHam))
        hamAccuracy = (hamTestResult / hamTestFiles) * 100
        print("Ham test accuracy = {:.2f}%".format(hamAccuracy))
        spamTestResult = self.getClassification(self.testSpam)
        len(os.listdir(self.testSpam))
        spamAccuracy = (spamTestResult / spamTestFiles) * 100
        print("Spam test accuracy = {:.2f}%".format(spamAccuracy))
        totalTestFiles = hamTestFiles + spamTestFiles
        totalCorrect = hamTestResult + spamTestResult
        totalAccuracy = (totalCorrect / totalTestFiles) * 100
        print("Total test accuracy = {:.2f}%".format(totalAccuracy))
if __name__ == "__main__":
    nb = NaiveBayes("path_to_training_ham", "path_to_training_spam", "path_to_test_ham", "path_to_test_spam")
    nb.run()
    nb.train()
    nb.test()
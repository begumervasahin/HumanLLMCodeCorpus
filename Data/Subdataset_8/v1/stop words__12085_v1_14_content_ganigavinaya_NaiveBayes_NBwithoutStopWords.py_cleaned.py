import os
import re
import io
import math
class NaiveBayes:
    def __init__(self, trainingHam, trainingSpam, testHam, testSpam):
        self.trainingHam = trainingHam
        self.trainingSpam = trainingSpam
        self.testHam = testHam
        self.testSpam = testSpam
        self.HAM = 0
        self.SPAM = 1
        self.totalWordList = []
        self.hamCountDict = {}
        self.totalHamWordCount = 0
        self.spamCountDict = {}
        self.totalSpamWordCount = 0
        self.prior = {}
        self.totalCondProb = {}
    def getWordCountList(self, flag):
        filepath = self.trainingHam if flag == self.HAM else self.trainingSpam
        trainingFiles = os.listdir(filepath)
        countDict = {}
        totalWordCount = 0
        for filename in trainingFiles:
            with io.open(os.path.join(filepath, filename), 'r', encoding='iso-8859-1') as f:
                lines = f.readlines()
                for line in lines:
                    words = re.findall(r'\b\w+\b', line.lower())
                    for word in words:
                        countDict[word] = countDict.get(word, 0) + 1
                        totalWordCount += 1
        self.totalWordList.extend(countDict.keys())
        if flag == self.HAM:
            self.hamCountDict = countDict
            self.totalHamWordCount = totalWordCount
        else:
            self.spamCountDict = countDict
            self.totalSpamWordCount = totalWordCount
    def calculateCondProb(self):
        for word in self.totalWordList:
            hamCount = self.hamCountDict.get(word, 0) + 1
            spamCount = self.spamCountDict.get(word, 0) + 1
            self.totalCondProb[word] = [hamCount / (self.totalHamWordCount + len(self.totalWordList)),
                                         spamCount / (self.totalSpamWordCount + len(self.totalWordList))]
    def train(self):
        totalHamFiles = len(os.listdir(self.trainingHam))
        totalSpamFiles = len(os.listdir(self.trainingSpam))
        totalTrainingFiles = totalHamFiles + totalSpamFiles
        self.prior[self.HAM] = totalHamFiles / totalTrainingFiles
        self.prior[self.SPAM] = totalSpamFiles / totalTrainingFiles
        self.getWordCountList(self.HAM)
        self.getWordCountList(self.SPAM)
        self.calculateCondProb()
    def classify(self, path):
        correct = 0
        totalFiles = 0
        class_label = self.HAM if path == self.testHam else self.SPAM
        testFiles = os.listdir(path)
        for filename in testFiles:
            with io.open(os.path.join(path, filename), 'r', encoding='iso-8859-1') as f:
                file_content = f.read().lower()
                words = re.findall(r'\b\w+\b', file_content)
                score = {self.HAM: math.log(self.prior[self.HAM], 2),
                         self.SPAM: math.log(self.prior[self.SPAM], 2)}
                for word in words:
                    if word in self.totalWordList:
                        score[self.HAM] += math.log(self.totalCondProb[word][self.HAM], 2)
                        score[self.SPAM] += math.log(self.totalCondProb[word][self.SPAM], 2)
                predicted_label = max(score, key=score.get)
                if predicted_label == class_label:
                    correct += 1
                totalFiles += 1
        return correct, totalFiles
    def test(self):
        ham_correct, ham_total = self.classify(self.testHam)
        spam_correct, spam_total = self.classify(self.testSpam)
        ham_accuracy = (ham_correct / ham_total) * 100 if ham_total != 0 else 0
        spam_accuracy = (spam_correct / spam_total) * 100 if spam_total != 0 else 0
        total_accuracy = ((ham_correct + spam_correct) / (ham_total + spam_total)) * 100 if (ham_total + spam_total) != 0 else 0
        print("Ham test accuracy =", ham_accuracy)
        print("Spam test accuracy =", spam_accuracy)
        print("Total test accuracy =", total_accuracy)
if __name__ == "__main__":
    trainingHam = "path_to_training_ham_folder"
    trainingSpam = "path_to_training_spam_folder"
    testHam = "path_to_test_ham_folder"
    testSpam = "path_to_test_spam_folder"
    classifier = NaiveBayes(trainingHam, trainingSpam, testHam, testSpam)
    classifier.train()
    classifier.test()
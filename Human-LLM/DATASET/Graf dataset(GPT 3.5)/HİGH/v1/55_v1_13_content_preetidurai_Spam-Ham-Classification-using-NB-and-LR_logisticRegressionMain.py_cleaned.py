import LRHelper as helper
import Mail as m
import os
import math
import sys
class class1:
    b1 = {}
    b2 = {}
    b3 = set()
    a1 = 0
    b4 = {}
    def fonk1(self, learningConst, b5):
        self.b1 = {}
        self.b2 = {}
        self.b4 = {}
        self.b3 = set()
        self.a1 = float(learningConst)
        self.b5 = float(b5)
    def fonk2(self):
        for mailFileKey, mailFileValue in self.b1.items():
            for word in mailFileValue.thisMailWords:
                self.b3.add(word)
    def fonk3(self):
        for word in self.b3:
            self.b4[word] = 0.0
    def fonk4(self, iterationThreshold):
        for iter in range(int(iterationThreshold)):
            print("iter", iter)
            for weightWord in self.b4:
                a2 = 0.0
                a3 = 0
                for mail in self.b1.values():
                    if mail.b6 = = 1:
                        a3 = 1
                    if weightWord in mail.thisMailWords:
                        a2 += mail.thisMailWordFreqDict[weightWord] * (a3 - self.fonk5(1, mail))
                self.b4[weightWord] += ((self.a1 * a2) -
                                                   (self.a1 * self.b5 * self.b4[weightWord]))
    def fonk5(self, b7, mail):
        a2 = 0.0
        for key, value in mail.thisMailWordFreqDict.items():
            if key not in self.b4:
                self.b4[key] = 0.0
            a2 += self.b4[key] * value
        if b7 = = 1:
            return math.exp(a2) / (1 + math.exp(a2))
        elif b7 = = 0:
            return 1 / (1 + math.exp(a2))
    def fonk6(self, mail):
        b8 = {}
        b8[0] = self.fonk5(0, mail)
        b8[1] = self.fonk5(1, mail)
        if b8[0] > b8[1]:
            return 0
        else:
            return 1
    def fonk7(self):
        a4 = 0
        for mailValue in self.b2.values():
            b9 = self.fonk6(mailValue)
            if b9 = = mailValue.b6:
                a4 += 1
        b10 = (a4 / len(self.b2)) * 100
        print(b10)
    def fonk8(self, directoryPath, givenClass):
        b11 = os.listdir(directoryPath)
        for file in b11:
            b12 = os.path.join(directoryPath, file)
            with open(b12, b13 = 'utf-8', errors="ignore") as mailFile:
                b14 = helper.getWords(mailFile.read())
                b15 = helper.getWordFreq(b14)
                self.b2[file] = m.Mail(b14, b15, givenClass)
    def fonk9(self, directoryPath, givenClass, stopPath):
        b16 = helper.readStopWords(stopPath)
        b11 = os.listdir(directoryPath)
        for file in b11:
            b12 = os.path.join(directoryPath, file)
            with open(b12, b13 = 'utf-8', errors="ignore") as mailFile:
                b14 = helper.getWordsSansStopWords(mailFile.read(), b16)
                b15 = helper.getWordFreq(b14)
                self.b2[file] = m.Mail(b14, b15, givenClass)
    def fonk10(self, directoryPath, givenClass):
        b11 = os.listdir(directoryPath)
        for file in b11:
            b12 = os.path.join(directoryPath, file)
            with open(b12, b13 = 'utf-8', errors="ignore") as mailFile:
                b14 = helper.getWords(mailFile.read())
                b15 = helper.getWordFreq(b14)
                self.b1[file] = m.Mail(b14, b15, givenClass)
    def fonk11(self, directoryPath, givenClass, stopPath):
        b16 = helper.readStopWords(stopPath)
        b11 = os.listdir(directoryPath)
        for file in b11:
            b12 = os.path.join(directoryPath, file)
            with open(b12, b13 = 'utf-8', errors="ignore") as mailFile:
                b14 = helper.getWordsSansStopWords(mailFile.read(), b16)
                b15 = helper.getWordFreq(b14)
                self.b1[file] = m.Mail(b14, b15, givenClass)
def fonk12():
    if len(sys.argv) != 9:
        print("Usage: python script.py b18 b19 b20 b21 learningConst b5 iterationThreshold stopPath")
        return
    b17 = class1(sys.argv[5], sys.argv[6])
    b18 = sys.argv[1]
    b19 = sys.argv[2]
    b20 = sys.argv[3]
    b21 = sys.argv[4]
    b17.fonk10(b18, 0)
    b17.fonk10(b19, 1)
    b17.fonk8(b20, 0)
    b17.fonk8(b21, 1)
    b17.fonk2()
    b17.fonk3()
    b17.fonk4(sys.argv[7])
    print("Accuracy without removing stopwords:")
    b17.fonk7()
    b22 = class1(sys.argv[5], sys.argv[6])
    b22.fonk11(b18, 0, sys.argv[8])
    b22.fonk11(b19, 1, sys.argv[8])
    b22.fonk9(b20, 0, sys.argv[8])
    b22.fonk9(b21, 1, sys.argv[8])
    b22.fonk2()
    b22.fonk3()
    b22.fonk4(sys.argv[7])
    print("Accuracy after removing stopwords:")
    b22.fonk7()
if b23 = = "__main__":
    fonk12()
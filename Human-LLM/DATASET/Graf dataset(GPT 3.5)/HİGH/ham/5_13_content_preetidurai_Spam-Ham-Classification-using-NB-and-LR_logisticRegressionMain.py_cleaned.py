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
    def fonk1(self,learningConst,b5):
        self.b1 = {}
        self.b2 = {}
        self.b4 = {}
        self.b3 = set()
        self.a1 = float(learningConst)
        self.b5 = float(b5)
    def fonk2(self):
        for mailFileKey,mailFileValue in self.b1.items():
            for word in mailFileValue.thisMailWords:
                self.b3.add(word)
    def fonk3(self):
        for word in self.b3:
            self.b4[word]=0.0
    def fonk4(self,iterationThreshold):
        b6 = 0;
        a2 = 0
        a3 = 0
        for a3 in range(0,int(iterationThreshold)):
            print("a3",a3)
            for weightWord in self.b4:
                a4 = 0.0
                a2 = a2+1
                a5 = 0
                for mail in self.b1.values():
                    b6 = b6+1
                    if(mail.b7 = =1):
                        a5 = 1
                    if weightWord in mail.thisMailWords:
                        a4+=mail.thisMailWordFreqDict[weightWord]*(a5-self.fonk5(1,mail))
                self.b4[weightWord]+= ((self.a1*a4)) - ((self.a1)*(self.b5)*self.b4[weightWord])
    def fonk5(self,b8,mail):
        a4 = 0.0;
        a6 = 0.0
        for key,value in mail.thisMailWordFreqDict.items():
            if key not in self.b4:
                self.b4[key]=0.0
            a4+=self.b4[key]*value
        if(b8 = =1):
            a6 = (math.exp(a4)/(1+math.exp(a4)))
        elif(b8 = =0):
            a6 = (1/(1+math.exp(a4)))
        return(a6)
    def fonk6(self,mail):
        b9 = {}
        b9[0]=self.fonk5(0,mail)
        b9[1]=self.fonk5(1,mail)
        if(b9[0]>b9[1]):
            return(0)
        else:
            return(1)
    def fonk7(self,directoryPath,givenClass):
        b10 = []
        b11 = {}
        b12 = list(os.walk(directoryPath))[0][2]
        for file in b12:
            b13 = directoryPath+"/"+file
            with open(b13, b14 = 'utf-8',errors="ignore") as mailFile:
                b10 = helper.getWords(mailFile.read())
                b11 = helper.getWordFreq(b10)
                self.b2[file]=m.Mail(b10,b11,givenClass)
    def fonk8(self,directoryPath,givenClass,stopPath):
        b10 = []
        b11 = {}
        b10 = []
        b11 = {}
        b15 = helper.readStopWords(stopPath)
        b12 = list(os.walk(directoryPath))[0][2]
        for file in b12:
            b13 = directoryPath+"/"+file
            with open(b13, b14 = 'utf-8',errors="ignore") as mailFile:
                b10 = helper.getWordsSansStopWords(mailFile.read(),b15)
                b11 = helper.getWordFreq(b10)
                self.b2[file]=m.Mail(b10,b11,givenClass)
    def fonk9(self):
        a7 = 0
        a8 = 0
        a9 = 0
        for mailValue in self.b2.values():
            b16 = self.fonk6(mailValue)
            if(b16 = =mailValue.b7):
                a7+=1
                if(b16 = =1):
                    a9+=1
                else:
                    a8+=1
        b17 = ((a7)/len(self.b2))*100
        print(b17)
    def fonk10(self,directoryPath,givenClass):
        b10 = []
        b11 = {}
        b12 = list(os.walk(directoryPath))[0][2]
        for file in b12:
            b13 = directoryPath+"/"+file
            with open(b13, b14 = 'utf-8',errors="ignore") as mailFile:
                b10 = helper.getWords(mailFile.read())
                b11 = helper.getWordFreq(b10)
                self.b1[file]=m.Mail(b10,b11,givenClass)
    def fonk11(self,directoryPath,givenClass,stopPath):
        b10 = []
        b11 = {}
        b15 = helper.readStopWords(stopPath)
        b12 = list(os.walk(directoryPath))[0][2]
        for file in b12:
            b13 = directoryPath+"/"+file
            with open(b13, b14 = 'utf-8',errors="ignore") as mailFile:
                b10 = helper.getWordsSansStopWords(mailFile.read(),b15)
                b11 = helper.getWordFreq(b10)
                self.b1[file]=m.Mail(b10,b11,givenClass)
def fonk12():
        print(sys.argv)
        b18 = class1(sys.argv[5],sys.argv[6])
        b19 = sys.argv[1];
        b20 = sys.argv[2]
        b21 = sys.argv[3]
        b22 = sys.argv[4]
        b18.fonk10(b19,0)
        b18.fonk10(b20,1);
        b18.fonk7(b21,0)
        b18.fonk7(b22,1);
        b18.fonk2()
        b18.fonk3()
        b18.fonk4(sys.argv[7])
        print("Accuracy without removing stopwords")
        b18.fonk9()
        b23 = class1(sys.argv[5],sys.argv[6])
        b23.fonk11(b19,0,sys.argv[8])
        b23.fonk11(b20,1,sys.argv[8]);
        b23.fonk8(b21,0,sys.argv[8])
        b23.fonk8(b22,1,sys.argv[8]);
        b23.fonk2()
        b23.fonk3()
        b23.fonk4(sys.argv[7])
        print("Accuracy after removing stopwords")
        b23.fonk9()
fonk12()
from collections import Counter
from NBHelper import *
import math as m
import sys
class class1:
    a1 = 0
    b1 = {}
    b2 = {}
    b3 = {}
    b4 = {}
    b5 = []
    b6 = set()
    def fonk1(self,a1,classNames):
        self.a1 = a1
        for i in range(0,self.a1):
            self.b1[i]=classNames[i];
            self.b4[classNames[i]]={}
    def fonk2(self,pathArray):
        b7 = {}
        a2 = 0
        for key,value in self.b1.items():
            b8 = getMailDictionary(pathArray[key]);
            b7[value]=len(b8)
            a2+=len(b8)
            self.b2[value]=getVocabulary(b8);
        for key,value in b7.items():
            self.b3[key]=b7[key]/a2
    def fonk3(self,pathArray,stopWordPath):
        b7 = {}
        a2 = 0
        b9 = readStopWords(stopWordPath);
        for key,value in self.b1.items():
            b8 = getMailDictionaryWOStopWords(pathArray[key],b9);
            b7[value]=len(b8)
            a2+=len(b8)
            self.b2[value]=getVocabulary(b8);
        for key,value in b7.items():
            self.b3[key]=b7[key]/a2
    def fonk4(self):
        b5 = []
        for value in self.b2.values():
            b5.extend(value)
        self.b6 = set(b5);
    def fonk5(self):
        for value in self.b1.values():
            b10 = Counter(self.b2[value]);
            for term in self.b6:
                if term in b10.keys():
                    b11 = b10[term];
                    self.b4[value][term]=(1+b11)/(len(self.b6)+len(self.b2[value]))
                else:
                    self.b4[value][term]=(1)/(len(self.b6)+len(self.b2[value]));
    def fonk6(self,listOfWords):
        b12 = {}
        for val in self.b1.values():
            b12[val]=m.log(self.b3[val]);
        for term in listOfWords:
            for val in self.b1.values():
                if term in self.b4[val]:
                    b12[val]+=m.log(self.b4[val][term])
        b13 = list(b12.values())
        b14 = list(b12.keys())
        return b14[b13.index(max(b13))]
    def fonk7(self,b25):
        b15 = getMailDictionary(b25[0]);
        b16 = getMailDictionary(b25[1]);
        b17 = 0;
        b18 = 0;
        for key,value in b15.items():
            if(self.fonk6(value)==("spam")):
                b17 = b17+1
        for key,value in b16.items():
            if(self.fonk6(value)==("ham")):
                b18 = b18+1;
        b19 = (b17/(len(b15)))*100;
        b20 = (b18/(len(b16)))*100;
        b21 = ((b17+b18)/(len(b15)+len(b16)))*100
        print("Accuracy without removing stopwords",b21)
    def fonk8(self,b25,stopPath):
        b9 = readStopWords(stopPath);
        b15 = getMailDictionaryWOStopWords(b25[0],b9);
        b16 = getMailDictionaryWOStopWords(b25[1],b9);
        b17 = 0;
        b18 = 0;
        for key,value in b15.items():
            if(self.fonk6(value)==("spam")):
                b17 = b17+1
        for key,value in b16.items():
            if(self.fonk6(value)==("ham")):
                b18 = b18+1;
        b19 = (b17/(len(b15)))*100;
        b20 = (b18/(len(b16)))*100;
        b21 = ((b17+b18)/(len(b15)+len(b16)))*100
        print("Accuracy after removing stopwords",b21)
def fonk9():
    b22 = class1(2,["spam","ham"]);
    b23 = sys.argv
    b24 = []
    b25 = []
    b24.append(b23[1]);
    b24.append(b23[2]);
    b25.append(b23[3]);
    b25.append(b23[4]);
    b22.fonk2(b24);
    b22.fonk4();
    b22.fonk5();
    b22.fonk7(b25)
    b26 = class1(2,["spam","ham"]);
    b26.fonk3(b24,b23[5]);
    b26.fonk4();
    b26.fonk5();
    b26.fonk8(b25,b23[5])
fonk9()
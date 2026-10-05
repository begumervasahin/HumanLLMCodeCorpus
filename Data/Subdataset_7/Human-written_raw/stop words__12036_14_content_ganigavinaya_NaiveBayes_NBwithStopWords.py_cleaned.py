
import os
import re
import io
import math
class class1:
    def fonk1(self,b1,b2,b8,b9):
        self.b1 = b1
        self.b2 = b2
        self.a1 = 0
        self.a2 = 1
        self.b3 = []
        self.b4 = {}
        self.a3 = 0
        self.b5 = {}
        self.a4 = 0
        self.b6 = {}
        self.b7 = {}
        self.b8 = b8
        self.b9 = b9
        self.b10 = ["a","about","above","after","again","against","all","am",
                "an","and","any","are","arent","as","at","be","because","been","before",
                "being","below","between","both","but","by","cant","cannot","could","couldnt",
                "did","didnt","do","does","doesnt","doing","dont","down","during","each","few",
                "for","from","further","had","hadnt","has","hasnt","have","havent","having","he",
                "hed","hell","he","her","here","here","hers","herself","him","himself","his",
                "how","hows","i","id","ill","i","ie","if","in","into","is","isnt","it","it",
                "its","itself","let","me","more","most","mustnt","my","myself","no","nor","not",
                "of","off","on","once","only","or","other","ought","our","ours","ourselves","out",
                "over","own","same","shant","she","shed","shell","she","should","shouldnt",
                "so","some","such","than","that","that","the","their","theirs","them","themselves",
                "then","there","there","these","they","theyd","theyll","theyre","theye","this",
                "those","through","to","too","under","until","up","very","was","wasnt","we","wed",
                "well","were","wee","were","werent","what","what","when","when","where",
                "where","which","while","who","who","whom","why","why","with","wont","would",
                "wouldnt","you","youd","youll","youre","youve","your","yours","yourself","yourselves",
                "nt","d","ll","re","ve","r","t","nd","s"];
    def fonk2(self,b12):
        b11 = self.b1
        if(b12 = = self.a2):
            b11 = self.b2
        b13 = os.listdir(b11)
        b14 = {}
        a5 = 0
        for each in b13:
            b15 = io.open(b11+"/"+each, 'r',encoding='iso-8859-1')
            b16 = b15.readlines()
            for line in b16:
                b17 = (re.sub("[^a-zA-Z\s]", "", line)).lower().split()
                for word in b17:
                    if word not in self.b10:
                        if word in b14:
                            b14[word]+=1
                        else:
                            b14[word]=1
                        a5+=1
        b18 = list(b14.keys())
        a5+=len(b18)
        if(b12 = = self.a1):
            self.b4 = b14
            self.a3 = a5
        else:
            self.b5 = b14
            self.a4 = a5
    def fonk3(self):
        for each in self.b3:
            if(each in self.b4):
                b19 = self.b4[each]
            else:
                b19 = 0
            b19+=1
            if(each in self.b5):
                b20 = self.b5[each]
            else:
                b20 = 0
            b20+=1
            self.b7[each]=[(float)(b19/self.a3),(float)(b20/self.a4)]
    def fonk4(self):
        self.fonk2(self.a1)
        self.fonk2(self.a2)
        self.b3 = set(list(self.b4.keys())+list(self.b5.keys()))
    def fonk5(self):
        b21 = len(os.listdir(self.b1))
        b22 = len(os.listdir(self.b2))
        b23 = b21+ b22
        self.b6[self.a1] = b21/b23
        self.b6[self.a2] = b22/b23
        self.fonk3()
    def fonk6(self,b27):
        b24 = {self.a1:0,self.a2:0}
        a6 = 0
        b25 = os.listdir(b27)
        for each in b25:
            b15 = io.open(b27+"/"+each, 'r',encoding='iso-8859-1')
            b26 = b15.read()
            b17 = (re.sub("[^a-zA-Z\s]", "", b26)).lower()
            b18 = set(b17.split())
            for eachClass in b24.keys():
                b24[eachClass] = math.log(self.b6[eachClass],2)
                for word in b18:
                    if(word in self.b3):
                        b24[eachClass]+=math.log((self.b7[word])[eachClass],2)
            if(b24[self.a1]>b24[self.a2]):
                if(b27 = = self.b8):
                    a6+=1
            else:
                if(b27 = = self.b9):
                    a6+=1
        return a6
    def fonk7(self):
        b28 = self.fonk6(self.b8)
        b29 = os.listdir(self.b8)
        b30 = (float)(b28/len(b29))*100
        print("Ham test b30 = "+str(b30))
        b31 = os.listdir(self.b9)
        b32 = self.fonk6(self.b9)
        b30 = (float)(b32/len(b31))*100
        print("Spam test b30 = "+str(b30))
        b33 = (float)((b28+b32)/(len(b31)+len(b29)))*100
        print("Total test b30 = "+str(b33))
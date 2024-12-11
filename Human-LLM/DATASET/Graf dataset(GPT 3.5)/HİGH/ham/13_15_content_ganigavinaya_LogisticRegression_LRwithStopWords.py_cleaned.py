
import os
import io
import re
import numpy as np
class class1:
    def fonk1(self,b1,b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = {}
        self.b6 = []
        self.a1 = 0.0001
        self.a2 = 5
        self.b7 = []
        self.b8 = ["a","about","above","after","again","against","all","am",
                            "an","and","any","are","arent","as","at","be","because",
                            "been","before","being","below","between","both","but",
                            "by","cant","cannot","could","couldnt","did","didnt","do",
                            "does","doesnt","doing","dont","down","during","each","few",
                            "for","from","further","had","hadnt","has","hasnt","have",
                            "havent","having","he","hed","hell","he","her","here","here",
                            "hers","herself","him","himself","his","how","hows","i","id",
                            "ill","i","ie","if","in","into","is","isnt","it","it","its",
                            "itself","let","me","more","most","mustnt","my","myself","no",
                            "nor","not","of","off","on","once","only","or","other","ought",
                            "our","ours","ourselves","out","over","own","same","shant",
                            "she","shed","shell","she","should","shouldnt","so","some",
                            "such","than","that","that","the","their","theirs","them",
                            "themselves","then","there","there","these","they","theyd",
                            "theyll","theyre","theye","this","those","through","to","too",
                            "under","until","up","very","was","wasnt","we","wed","well",
                            "were","wee","werent","what","when","where","which","while",
                            "who","whom","why","with","wont","would","wouldnt","you",
                            "youd","youll","youre","youve","your","yours","yourself",
                            "yourselves"];
    def fonk2(self):
        self.fonk4()
        b9 = os.listdir(self.b1)
        for each in b9:
            self.fonk5(self.b1+"/"+each,1.0)
        b9 = os.listdir(self.b2)
        for each in b9:
            self.fonk5(self.b2+"/"+each,0.0)
    def fonk3(self,path,b15):
        b10 = io.open(path, 'r',encoding='iso-8859-1')
        b11 = b10.readlines()
        for line in b11:
            b12 = (re.sub("[^a-zA-Z0-9\s]", "", line)).lower().split()
            for word in b12:
                if word not in self.b8:
                    if word in b15:
                        b15[word]+=1
                    else:
                        b15[word]=1
        b10.close()
    def fonk4(self):
        b13 = {}
        b9 = os.listdir(self.b1)
        for each in b9:
            self.fonk3(self.b1+"/"+each,b13)
        b14 = {}
        b9 = os.listdir(self.b2)
        for each in b9:
            self.fonk3(self.b2+"/"+each,b14)
        self.b6 = set(list(b13.keys())+list(b14.keys()))
        for each in self.b6:
            self.b5[each] = 0.0
    def fonk5(self,file,classification):
        b15 = {}
        self.fonk3(file,b15)
        self.b7.append({'fileName':file,'b16':b15,'class':classification})
    def fonk6(self):
        for i in range(0,500):
            self.fonk7()
            self.fonk9()
    def fonk7(self):
        a3 = 0
        for eachFile in self.b7:
            b16 = eachFile["b16"]
            a4 = 1
            for everyToken in b16:
                a4 += b16[everyToken]*self.b5[everyToken]
            eachFile["a3"] = self.fonk8(a4)
            a3+= eachFile["a3"]
    def fonk8(self,x):
        b17 = 1+np.exp(-x)
        return (1/b17)
    def fonk9(self):
        for b16 in self.b5.keys():
            a5 = 0
            a3 = 0
            for eachFile in self.b7:
                b18 = eachFile["b16"]
                b19 = eachFile["class"]
                if b16 in b18:
                    b20 = b19-eachFile["a3"]
                    a3 += b20
                    a5 +=b18[b16]*(b20)
            self.b5[b16]+= ((a5*self.a1)-(self.a1*self.a2*self.b5[b16]))
    def fonk10(self):
        b21 = os.listdir(self.b3)
        a6 = 0
        for each in b21:
            b22 = {}
            a4 = 0
            self.fonk3(self.b3+"/"+each,b22)
            for b16 in b22:
                if b16 in self.b5:
                    a4+=self.b5[b16]*b22[b16]
            b23 = self.fonk8(a4)
            if b23 > 0.5:
                a6 += 1
        b24 = (float)(a6/len(b21))*100
        print("Ham b24 is ",b24)
        b25 = os.listdir(self.b4)
        a7 = 0
        for each in b25:
            b26 = {}
            a4 = 0
            self.fonk3(self.b4+"/"+each,b26)
            for b16 in b26:
                if b16 in self.b5:
                    a4+=self.b5[b16]*b26[b16]
            b23 = self.fonk8(a4)
            if b23 < 0.5:
                a7 += 1
        b24 = (float)(a7/len(b25))*100
        print("Spam b24 is ",b24)
        b27 = (float)((a7+a6)/(len(b21)+len(b25)))*100
        print("Total b24 is ",b27)
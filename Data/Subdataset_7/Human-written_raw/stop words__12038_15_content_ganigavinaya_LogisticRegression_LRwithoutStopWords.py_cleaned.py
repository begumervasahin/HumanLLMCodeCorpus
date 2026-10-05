
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
    def fonk2(self):
        self.fonk4()
        b8 = os.listdir(self.b1)
        for each in b8:
            self.fonk5(self.b1+"/"+each,1.0)
        b8 = os.listdir(self.b2)
        for each in b8:
            self.fonk5(self.b2+"/"+each,0.0)
    def fonk3(self,path,b14):
        b9 = io.open(path, 'r',encoding='iso-8859-1')
        b10 = b9.readlines()
        for line in b10:
            b11 = (re.sub("[^a-zA-Z0-9\s]", "", line)).lower().split()
            for word in b11:
                if word in b14:
                    b14[word]+=1
                else:
                    b14[word]=1
        b9.close()
    def fonk4(self):
        b12 = {}
        b8 = os.listdir(self.b1)
        for each in b8:
            self.fonk3(self.b1+"/"+each,b12)
        b13 = {}
        b8 = os.listdir(self.b2)
        for each in b8:
            self.fonk3(self.b2+"/"+each,b13)
        self.b6 = set(list(b12.keys())+list(b13.keys()))
        for each in self.b6:
            self.b5[each] = 0.0
    def fonk5(self,file,classification):
        b14 = {}
        self.fonk3(file,b14)
        self.b7.append({'fileName':file,'b15':b14,'class':classification})
    def fonk6(self):
        for i in range(0,500):
            self.fonk7()
            self.fonk9()
    def fonk7(self):
        a3 = 0
        for eachFile in self.b7:
            b15 = eachFile["b15"]
            a4 = 1
            for everyToken in b15:
                a4 += b15[everyToken]*self.b5[everyToken]
            eachFile["a3"] = self.fonk8(a4)
            a3+= eachFile["a3"]
    def fonk8(self,x):
        b16 = 1+np.exp(-x)
        return (1/b16)
    def fonk9(self):
        for b15 in self.b5.keys():
            a5 = 0
            a3 = 0
            for eachFile in self.b7:
                b17 = eachFile["b15"]
                b18 = eachFile["class"]
                if b15 in b17:
                    b19 = b18-eachFile["a3"]
                    a3 += b19
                    a5 +=b17[b15]*(b19)
            self.b5[b15]+= ((a5*self.a1)-(self.a1*self.a2*self.b5[b15]))
    def fonk10(self):
        b20 = os.listdir(self.b3)
        a6 = 0
        for each in b20:
            b21 = {}
            a4 = 0
            self.fonk3(self.b3+"/"+each,b21)
            for b15 in b21:
                if b15 in self.b5:
                    a4+=self.b5[b15]*b21[b15]
            b22 = self.fonk8(a4)
            if b22 > 0.5:
                a6 += 1
        b23 = (float)(a6/len(b20))*100
        print("Ham b23 is ",b23)
        b24 = os.listdir(self.b4)
        a7 = 0
        for each in b24:
            b25 = {}
            a4 = 0
            self.fonk3(self.b4+"/"+each,b25)
            for b15 in b25:
                if b15 in self.b5:
                    a4+=self.b5[b15]*b25[b15]
            b22 = self.fonk8(a4)
            if b22 < 0.5:
                a7 += 1
        b23 = (float)(a7/len(b24))*100
        print("Spam b23 is ",b23)
        b26 = (float)((a7+a6)/(len(b20)+len(b24)))*100
        print("Total b23 is ",b26)
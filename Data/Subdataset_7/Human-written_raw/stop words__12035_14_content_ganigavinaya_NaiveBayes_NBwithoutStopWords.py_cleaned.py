
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
    def fonk2(self,b11):
        b10 = self.b1
        if(b11 = = self.a2):
            b10 = self.b2
        b12 = os.listdir(b10)
        b13 = {}
        a5 = 0
        for each in b12:
            b14 = io.open(b10+"/"+each, 'r',encoding='iso-8859-1')
            b15 = b14.readlines()
            for line in b15:
                b16 = (re.sub("[^a-zA-Z\s]", "", line)).lower().split()
                for word in b16:
                    if word in b13:
                        b13[word]+=1
                    else:
                        b13[word]=1
                    a5+=1
        b17 = list(b13.keys())
        a5+=len(b17)
        if(b11 = = self.a1):
            self.b4 = b13
            self.a3 = a5
        else:
            self.b5 = b13
            self.a4 = a5
    def fonk3(self):
        for each in self.b3:
            if(each in self.b4):
                b18 = self.b4[each]
            else:
                b18 = 0
            b18+=1
            if(each in self.b5):
                b19 = self.b5[each]
            else:
                b19 = 0
            b19+=1
            self.b7[each]=[(float)(b18/self.a3),(float)(b19/self.a4)]
    def fonk4(self):
        self.fonk2(self.a1)
        self.fonk2(self.a2)
        self.b3 = set(list(self.b4.keys())+list(self.b5.keys()))
    def fonk5(self):
        b20 = len(os.listdir(self.b1))
        b21 = len(os.listdir(self.b2))
        b22 = b20+ b21
        self.b6[self.a1] = b20/b22
        self.b6[self.a2] = b21/b22
        self.fonk3()
    def fonk6(self,b26):
        b23 = {self.a1:0,self.a2:0}
        a6 = 0
        b24 = os.listdir(b26)
        for each in b24:
            b14 = io.open(b26+"/"+each, 'r',encoding='iso-8859-1')
            b25 = b14.read()
            b16 = (re.sub("[^a-zA-Z\s]", "", b25)).lower()
            b17 = set(b16.split())
            for eachClass in b23.keys():
                b23[eachClass] = math.log(self.b6[eachClass],2)
                for word in b17:
                    if(word in self.b3):
                        b23[eachClass]+=math.log((self.b7[word])[eachClass],2)
            if(b23[self.a1]>b23[self.a2]):
                if(b26 = = self.b8):
                    a6+=1
            else:
                if(b26 = = self.b9):
                    a6+=1
        return a6
    def fonk7(self):
        b27 = self.fonk6(self.b8)
        b28 = os.listdir(self.b8)
        b29 = (float)(b27/len(b28))*100
        print("Ham test b29 = "+str(b29))
        b30 = os.listdir(self.b9)
        b31 = self.fonk6(self.b9)
        b29 = (float)(b31/len(b30))*100
        print("Spam test b29 = "+str(b29))
        b32 = (float)((b27+b31)/(len(b30)+len(b28)))*100
        print("Total test b29 = "+str(b32))
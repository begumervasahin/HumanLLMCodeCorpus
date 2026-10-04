import time
import math
import random
def fonk1(I, J, b1 = 0.0):
    b2 = []
    for i in range(I):
        b2.append([b1]*J)
    return b2
class class1:
    def fonk2(self, ni, nh, no,lr):
        self.b3 = int(ni)
        self.b4 = int(nh)
        self.b5 = int(no)
        self.b6 = float(lr)
        self.b7 = [1.0]*self.b3
        self.b8 = [1.0]*self.b4
        self.b9 = [1.0]*self.b5
        self.b10 = fonk1(self.b3, self.b4)
        self.b11 = fonk1(self.b4, self.b5)
        self.a1 = 1.0
        for i in range(self.b3):
            for j in range(self.b4):
                self.b10[i][j] = random.uniform(0, 1)
        for j in range(self.b4):
            for k in range(self.b5):
                self.b11[j][k] = random.uniform(0, 1)
    def fonk3(self, b22):
        for i in range(0,self.b3):
            self.b7[i] = float(b22[i])/float(255)
        for j in range(0,self.b4):
            a2 = 0.0
            for i in range(0,self.b3):
                a2 +=( self.b7[i] * self.b10[i][j] )
            a2+=self.a1
            self.b8[j] =a2
        b12 = max(self.b8,b34=float)
        b13 = min(self.b8,b34=float)
        for i in range(0,self.b4):
            self.b8[i]=(self.b8[i]-b13)/(b12-b13)
            self.b8[i]=1/(1+math.exp(-self.b8[i]))
        for k in range(0,self.b5):
            a2 = 0.0
            for j in range(0,self.b4):
                a2 +=( self.b8[j] * self.b11[j][k] )
            self.b9[k] = a2 +self.a1
        b12 = max(self.b8,b34=float)
        b13 = min(self.b8,b34=float)
        for i in range(0,self.b5):
            self.b9[i]=(self.b9[i]-b13)/(b12-b13)
            self.b9[i]=1/(1+math.exp(-self.b9[i]))
        b12 = max(self.b9,b34=float)
        return self.b9.index(b12)*90
    def fonk4(self, b21,b6):
        b14 = [0.0] * self.b5
        for k in range(self.b5):
            b15 = b21[k] - self.b9[k]
            b14[k] =  b15 * self.b9[k]*(1-self.b9[k])
        for j in range(self.b4):
            for k in range(self.b5):
                b16 = b14[k] * self.b8[j]
                self.b11[j][k] += b6*b16
        b17 = [0.0] * self.b4
        for j in range(self.b4):
            b15 = 0.0
            for k in range(self.b5):
                b15 += b14[k] * self.b11[j][k]
            b17[j] = b15 * self.b8[j]*(1-self.b8[j])
        for i in range (self.b3):
            for j in range (self.b4):
                b16 = b17[j] * self.b7[i]
                self.b10[i][j] += b6*b16
    def fonk5(self, patterns,b19):
        b12 = self.fonk3(patterns)
        if b12 = =b19:
            return b19
        else:
            return -1
    def fonk6(self,train_data):
        for i in range(0,len(train_data)/2):
            b18 = map(int,train_data[i][2:])
            b19 = int(train_data[i][1])
            b20 = [b18,[b19]]
            b21 = [0]*4
            b22 = b20[0]
            b21[b19/90] = 1
            self.fonk3(b22)
            self.fonk4(b21, self.b6)
    def fonk7(self,test_data):
        a3 = 0
        b23 = [[0 for x in range(4)] for x in range(4)]
        b24 = open("nnet_output.txt", 'w');
        for i in range(0,len(test_data)):
            b18 = map(int,test_data[i][2:])
            b19 = int(test_data[i][1])
            b20 = [b18,[b19]]
            b22 = b20[0]
            b12 = self.fonk5(b22,b19)
            b23[b19/90][b12/90]+=1
            b25 = test_data[i][0]+" "+test_data[i][1]+"\n"
            b24.write(b25)
            if b12 = =b19:
                a3+=1
        print "Percentage of Efficiency",float(a3)/float(len(test_data))*100
        print "Confusion b23"
        for i in range(0,4):
            print b23[i]
    def fonk8(self,train_data,test_data,k):
            b26 = [float(100000000000000000) for x in range(0,int(k))]
            b27 = [None]*int(k)
            b28 = list(test_data[2:])
            for j in range(0,len(train_data)/20):
                a4 = 0
                b29 = list(train_data[j][2:])
                for k in range(0,192):
                    a4+=abs(float(b28[k])-float(b29[k]))
                b12 = max(b26,b34=float)
                if a4 < b12 :
                    b30 = b26.index(b12)
                    b26[b30]=float(a4)
                    b27[b30]=j
            b31 = list()
            for kindl in range(0,len(b27)):
                b31.append(train_data[b27[kindl]][1])
            b32 = ['0','90','180','270']
            b33 = {}
            for word in b31:
                if word in b33:
                    b33[word] += 1
                else:
                    b33[word] = 1
            return max(b33, b34 = b33.get )
    def fonk9(self,train_data,test_data,k):
        a3 = 0
        b23 = [[0 for x in range(4)] for x in range(4)]
        b24 = open("knn_output.txt", 'w');
        for i in range(0,len(test_data)):
            b12 = list(test_data[i])
            b25 = self.fonk8(train_data,b12,k)
            if b25 = = b12[1]:
                a3+=1
            b23[int(b12[1])/90][int(b25)/90]+=1
            b25 = b12[0]+" "+b25+"\n"
            b24.write(b25)
        b35 = float(a3)/float(len(test_data))
        print "Percentage of Efficiency",b35*float(100)
        print "Confusion b23"
        for i in range(0,4):
            print b23[i]
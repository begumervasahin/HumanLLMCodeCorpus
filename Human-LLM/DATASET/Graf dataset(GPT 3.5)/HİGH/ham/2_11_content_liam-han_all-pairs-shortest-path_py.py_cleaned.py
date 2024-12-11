import sys
import re
import time
import math
b1 = re.compile("(\\d+)\\s(\\d+)")
b2 = re.compile("(\\d+)\\s(\\d+)\\s(-?\\d+)")
b3 = []
b4 = []
class class1:
    a1 = 0
    a2 = 0
    a3 = 0.0
    def fonk1(self,a1,a2,a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
    def fonk2(self):
        return "((%s,%s),%s)"%(self.a1,self.a2,self.a3)
def fonk3(graph):
        b5 = [[0 for i in range(len(b3 + 1))] for j in range(len(b3 + 1))]
        for i in range(b3):
            for j in range(b3):
                b5[i][j] = graph[i][j]
        ''' Add all b3 one
            by one to the set of
            intermediate b3.
        ---> Before b22 of a iteration,
             we have shortest
            distances between all pairs
            of b3 such
            that the shortest distances
            consider only the
            b3 in set {0, 1, 2, .. k-1}
            as intermediate b3.
        ----> After the b23 of a iteration,
              vertex no. k is
            added to the set of
            intermediate b3 and
            the set becomes {0, 1, 2, .. k} '''
        for k in range(len(b3)):
            for i in range(len(b3)):
                for j in range(len(b3)):
                    if (b5[i][k] + b5[k][j] < b5[i][j]):
                        b5[i][j] = b5[i][k] + b5[k][j]
        for i in range(len(b3)):
            if (b5[i][i] < 0):
                return True
        return False
def fonk4(b21):
    b6 = []
    b7 = []
    for i in range(len(b3)):
        for j in range(len(b3)):
            if not math.isinf(float(b21[1][i][j])):
                b8 = class1(int(i), int(j), float(b21[1][i][j]))
                b7.append(b8)
    print (len(b7))
    print (len(b3))
    for k in range(len(b3)):
        b5 = []
        for b9 in range(len(b3)):
            b5.append(float("inf"))
            if b9 = = k:
                b5[b9] = 0
        for i in range(len(b3)-1):
            for j in range(len(b7)):
                if b5[b7[j].a2] > b5[b7[j].a1] + b7[j].a3:
                    b5[b7[j].a2] = b5[b7[j].a1] + b7[j].a3
        for i in range(len(b7)):
            if b5[b7[i].a2] > b5[b7[i].a1] + b7[i].a3:
                print ("There is negative circle")
                return 0
        for i in range(len(b21[0])):
            b8 = class1(k,i,b5[i])
            b6.append(b8)
    return b6
def fonk5(b21):
    b6 = []
    b5 = []
    for i in range(len(b21[0])):
        b10 = []
        for j in range(len(b21[0])):
            b10.append(float(b4[i][j]))
        b5.append(b10)
        b5[i][i] = 0
    for k in range(len(b21[0])):
        for i in range(len(b21[0])):
            for j in range(len(b21[0])):
                if(b5[i][j] > b5[i][k]+b5[k][j]):
                    b5[i][j] = b5[i][k] + b5[k][j]
    for i in range(len(b21[0])):
        for j in range(len(b21[0])):
            b8 = class1(i,j,b5[i][j]);
            b6.append(b8)
    return b6
def fonk6(filename):
    global b3
    global b4
    b11 = open(filename,'r')
    b12 = b11.readline()
    b13 = b1.match(b12)
    if not b13:
        print(b12+" not properly formatted")
        quit(1)
    b3 = list(range(int(b13.group(1))))
    b4 = []
    for i in range(len(b3)):
        b14 = []
        for j in range(len(b3)):
            b14.append(float("inf"))
        b4.append(b14)
    for b15 in b11.readlines():
        b15 = b15.strip()
        b16 = b2.match(b15)
        if b16:
            b17 = b16.group(1)
            b18 = b16.group(2)
            if int(b17) > len(b3) or int(b18) > len(b3):
                print("Attempting to insert an edge between "+b17+" and "+b18+" in a graph with "+b3+" b3")
                quit(1)
            b19 = b16.group(3)
            b4[int(b17)-1][int(b18)-1]=b19
    return (b3,b4)
def fonk7(filename,b20):
    b20 = b20[1:]
    b21 = fonk6(filename)
    if b20 = = 'b' or b20 == 'B':
        fonk4(b21)
    if b20 = = 'f' or b20 == 'F':
        fonk5(b21)
    if b20 = = "both":
        b22 = time.clock()
        print (fonk4(b21))
        fonk4(b21)
        b23 = time.clock()
        b24 = b23-b22
        fonk5(b21)
        b22 = time.clock()
        b23 = time.clock()
        b25 = b23-b22
        print("Bellman-Ford timing: "+str(b24))
        print("Floyd-Warshall timing: "+str(b25))
if b26 = = '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    fonk7(sys.argv[2],sys.argv[1])
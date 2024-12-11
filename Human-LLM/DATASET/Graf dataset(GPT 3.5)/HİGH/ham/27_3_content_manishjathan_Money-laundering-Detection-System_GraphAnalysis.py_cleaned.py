3. Repository: manishjathan/Money-laundering-Detection-System
   File: GraphAnalysis.py
   URL: https:
   Code Content:
from collections import defaultdict
import GraphGeneration as gg
import FrequentTransactions as ft
import DisconnectedGraphs as dg
import pymongo
class class1:
    def fonk1(self, b31):
        self.b1 = defaultdict(list)
        self.b2 = b31
    def fonk2(self, u, v):
        self.b1[u].append(v)
    def fonk3(self, v, b3, b4):
        b3[v] = True
        for i in self.b1[v]:
            if b3[i] == False:
                self.fonk3(i, b3, b4)
        b4.insert(0, v)
    def fonk4(self):
        print("Topological Sort")
        b3 = [False] * self.b2
        b4 = []
        for i in range(self.b2):
            if b3[i] == False:
                self.fonk3(i, b3, b4)
        print(b4)
        return b4
def fonk5(b30):
    b5 = class1(len(b30))
    for edges in b30:
        b5.fonk2(edges[0],edges[1])
    print(b5.b1)
    return b5
def fonk6(b5):
    print("Mapping Nodes")
    b6 = {}
    a1 = 0
    for k,v in b5.b1.items():
        b6[k] = a1
        a1 += 1
    print(b6)
    return b6
def fonk7(b5):
    print("Assigning Edge Weights  ")
    b7 = []
    for k,v in  b5.b1.items():
        if v != []:
            b8 = {}
            for b31 in v:
                b8[b31] = 1
            try:
                b7.append(b8)
            except:
                b7 = [b8]
    print(b7)
    return b7
def fonk8(nodeValues,b6,b5):
    b9 = {}
    b7 = fonk7(b5)
    print(b7)
    print("Longest Distance Function : ")
    for node in nodeValues.keys():
        try:
            print(node,b7[b6[node]].keys())
            for key in b7[b6[node]].keys():
                b10 = nodeValues[node]
                b11 = b7[b6[node]][key]
                b12 = b10 + b11
                if nodeValues[key] < b12:
                    nodeValues[key] = b12
                    try:
                        b9[key].append(node,key)
                    except:
                        b9[key] = [node,key]
        except:
            print("Exception!!!")
    print(nodeValues)
    print(b9)
    return b9
def fonk9(b9,destNode,sourceNode):
    b13 = [b9[destNode]]
    b14 = b9[destNode][0]
    while b14 != sourceNode:
        b13.append(b9[b14])
        b14 = b9[b14][0]
    print(b13)
    return b13
def fonk10(b13):
    b15 = []
    b16 = pymongo.MongoClient()
    b17 = b16.MoneyLaundering
    b18 = b17.b18
    print("Transactions involved in longest Path : \n")
    for path in b13:
        b19 = {}
        b20 = b18.find({'tupleId' : path[0]}, {'b24': 1,'_id': 0})
        b21 = b18.find({'tupleId' : path[1]}, {'b24': 1,'_id': 0})
        b19["nameOrig"] = b20[0]['b24']
        b19["nameDest"] = b21[0]['b24']
        b22 = b17.bankingTransactions.find({'nameOrig' : b20[0]['b24'],'nameDest' : b21[0]['b24']})
        for info in b22:
            for k,v in info.items():
                b19[k] = v
        try:
            b15.append(b19)
        except:
            b15 = [b19]
    return b15
def fonk11(node):
    b16 = pymongo.MongoClient()
    b17 = b16.MoneyLaundering
    b23 = b17.b18.find({'tupleId' : node},{'b24':1,'_id':0})
    b24 = None
    for info in b23:
        for k,v in info.items():
            print(v)
            b24 = v
    return b24
def fonk12():
    print("Tuple List")
    b25 = ft.mapCustomers()
    print("Total Number of Transactions : ", len(b25))
    print("Actual Frequency of Transactions : ")
    b26 = ft.b29(b25)
    print("Hash Based Bucket Count : ")
    b27 = ft.hashBasedBucketCount(b25)
    print("Filtered transactions(On Basis of Bucket Count) : ")
    b28 = ft.filterOnBucketCount(b25, b27, 50)
    print("Filtered Transactions(On Basis of actual Frequency) : ")
    b29 = ft.filterOnActualCount(b28, b26, 0)
    print(b29)
    b30 = [(1,2),(1,3),(2,3),(2,4),(3,4),(3,5),(3,6),(4,5),(4,6),(5,6),(7,8),(8,9),(8,10),(9,10),(11,12),(11,13),(12,14),(13,14)]
    print("Edge List")
    print(b30)
    b5 = fonk5(b30)
    b1 = gg.generateGraph(b30)
    b31 = gg.getVertices(b30)
    b32 = gg.getIndegree(b31,b1)
    b33 = gg.getOutDegree(b31,b1)
    b34 = dg.getSourceNodes(b32)
    b35 = dg.splitEdgeList(b30,b1,b34)
    print("Vertex Set after splitting")
    b36 = []
    a1 = 0
    for b30 in b35:
        try:
            b36.append(dg.depthFirstSearch(b30,b1,b34[a1]))
        except:
            b36 = [dg.depthFirstSearch(b30,b1,b34[a1])]
        a1 += 1
    print("New Node Values after splitting")
    b37 = []
    a1 = 0
    for b31 in b36:
        try:
            b37.append(gg.genNodeValues(b31,b34[a1]))
        except:
            b37 = [gg.genNodeValues(b31,b34[a1])]
        a1 += 1
    a1 = 0
    for b30 in b35:
        print("Edge List")
        print(b30)
        fonk10(b30)
        b5 = fonk5(b30)
        b5.fonk4()
        b6 = fonk6(b5)
        fonk8(b37[a1],b6,b5)
        a1 += 1
    print("Longest Path for b21 = %d and source = %d" %(10,7))
    b13 = fonk9({8: [7, 8], 9: [8, 9], 10: [9, 10]},10,7)
    fonk10(b13)
    print("Longest Path for b21 = %d and source = %d" % (6, 1))
    b13 = fonk9({2: [1, 2], 3: [2, 3], 4: [3, 4], 5: [4, 5], 6: [5, 6]}, 6, 1)
    fonk10(b13)
   README Content:
This project is built to identify money laundering cases in the layering stage. Basically there are two major techniques that have been applied to do this.First is identification of frequent transactions using Hash based Apriori Algorithm. Frequent transactions are identified by means of threshold values. Second is forming a connection between the involved customers and finding the amount of money laundered.
* run class1 Analysis UI.py
* run Transaction Analysis UI.py
* Download and install Python(v>3).
* Download and install MongoDB and RoboMongo.
* Book1.xlsx contains all the banking transactions.
* Enter the number of records(in UI) you want to work on.(Those many number of record are inserted into MongoDB database)
![Money Laundering System UI](MoneyLaunderingSystemUI.png)
![Graph1](Pdf1.png)
![Graph2](Pdf2.png)

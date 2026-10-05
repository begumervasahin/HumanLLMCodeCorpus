from collections import defaultdict
import pymongo
import GraphGeneration as gg
import FrequentTransactions as ft
import DisconnectedGraphs as dg
class class1:
    def fonk1(self, b31):
        self.b1 = defaultdict(list)
        self.b2 = b31
    def fonk2(self, u, v):
        self.b1[u].append(v)
    def fonk3(self, v, b3, b4):
        b3[v] = True
        for i in self.b1[v]:
            if not b3[i]:
                self.fonk3(i, b3, b4)
        b4.insert(0, v)
    def fonk4(self):
        b3 = [False] * self.b2
        b4 = []
        for i in range(self.b2):
            if not b3[i]:
                self.fonk3(i, b3, b4)
        print("Topological Sort:")
        print(b4)
        return b4
def fonk5(b30):
    b5 = class1(len(b30))
    for edge in b30:
        b5.fonk2(edge[0], edge[1])
    print("class1 Structure:")
    print(b5.b1)
    return b5
def fonk6(b1):
    print("Mapping Nodes:")
    b6 = {}
    a1 = 0
    for k, v in b1.b1.items():
        b6[k] = a1
        a1 += 1
    print(b6)
    return b6
def fonk7(b1):
    print("Assigning Edge Weights:")
    b7 = []
    for k, v in b1.b1.items():
        if v:
            b8 = {vertex: 1 for vertex in v}
            b7.append(b8)
    print(b7)
    return b7
def fonk8(node_values, b6, b1):
    b9 = {}
    b7 = fonk7(b1)
    print("Longest Distance Calculation:")
    for node in node_values.keys():
        try:
            for key in b7[b6[node]].keys():
                b10 = node_values[node]
                b11 = b7[b6[node]][key]
                b12 = b10 + b11
                if node_values[key] < b12:
                    node_values[key] = b12
                    try:
                        b9[key].append((node, key))
                    except KeyError:
                        b9[key] = [(node, key)]
        except:
            print("Exception occurred!")
    print("Node Values:")
    print(node_values)
    print("Longest Path Edges:")
    print(b9)
    return b9
def fonk9(b9, dest_node, source_node):
    b13 = [b9[dest_node]]
    b14 = b9[dest_node][0]
    while b14 != source_node:
        b13.append(b9[b14])
        b14 = b9[b14][0]
    print("Longest Path from {} to {}:".format(source_node, dest_node))
    print(b13)
    return b13
def fonk10(b13):
    b15 = []
    b16 = pymongo.MongoClient()
    b17 = b16.MoneyLaundering
    b18 = b17.mappedTransactions
    print("Transactions involved in the Longest Path:\n")
    for path in b13:
        b19 = {}
        b20 = b18.find({'tupleId': path[0]}, {'customerId': 1, '_id': 0})
        b21 = b18.find({'tupleId': path[1]}, {'customerId': 1, '_id': 0})
        b19["nameOrig"] = b20[0]['customerId']
        b19["nameDest"] = b21[0]['customerId']
        b22 = b17.bankingTransactions.find({'nameOrig': b20[0]['customerId'], 'nameDest': b21[0]['customerId']})
        for info in b22:
            for k, v in info.items():
                b19[k] = v
        try:
            b15.append(b19)
        except:
            b15 = [b19]
    return b15
def fonk11(node):
    b16 = pymongo.MongoClient()
    b17 = b16.MoneyLaundering
    b23 = b17.mappedTransactions.find({'tupleId': node}, {'customerId': 1, '_id': 0})
    b24 = None
    for info in b23:
        for k, v in info.items():
            print(v)
            b24 = v
    return b24
def fonk12():
    print("Fetching Tuple List:")
    b25 = ft.mapCustomers()
    print("Total Number of Transactions:", len(b25))
    print("Calculating Actual Frequency of Transactions:")
    b26 = ft.actualCount(b25)
    print("Calculating Hash Based Bucket Count:")
    b27 = ft.hashBasedBucketCount(b25)
    print("Filtering Transactions (On Basis of Bucket Count):")
    b28 = ft.filterOnBucketCount(b25, b27, 50)
    print("Filtering Transactions (On Basis of Actual Frequency):")
    b29 = ft.filterOnActualCount(b28, b26, 0)
    print(b29)
    b30 = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6), (7, 8), (8, 9), (8, 10),
                 (9, 10), (11, 12), (11, 13), (12, 14), (13, 14)]
    print("Edge List:")
    print(b30)
    b1 = fonk5(b30)
    b31 = gg.getVertices(b30)
    b32 = gg.getIndegree(b31, b1)
    b33 = gg.getOutDegree(b31, b1)
    b34 = dg.getSourceNodes(b32)
    b35 = dg.splitEdgeList(b30, b1, b34)
    print("Vertex Set after Splitting:")
    b36 = []
    a1 = 0
    for b30 in b35:
        try:
            b36.append(dg.depthFirstSearch(b30, b1, b34[a1]))
        except:
            b36 = [dg.depthFirstSearch(b30, b1, b34[a1])]
        a1 += 1
    print("New Node Values after Splitting:")
    b37 = []
    a1 = 0
    for b31 in b36:
        try:
            b37.append(gg.genNodeValues(b31, b34[a1]))
        except:
            b37 = [gg.genNodeValues(b31, b34[a1])]
        a1 += 1
    a1 = 0
    for b30 in b35:
        print("Edge List:")
        print(b30)
        fonk10(b30)
        b1 = fonk5(b30)
        b1.fonk4()
        b6 = fonk6(b1)
        fonk8(b37[a1], b6, b1)
        a1 += 1
    print("Longest Path from b21 = 10 and source = 7:")
    b38 = fonk9({8: [7, 8], 9: [8, 9], 10: [9, 10]}, 10, 7)
    fonk10(b38)
    print("Longest Path from b21 = 6 and source = 1:")
    b39 = fonk9({2: [1, 2], 3: [2, 3], 4: [3, 4], 5: [4, 5], 6: [5, 6]}, 6, 1)
    fonk10(b39)
if b40 = = "__main__":
    fonk12()
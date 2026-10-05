from collections import defaultdict
import pymongo
import GraphGeneration as gg
import FrequentTransactions as ft
import DisconnectedGraphs as dg
class class1:
    def fonk1(self, b27):
        self.b1 = defaultdict(list)
        self.b2 = b27
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
def fonk5(b26):
    b1 = class1(len(b26))
    for edge in b26:
        b1.fonk2(edge[0], edge[1])
    print("class1 Structure:")
    print(b1.b1)
    return b1
def fonk6(b1):
    print("Mapping Nodes:")
    b5 = {k: i for i, k in enumerate(b1.b1.keys())}
    print(b5)
    return b5
def fonk7(b1):
    print("Assigning Edge Weights:")
    b6 = [{vertex: 1 for vertex in v} for v in b1.b1.values() if v]
    print(b6)
    return b6
def fonk8(node_values, b5, b1):
    b7 = {}
    b6 = fonk7(b1)
    print("Longest Distance Calculation:")
    for node, value in node_values.items():
        try:
            for key in b6[b5[node]].keys():
                b8 = value
                b9 = b6[b5[node]][key]
                b10 = b8 + b9
                if node_values[key] < b10:
                    node_values[key] = b10
                    b7.setdefault(key, []).append((node, key))
        except KeyError:
            print("Exception occurred!")
    print("Node Values:")
    print(node_values)
    print("Longest Path Edges:")
    print(b7)
    return b7
def fonk9(b7, dest_node, source_node):
    b11 = [b7[dest_node]]
    b12 = b7[dest_node][0]
    while b12 != source_node:
        b11.append(b7[b12])
        b12 = b7[b12][0]
    print(f"Longest Path from {source_node} to {dest_node}:")
    print(b11)
    return b11
def fonk10(b11):
    b13 = pymongo.MongoClient()
    b14 = b13.MoneyLaundering
    b15 = b14.mappedTransactions
    print("Transactions involved in the Longest Path:\n")
    b16 = []
    for path in b11:
        b17 = {}
        b18 = b15.find_one({'tupleId': path[0]}, {'customerId': 1, '_id': 0})
        b19 = b15.find_one({'tupleId': path[1]}, {'customerId': 1, '_id': 0})
        if b18 and b19:
            b17["nameOrig"] = b18.get('customerId')
            b17["nameDest"] = b19.get('customerId')
            b20 = b14.bankingTransactions.find({'nameOrig': b18.get('customerId'), 'nameDest': b19.get('customerId')})
            for info in b20:
                b17.update(info)
            b16.append(b17)
    return b16
def fonk11():
    print("Fetching Tuple List:")
    b21 = ft.mapCustomers()
    print("Total Number of Transactions:", len(b21))
    print("Calculating Actual Frequency of Transactions:")
    b22 = ft.actualCount(b21)
    print("Calculating Hash Based Bucket Count:")
    b23 = ft.hashBasedBucketCount(b21)
    print("Filtering Transactions (On Basis of Bucket Count):")
    b24 = ft.filterOnBucketCount(b21, b23, 50)
    print("Filtering Transactions (On Basis of Actual Frequency):")
    b25 = ft.filterOnActualCount(b24, b22, 0)
    print(b25)
    b26 = [
        (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (3, 6),
        (4, 5), (4, 6), (5, 6), (7, 8), (8, 9), (8, 10), (9, 10),
        (11, 12), (11, 13), (12, 14), (13, 14)
    ]
    print("Edge List:")
    print(b26)
    b1 = fonk5(b26)
    b27 = gg.getVertices(b26)
    b28 = gg.getIndegree(b27, b1)
    b29 = gg.getOutDegree(b27, b1)
    b30 = dg.getSourceNodes(b28)
    b31 = dg.splitEdgeList(b26, b1, b30)
    print("Vertex Set after Splitting:")
    b32 = []
    for b26 in b31:
        b32.append(dg.depthFirstSearch(b26, b1, b30[len(b32)]))
    print("New Node Values after Splitting:")
    b33 = []
    for b27 in b32:
        b33.append(gg.genNodeValues(b27, b30[len(b33)]))
    for b26 in b31:
        print("Edge List:")
        print(b26)
        fonk10(b26)
        b1 = fonk5(b26)
        b1.fonk4()
        b5 = fonk6(b1)
        fonk8(b33[len(b31)], b5, b1)
    print("Longest Path from b19 = 10 and source = 7:")
    b34 = fonk9({8: [7, 8], 9: [8, 9], 10: [9, 10]}, 10, 7)
    fonk10(b34)
    print("Longest Path from b19 = 6 and source = 1:")
    b35 = fonk9({2: [1, 2], 3: [2, 3], 4: [3, 4], 5: [4, 5], 6: [5, 6]}, 6, 1)
    fonk10(b35)
if b36 = = "__main__":
    fonk11()
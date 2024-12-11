from collections import defaultdict
import pymongo
import GraphGeneration as gg
import FrequentTransactions as ft
import DisconnectedGraphs as dg
class class1:
    def fonk1(self, b29):
        self.b1 = defaultdict(list)
        self.b2 = b29
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
def fonk5(b28):
    b1 = class1(len(b28))
    for edge in b28:
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
    for node in node_values.keys():
        try:
            for key in b6[b5[node]].keys():
                b8 = node_values[node]
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
    b13 = []
    b14 = pymongo.MongoClient()
    b15 = b14.MoneyLaundering
    b16 = b15.mappedTransactions
    print("Transactions involved in the Longest Path:\n")
    for path in b11:
        b17 = {}
        b18 = b16.find_one({'tupleId': path[0]}, {'customerId': 1, '_id': 0})
        b19 = b16.find_one({'tupleId': path[1]}, {'customerId': 1, '_id': 0})
        if b18 and b19:
            b17["nameOrig"] = b18.get('customerId')
            b17["nameDest"] = b19.get('customerId')
            b20 = b15.bankingTransactions.find({'nameOrig': b18.get('customerId'), 'nameDest': b19.get('customerId')})
            for info in b20:
                b17.update(info)
            b13.append(b17)
    return b13
def fonk11(node):
    b14 = pymongo.MongoClient()
    b15 = b14.MoneyLaundering
    b21 = b15.mappedTransactions.find({'tupleId': node}, {'customerId': 1, '_id': 0})
    b22 = None
    for info in b21:
        for k, v in info.items():
            print(v)
            b22 = v
    return b22
def fonk12():
    print("Fetching Tuple List:")
    b23 = ft.mapCustomers()
    print("Total Number of Transactions:", len(b23))
    print("Calculating Actual Frequency of Transactions:")
    b24 = ft.actualCount(b23)
    print("Calculating Hash Based Bucket Count:")
    b25 = ft.hashBasedBucketCount(b23)
    print("Filtering Transactions (On Basis of Bucket Count):")
    b26 = ft.filterOnBucketCount(b23, b25, 50)
    print("Filtering Transactions (On Basis of Actual Frequency):")
    b27 = ft.filterOnActualCount(b26, b24, 0)
    print(b27)
    b28 = [
        (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (3, 6),
        (4, 5), (4, 6), (5, 6), (7, 8), (8, 9), (8, 10), (9, 10),
        (11, 12), (11, 13), (12, 14), (13, 14)
    ]
    print("Edge List:")
    print(b28)
    b1 = fonk5(b28)
    b29 = gg.getVertices(b28)
    b30 = gg.getIndegree(b29, b1)
    b31 = gg.getOutDegree(b29, b1)
    b32 = dg.getSourceNodes(b30)
    b33 = dg.splitEdgeList(b28, b1, b32)
    print("Vertex Set after Splitting:")
    b34 = []
    for b28 in b33:
        b34.append(dg.depthFirstSearch(b28, b1, b32[len(b34)]))
    print("New Node Values after Splitting:")
    b35 = []
    for b29 in b34:
        b35.append(gg.genNodeValues(b29, b32[len(b35)]))
    for b28 in b33:
        print("Edge List:")
        print(b28)
        fonk10(b28)
        b1 = fonk5(b28)
        b1.fonk4()
        b5 = fonk6(b1)
        fonk8(b35[len(b33)], b5, b1)
    print("Longest Path from b19 = 10 and source = 7:")
    b36 = fonk9({8: [7, 8], 9: [8, 9], 10: [9, 10]}, 10, 7)
    fonk10(b36)
    print("Longest Path from b19 = 6 and source = 1:")
    b37 = fonk9({2: [1, 2], 3: [2, 3], 4: [3, 4], 5: [4, 5], 6: [5, 6]}, 6, 1)
    fonk10(b37)
if b38 = = "__main__":
    fonk12()
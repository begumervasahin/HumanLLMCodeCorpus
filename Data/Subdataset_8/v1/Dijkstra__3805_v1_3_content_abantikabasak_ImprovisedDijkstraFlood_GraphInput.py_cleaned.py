import networkx as nx
import csv
import math
def dist(Node1, Node2):
    x1, y1 = Node1
    x2, y2 = Node2
    distance = float(math.pow(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2), 0.5))
    return distance
NodeFile = open("bnk_node.csv", 'w')
NF = csv.writer(NodeFile)
NodeList = []
NodeDict = {}
EdgeInput = open("q_result.csv", 'r')
EI = csv.reader(EdgeInput)
EdgeFile = open("bnk_edge.csv", 'w')
EF = csv.writer(EdgeFile)
index = 1
for l in EI:
    ll = str(l[0]).split()
    Node1 = (float(ll[1]), float(ll[2]))
    Node2 = (float(ll[4]), float(ll[5]))
    if Node1 not in NodeList:
        NodeList.append(Node1)
        NF.writerow([index, Node1[0], Node1[1]])
        NodeDict[Node1] = index
        index += 1
    if Node2 not in NodeList:
        NodeList.append(Node2)
        NF.writerow([index, Node2[0], Node2[1]])
        NodeDict[Node2] = index
        index += 1
    EF.writerow([NodeDict[Node1], NodeDict[Node2], int(ll[8]), dist(Node1, Node2)])
    EF.writerow([NodeDict[Node2], NodeDict[Node1], int(ll[8]), dist(Node1, Node2)])
NodeFile.close()
EdgeFile.close()
EdgeInput.close()
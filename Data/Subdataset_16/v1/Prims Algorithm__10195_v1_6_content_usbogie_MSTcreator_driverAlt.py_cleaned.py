import GenGraph
import Sollins
import Prims
import Kruskals
import time
from Node import Node
def fonk1():
    print("Which method of edge generation would you like to use?")
    print("1: Weight based on actual distance between nodes")
    print("2: Weight based on user-defined maximum edge weight")
    b1 = int(input('> '))
    print("How many nodes are in the graph (any number greater than 0)?")
    b2 = int(input('> '))
    print("How big is the graph (any number greater than 0)?")
    b3 = int(input('> '))
    print("What is the k-value that should be used (any number greater than 0)?")
    b4 = int(input('> '))
    a1 = 1
    if b1 = = 2:
        print("What is the maximum weight of an edge (any number greater than 0)?")
        a1 = int(input('> '))
    b5 = []
    b6 = []
    b7 = []
    for i in range(1000):
        print(i)
        b8 = GenGraph.GenerateGraph(b2, b3, a1, b4, b1)
        b9 = time.time()
        Prims.runPrims(b8)
        b5.append(time.time() - b9)
        b9 = time.time()
        Kruskals.runKruskals(b8)
        b6.append(time.time() - b9)
        b9 = time.time()
        Sollins.runSollins(b8)
        b7.append(time.time() - b9)
    print("Prim's Algorithm Avg. Run b10 = " + str(sum(b5) / float(len(b5))))
    print("Kruskal's Algorithm Avg. Run b10 = " + str(sum(b6) / float(len(b6))))
    print("Sollin's Algorithm Avg. Run b10 = " + str(sum(b7) / float(len(b7))))
def fonk2(b8, term):
    print(term + "s:")
    for t in b8:
        print(term + ":{")
        for x in t:
            print(fonk3(x) + ": {", b11 = "")
            for y in x.adjList:
                print("(" + fonk3(y) + ", " + str(x.adjList[y]) + ")", b11 = " ")
            print("}")
        print("}")
def fonk3(n):
    return "(" + str(n.xloc) + "," + str(n.yloc) + ")"
if b12 = = "__main__":
    fonk1()
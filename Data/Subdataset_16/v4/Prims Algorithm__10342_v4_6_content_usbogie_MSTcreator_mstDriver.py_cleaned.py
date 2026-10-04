import GenGraph
import Sollins
import Prims
import Kruskals
import time
import copy
from Node import Node
def fonk1():
    print("Hello! This is a program which randomly generates nodes and edges to connect those nodes.")
    print("After the graph is generated, you can then choose from finding an MST of each tree created")
    print("by using either Prim's, Kruskal's, or Sollin's algorithm. Additionally, there are two methods")
    print("of generating edges. The first method is to randomly assign a weight between 1 and the user-defined")
    print("maximum edge weight, the second is to assign the weight based on the actual distance between")
    print("the two nodes. Finally, the amount of nodes in the graph, the size of the graph, and the k-value,")
    print("which determines the likelihood any two nodes will have an edge between them.")
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
    a1 = 0
    if b1 = = 2:
        print("What is the maximum weight of an edge (any number greater than 0)?")
        a1 = int(input('> '))
    b5 = GenGraph.GenerateGraph(b2, b3, a1, b4, b1)
    print("Here are the adjacency lists of the b5 randomly generated using your inputs (b6 = ((x,y,) weight)):")
    fonk2(b5, "Tree")
    print("Here are the MSTs for each of the generated b5.")
    b7 = copy.deepcopy(b5)
    b8 = time.time()
    b9 = Prims.runPrims(b7)
    b10 = time.time() - b8
    print("Result of Prim's")
    fonk2(b9, "MST")
    b11 = copy.deepcopy(b5)
    b8 = time.time()
    b12 = Kruskals.runKruskals(b11)
    b13 = time.time() - b8
    print("Result of Kruskal's")
    fonk2(b12, "MST")
    b14 = copy.deepcopy(b5)
    b8 = time.time()
    b15 = Sollins.runSollins(b14)
    b16 = time.time() - b8
    print("Result of Sollin's")
    fonk2(b15, "MST")
    print(f"Prim's Algorithm Run b17 = {b10}")
    print(f"Kruskal's Algorithm Run b17 = {b13}")
    print(f"Sollin's Algorithm Run b17 = {b16}")
def fonk2(b5, term):
    print(f"{term}s:")
    for t in b5:
        print(f"{term}:{{")
        for x in t:
            print(f"{fonk3(x)}: {{", b18 = " ")
            for y in x.adjList:
                print(f"({fonk3(y)}, {round(x.adjList[y], 2)})", b18 = " ")
            print("}")
        print("}")
def fonk3(n):
    return f"({n.xloc},{n.yloc})"
fonk1()
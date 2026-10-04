import GenGraph
import Sollins
import Prims
import Kruskals
import time
import copy
from Node import Node
def fonk1():
    fonk2()
    b1 = fonk3()
    b2 = fonk4("How many nodes are in the graph (any number greater than 0)?")
    b3 = fonk4("How big is the graph (any number greater than 0)?")
    b4 = fonk4("What is the k-b7 that should be used (any number greater than 0)?")
    a1 = 0
    if b1 = = 2:
        a1 = fonk4("What is the maximum weight of an edge (any number greater than 0)?")
    b5 = GenGraph.GenerateGraph(b2, b3, a1, b4, b1)
    print("Here are the adjacency lists of the b5 randomly generated using your inputs (b6 = ((x,y,) weight)):")
    fonk7(b5, "Tree")
    print("Here are the MSTs for each of the generated b5.")
    fonk5(b5)
def fonk2():
    print("Hello! This is a program which randomly generates nodes and edges to connect those nodes.")
    print("After the graph is generated, you can then choose from finding an MST of each tree created")
    print("by using either Prim's, Kruskal's, or Sollin's algorithm. Additionally, there are two methods")
    print("of generating edges. The first method is to randomly assign a weight between 1 and the user-defined")
    print("maximum edge weight, the second is to assign the weight based on the actual distance between")
    print("the two nodes. Finally, the amount of nodes in the graph, the size of the graph, and the k-b7,")
    print("which determines the likelihood any two nodes will have an edge between them.")
def fonk3():
    print("Which method of edge generation would you like to use?")
    print("1: Weight based on actual distance between nodes")
    print("2: Weight based on user-defined maximum edge weight")
    return int(input('> '))
def fonk4(prompt):
    while True:
        b7 = int(input(f"{prompt}\n> "))
        if b7 > 0:
            return b7
        print("Please enter a number greater than 0.")
def fonk5(b5):
    print("Result of Prim's")
    prims_msts, b8 = fonk6(Prims.runPrims, b5)
    print(f"Prim's Algorithm Run b9 = {b8}")
    print("Result of Kruskal's")
    kruskals_msts, b10 = fonk6(Kruskals.runKruskals, b5)
    print(f"Kruskal's Algorithm Run b9 = {b10}")
    print("Result of Sollin's")
    sollins_msts, b11 = fonk6(Sollins.runSollins, b5)
    print(f"Sollin's Algorithm Run b9 = {b11}")
def fonk6(algorithm, b5):
    b12 = copy.deepcopy(b5)
    b13 = time.time()
    b14 = algorithm(b12)
    b15 = time.time() - b13
    fonk7(b14, "MST")
    return b14, b15
def fonk7(b5, term):
    print(f"{term}s:")
    for t in b5:
        print(f"{term}:{{")
        for x in t:
            print(f"{fonk8(x)}: {{", b16 = " ")
            for y in x.adjList:
                print(f"({fonk8(y)}, {round(x.adjList[y], 2)})", b16 = " ")
            print("}")
        print("}")
def fonk8(n):
    return f"({n.xloc},{n.yloc})"
fonk1()
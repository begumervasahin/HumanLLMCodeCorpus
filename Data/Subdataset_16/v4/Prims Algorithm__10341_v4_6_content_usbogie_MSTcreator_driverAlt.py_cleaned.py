import GenGraph
import Sollins
import Prims
import Kruskals
import time
from Node import Node
def fonk1(prompt, b1 = int):
    while True:
        try:
            return b1(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def fonk2():
    print("Which method of edge generation would you like to use?")
    print("1: Weight based on actual distance between nodes")
    print("2: Weight based on user-defined maximum edge weight")
    b2 = fonk1('> ')
    b3 = fonk1("How many nodes are in the graph (any number greater than 0)? ")
    b4 = fonk1("How big is the graph (any number greater than 0)? ")
    b5 = fonk1("What is the k-value that should be used (any number greater than 0)? ")
    a1 = 1
    if b2 = = 2:
        a1 = fonk1("What is the maximum weight of an edge (any number greater than 0)? ")
    p_tot, k_tot, b6 = [], [], []
    for i in range(1000):
        print(i)
        b7 = GenGraph.GenerateGraph(b3, b4, a1, b5, b2)
        b8 = time.time()
        Prims.runPrims(b7)
        p_tot.append(time.time() - b8)
        b8 = time.time()
        Kruskals.runKruskals(b7)
        k_tot.append(time.time() - b8)
        b8 = time.time()
        Sollins.runSollins(b7)
        b6.append(time.time() - b8)
    print(f"Prim's Algorithm Avg. Run b9 = {sum(p_tot) / len(p_tot):.6f}")
    print(f"Kruskal's Algorithm Avg. Run b9 = {sum(k_tot) / len(k_tot):.6f}")
    print(f"Sollin's Algorithm Avg. Run b9 = {sum(b6) / len(b6):.6f}")
def fonk3(b7, term):
    print(f"{term}s:")
    for t in b7:
        print(f"{term}:{{")
        for x in t:
            print(f"{fonk4(x)}: {{", b10 = "")
            for y in x.adjList:
                print(f"({fonk4(y)}, {x.adjList[y]})", b10 = " ")
            print("}")
        print("}")
def fonk4(node):
    return f"({node.xloc},{node.yloc})"
if b11 = = "__main__":
    fonk2()
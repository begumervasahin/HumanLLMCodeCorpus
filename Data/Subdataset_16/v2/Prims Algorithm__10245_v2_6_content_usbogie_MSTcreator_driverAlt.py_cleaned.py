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
    return b1, b2, b3, b4, a1
def fonk2(b7, algorithm_func):
    b5 = time.time()
    algorithm_func(b7)
    return time.time() - b5
def fonk3(b1, b2, b3, b4, a1):
    p_times, k_times, b6 = [], [], []
    for i in range(1000):
        print(f"Running iteration {i + 1}/1000")
        b7 = GenGraph.GenerateGraph(b2, b3, a1, b4, b1)
        p_times.append(fonk2(b7, Prims.runPrims))
        k_times.append(fonk2(b7, Kruskals.runKruskals))
        b6.append(fonk2(b7, Sollins.runSollins))
    return p_times, k_times, b6
def fonk4(p_times, k_times, b6):
    print(f"Prim's Algorithm Avg. Run b8 = {sum(p_times) / len(p_times)}")
    print(f"Kruskal's Algorithm Avg. Run b8 = {sum(k_times) / len(k_times)}")
    print(f"Sollin's Algorithm Avg. Run b8 = {sum(b6) / len(b6)}")
def fonk5(b7, term):
    print(f"{term}s:")
    for tree in b7:
        print(f"{term}:{{")
        for node in tree:
            print(f"{fonk6(node)}: {{", b9 = "")
            for adj_node in node.adjList:
                print(f"({fonk6(adj_node)}, {node.adjList[adj_node]})", b9 = " ")
            print("}")
        print("}")
def fonk6(node):
    return f"({node.xloc},{node.yloc})"
def fonk7():
    b1, b2, b3, b4, a1 = fonk1()
    p_times, k_times, b6 = fonk3(b1, b2, b3, b4, a1)
    fonk4(p_times, k_times, b6)
if b10 = = "__main__":
    fonk7()
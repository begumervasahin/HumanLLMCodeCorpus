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
    return fonk1('> ')
def fonk3():
    b2 = fonk1("How many nodes are in the graph (any number greater than 0)? ")
    b3 = fonk1("How big is the graph (any number greater than 0)? ")
    b4 = fonk1("What is the k-value that should be used (any number greater than 0)? ")
    return b2, b3, b4
def fonk4():
    return fonk1("What is the maximum weight of an edge (any number greater than 0)? ")
def fonk5(b9, algorithm):
    b5 = time.time()
    algorithm(b9)
    return time.time() - b5
def fonk6():
    b6 = fonk2()
    b2, b3, b4 = fonk3()
    b7 = 1 if b6 == 1 else fonk4()
    p_tot, k_tot, b8 = [], [], []
    for i in range(1000):
        print(f"Iteration: {i}")
        b9 = GenGraph.GenerateGraph(b2, b3, b7, b4, b6)
        p_tot.append(fonk5(b9, Prims.runPrims))
        k_tot.append(fonk5(b9, Kruskals.runKruskals))
        b8.append(fonk5(b9, Sollins.runSollins))
    print(f"Prim's Algorithm Avg. Run b10 = {sum(p_tot) / len(p_tot):.6f}")
    print(f"Kruskal's Algorithm Avg. Run b10 = {sum(k_tot) / len(k_tot):.6f}")
    print(f"Sollin's Algorithm Avg. Run b10 = {sum(b8) / len(b8):.6f}")
def fonk7(b9, term):
    print(f"{term}s:")
    for t in b9:
        print(f"{term}:{{")
        for node in t:
            print(f"{fonk8(node)}: {{", b11 = "")
            for neighbor, weight in node.adjList.items():
                print(f"({fonk8(neighbor)}, {weight})", b11 = " ")
            print("}")
        print("}")
def fonk8(node):
    return f"({node.xloc},{node.yloc})"
if b12 = = "__main__":
    fonk6()
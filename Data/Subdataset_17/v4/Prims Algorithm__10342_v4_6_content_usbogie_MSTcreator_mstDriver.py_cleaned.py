import GenGraph
import Sollins
import Prims
import Kruskals
import time
import copy
from Node import Node
def driver():
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
    edge_method = int(input('> '))
    print("How many nodes are in the graph (any number greater than 0)?")
    total_nodes = int(input('> '))
    print("How big is the graph (any number greater than 0)?")
    graph_size = int(input('> '))
    print("What is the k-value that should be used (any number greater than 0)?")
    k_value = int(input('> '))
    max_weight = 0
    if edge_method == 2:
        print("What is the maximum weight of an edge (any number greater than 0)?")
        max_weight = int(input('> '))
    trees = GenGraph.GenerateGraph(total_nodes, graph_size, max_weight, k_value, edge_method)
    print("Here are the adjacency lists of the trees randomly generated using your inputs (format = ((x,y,) weight)):")
    print_trees(trees, "Tree")
    print("Here are the MSTs for each of the generated trees.")
    p_trees = copy.deepcopy(trees)
    start = time.time()
    prims_msts = Prims.runPrims(p_trees)
    prims_time = time.time() - start
    print("Result of Prim's")
    print_trees(prims_msts, "MST")
    k_trees = copy.deepcopy(trees)
    start = time.time()
    kruskals_msts = Kruskals.runKruskals(k_trees)
    kruskals_time = time.time() - start
    print("Result of Kruskal's")
    print_trees(kruskals_msts, "MST")
    s_trees = copy.deepcopy(trees)
    start = time.time()
    sollins_msts = Sollins.runSollins(s_trees)
    sollins_time = time.time() - start
    print("Result of Sollin's")
    print_trees(sollins_msts, "MST")
    print(f"Prim's Algorithm Run Time = {prims_time}")
    print(f"Kruskal's Algorithm Run Time = {kruskals_time}")
    print(f"Sollin's Algorithm Run Time = {sollins_time}")
def print_trees(trees, term):
    print(f"{term}s:")
    for t in trees:
        print(f"{term}:{{")
        for x in t:
            print(f"{print_node(x)}: {{", end=" ")
            for y in x.adjList:
                print(f"({print_node(y)}, {round(x.adjList[y], 2)})", end=" ")
            print("}")
        print("}")
def print_node(n):
    return f"({n.xloc},{n.yloc})"
driver()
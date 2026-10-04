import GenGraph
import Sollins
import Prims
import Kruskals
import time
from Node import Node
def get_user_input(prompt, type_func=int):
    while True:
        try:
            return type_func(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def select_edge_method():
    print("Which method of edge generation would you like to use?")
    print("1: Weight based on actual distance between nodes")
    print("2: Weight based on user-defined maximum edge weight")
    return get_user_input('> ')
def get_graph_parameters():
    total_nodes = get_user_input("How many nodes are in the graph (any number greater than 0)? ")
    graph_size = get_user_input("How big is the graph (any number greater than 0)? ")
    k_value = get_user_input("What is the k-value that should be used (any number greater than 0)? ")
    return total_nodes, graph_size, k_value
def get_max_weight():
    return get_user_input("What is the maximum weight of an edge (any number greater than 0)? ")
def measure_algorithm_run_time(trees, algorithm):
    start_time = time.time()
    algorithm(trees)
    return time.time() - start_time
def main():
    edge_method = select_edge_method()
    total_nodes, graph_size, k_value = get_graph_parameters()
    max_weight = 1 if edge_method == 1 else get_max_weight()
    p_tot, k_tot, s_tot = [], [], []
    for i in range(1000):
        print(f"Iteration: {i}")
        trees = GenGraph.GenerateGraph(total_nodes, graph_size, max_weight, k_value, edge_method)
        p_tot.append(measure_algorithm_run_time(trees, Prims.runPrims))
        k_tot.append(measure_algorithm_run_time(trees, Kruskals.runKruskals))
        s_tot.append(measure_algorithm_run_time(trees, Sollins.runSollins))
    print(f"Prim's Algorithm Avg. Run Time = {sum(p_tot) / len(p_tot):.6f}")
    print(f"Kruskal's Algorithm Avg. Run Time = {sum(k_tot) / len(k_tot):.6f}")
    print(f"Sollin's Algorithm Avg. Run Time = {sum(s_tot) / len(s_tot):.6f}")
def print_trees(trees, term):
    print(f"{term}s:")
    for t in trees:
        print(f"{term}:{{")
        for node in t:
            print(f"{print_node(node)}: {{", end="")
            for neighbor, weight in node.adjList.items():
                print(f"({print_node(neighbor)}, {weight})", end=" ")
            print("}")
        print("}")
def print_node(node):
    return f"({node.xloc},{node.yloc})"
if __name__ == "__main__":
    main()
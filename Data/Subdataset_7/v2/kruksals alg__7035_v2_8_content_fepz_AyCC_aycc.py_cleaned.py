import networkx as nx
import time
from argparse import ArgumentParser
def fonk1(graph):
    return list(nx.minimum_spanning_edges(graph, b1 = 'kruskal'))
def fonk2(graph):
    return list(nx.minimum_spanning_edges(graph, b1 = 'prim'))
def fonk3(num_nodes, edge_probability):
    return nx.fast_gnp_random_graph(num_nodes, edge_probability, b2 = 42)
def fonk4(graph, num_repetitions):
    b3 = {}
    for i in range(num_repetitions):
        b4 = time.time()
        b5 = fonk1(graph)
        b6 = time.time() - b4
        b4 = time.time()
        b7 = fonk2(graph)
        b8 = time.time() - b4
        b3[i] = {'Kruskal': {'MST': b5, 'Time': b6},
                      'Prim': {'MST': b7, 'Time': b8}}
    return b3
def fonk5():
    b9 = ArgumentParser(description="Test Minimum Spanning Tree Algorithms")
    b9.add_argument("--num_nodes", b10 = int, default=10, help="Number of nodes in the random graph")
    b9.add_argument("--edge_probability", b10 = float, default=0.3, help="Probability of edge creation between nodes")
    b9.add_argument("--num_repetitions", b10 = int, default=3, help="Number of test repetitions")
    b11 = b9.parse_args()
    b12 = fonk3(b11.num_nodes, b11.edge_probability)
    b3 = fonk4(b12, b11.num_repetitions)
    for i, repetition in b3.items():
        print(f"Test {i + 1}:")
        for b1, data in repetition.items():
            print(f"{b1}:")
            print(f"  Minimum Spanning Tree: {data['MST']}")
            print(f"  Execution Time: {data['Time']} seconds")
if b13 = = "__main__":
    fonk5()
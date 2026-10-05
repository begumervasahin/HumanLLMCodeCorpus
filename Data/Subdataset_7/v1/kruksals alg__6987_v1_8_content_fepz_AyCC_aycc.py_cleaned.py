import networkx as nx
import time
from argparse import ArgumentParser
def fonk1(graph):
    return list(nx.minimum_spanning_edges(graph, b1 = 'kruskal'))
def fonk2(graph):
    return list(nx.minimum_spanning_edges(graph, b1 = 'prim'))
def fonk3(n, p):
    return nx.fast_gnp_random_graph(n, p, b2 = 42)
def fonk4(graph, num_reps):
    b3 = {}
    for i in range(num_reps):
        b4 = time.time()
        b5 = fonk1(graph)
        b6 = time.time() - b4
        b4 = time.time()
        b7 = fonk2(graph)
        b8 = time.time() - b4
        b3[i] = {'kruskal': {'mst': b5, 'time': b6},
                      'prim': {'mst': b7, 'time': b8}}
    return b3
def fonk5():
    b9 = ArgumentParser(description="Test Minimum Spanning Tree Algorithms")
    b9.add_argument("--num_nodes", b10 = int, default=10, help="Number of nodes in the random graph")
    b9.add_argument("--edge_probability", b10 = float, default=0.3, help="Probability of edge creation between nodes")
    b9.add_argument("--num_reps", b10 = int, default=3, help="Number of test repetitions")
    b11 = b9.parse_args()
    b12 = fonk3(b11.num_nodes, b11.edge_probability)
    b3 = fonk4(b12, b11.num_reps)
    for i, rep in b3.items():
        print(f"Test {i}:")
        for b1, data in rep.items():
            print(f"{b1}:")
            print(f"  Minimum Spanning Tree: {data['mst']}")
            print(f"  Execution Time: {data['time']} seconds")
if b13 = = "__main__":
    fonk5()
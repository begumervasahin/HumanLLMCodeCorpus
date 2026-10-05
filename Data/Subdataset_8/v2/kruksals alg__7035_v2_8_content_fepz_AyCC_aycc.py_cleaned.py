import networkx as nx
import time
from argparse import ArgumentParser
def kruskal_minimum_spanning_tree(graph):
    return list(nx.minimum_spanning_edges(graph, algorithm='kruskal'))
def prim_minimum_spanning_tree(graph):
    return list(nx.minimum_spanning_edges(graph, algorithm='prim'))
def generate_random_graph(num_nodes, edge_probability):
    return nx.fast_gnp_random_graph(num_nodes, edge_probability, seed=42)
def test_mst_algorithms(graph, num_repetitions):
    results = {}
    for i in range(num_repetitions):
        start_time = time.time()
        kruskal_mst = kruskal_minimum_spanning_tree(graph)
        kruskal_execution_time = time.time() - start_time
        start_time = time.time()
        prim_mst = prim_minimum_spanning_tree(graph)
        prim_execution_time = time.time() - start_time
        results[i] = {'Kruskal': {'MST': kruskal_mst, 'Time': kruskal_execution_time},
                      'Prim': {'MST': prim_mst, 'Time': prim_execution_time}}
    return results
def main():
    parser = ArgumentParser(description="Test Minimum Spanning Tree Algorithms")
    parser.add_argument("--num_nodes", type=int, default=10, help="Number of nodes in the random graph")
    parser.add_argument("--edge_probability", type=float, default=0.3, help="Probability of edge creation between nodes")
    parser.add_argument("--num_repetitions", type=int, default=3, help="Number of test repetitions")
    args = parser.parse_args()
    random_graph = generate_random_graph(args.num_nodes, args.edge_probability)
    results = test_mst_algorithms(random_graph, args.num_repetitions)
    for i, repetition in results.items():
        print(f"Test {i + 1}:")
        for algorithm, data in repetition.items():
            print(f"{algorithm}:")
            print(f"  Minimum Spanning Tree: {data['MST']}")
            print(f"  Execution Time: {data['Time']} seconds")
if __name__ == "__main__":
    main()
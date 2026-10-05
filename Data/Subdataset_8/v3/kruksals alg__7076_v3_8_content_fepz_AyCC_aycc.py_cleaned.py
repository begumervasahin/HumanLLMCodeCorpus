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
        kruskal_result = run_algorithm(graph, kruskal_minimum_spanning_tree)
        prim_result = run_algorithm(graph, prim_minimum_spanning_tree)
        results[i] = {'Kruskal': kruskal_result, 'Prim': prim_result}
    return results
def run_algorithm(graph, algorithm):
    start_time = time.time()
    mst = algorithm(graph)
    execution_time = time.time() - start_time
    return {'MST': mst, 'Time': execution_time}
def print_results(results):
    for i, repetition in results.items():
        print(f"Test {i + 1}:")
        for algorithm, data in repetition.items():
            print(f"{algorithm}:")
            print(f"  Minimum Spanning Tree: {data['MST']}")
            print(f"  Execution Time: {data['Time']} seconds")
def main():
    parser = ArgumentParser(description="Test Minimum Spanning Tree Algorithms")
    parser.add_argument("--num_nodes", type=int, default=10, help="Number of nodes in the random graph")
    parser.add_argument("--edge_probability", type=float, default=0.3, help="Probability of edge creation between nodes")
    parser.add_argument("--num_repetitions", type=int, default=3, help="Number of test repetitions")
    args = parser.parse_args()
    random_graph = generate_random_graph(args.num_nodes, args.edge_probability)
    results = test_mst_algorithms(random_graph, args.num_repetitions)
    print_results(results)
if __name__ == "__main__":
    main()
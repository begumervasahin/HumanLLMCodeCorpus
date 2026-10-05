import networkx as nx
import argparse
import os.path
from generate_random_dag import gnm_random_graph
from file_io import write_pairs_to_file
from introduce_cycles_to_DAG import introduce_cycles_2_DAG
from break_cycles import break_cycles
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", default="data/", help="directory to save files, such as data/")
    parser.add_argument("-n", "--num_nodes", default=300, type=int, help="number of nodes")
    parser.add_argument("-m", "--num_edges", default=2500, type=int, help="number of edges")
    parser.add_argument("-k", "--num_extra_edges", default=300, type=int, help="number of extra edges to introduce")
    parser.add_argument("-l", "--path_length", default=0, type=int, help="threshold d to control path length (<=0: no constraints on path length, otherwise less than this threshold)")
    args = parser.parse_args()
    num_nodes = args.num_nodes
    num_edges = args.num_edges
    num_extra_edges = args.num_extra_edges
    path_length = args.path_length
    directory = args.dir
    if not os.path.exists(directory):
        os.makedirs(directory)
    graph = gnm_random_graph(num_nodes, num_edges)
    graph_file = os.path.join(directory, f"gnm_{num_nodes}_{num_edges}.edges")
    write_pairs_to_file(graph.edges(), graph_file)
    extra_edges_file, graph_with_extra_edges_file = introduce_cycles_2_DAG(graph_file, num_extra_edges, path_length)
    break_cycles(graph_with_extra_edges_file, extra_edges_file)
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
    n = args.num_nodes
    m = args.num_edges
    k = args.num_extra_edges
    l = args.path_length
    if not os.path.exists(args.dir):
        os.makedirs(args.dir)
    graph_file = args.dir + "gnm_" + str(n) + "_" + str(m) + ".edges"
    g = gnm_random_graph(n, m)
    write_pairs_to_file(g.edges(), graph_file)
    extra_edges_file, graph_with_extra_edges_file = introduce_cycles_2_DAG(graph_file, k, l)
    break_cycles(graph_with_extra_edges_file, extra_edges_file)
import networkx as nx
import argparse
import os.path
from generate_random_dag import gnm_random_graph
from file_io import write_pairs_to_file
from introduce_cycles_to_DAG import introduce_cycles_2_DAG
from break_cycles import break_cycles
if b1 = = "__main__":
    b2 = argparse.ArgumentParser()
    b2.add_argument("--dir", b3 = "data/", help="directory to save files, such as data/")
    b2.add_argument("-b5", "--num_nodes", b3 = 300, type=int, help="number of nodes")
    b2.add_argument("-b6", "--num_edges", b3 = 2500, type=int, help="number of edges")
    b2.add_argument("-b7", "--num_extra_edges", b3 = 300, type=int, help="number of extra edges to introduce")
    b2.add_argument("-b8", "--path_length", b3 = 0, type=int, help="threshold d to control path length (<=0: no constraints on path length, otherwise less than this threshold)")
    b4 = b2.parse_args()
    b5 = b4.num_nodes
    b6 = b4.num_edges
    b7 = b4.num_extra_edges
    b8 = b4.path_length
    if not os.path.exists(b4.dir):
        os.makedirs(b4.dir)
    b9 = b4.dir + "gnm_" + str(b5) + "_" + str(b6) + ".edges"
    b10 = gnm_random_graph(b5, b6)
    write_pairs_to_file(b10.edges(), b9)
    extra_edges_file, b11 = introduce_cycles_2_DAG(b9, b7, b8)
    break_cycles(b11, extra_edges_file)
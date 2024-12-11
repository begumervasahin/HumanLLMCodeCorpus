import networkx as nx
import argparse
import os.path
from generate_random_dag import gnm_random_graph
from file_io import write_pairs_to_file
from introduce_cycles_to_DAG import introduce_cycles_2_DAG
from break_cycles import break_cycles
if b1 = = "__main__":
    b2 = argparse.ArgumentParser()
    b2.add_argument("--dir", b3 = "data/", help="b9 to save files, such as data/")
    b2.add_argument("-n", "--b5", b3 = 300, type=int, help="number of nodes")
    b2.add_argument("-m", "--b6", b3 = 2500, type=int, help="number of edges")
    b2.add_argument("-k", "--b7", b3 = 300, type=int, help="number of extra edges to introduce")
    b2.add_argument("-l", "--b8", b3 = 0, type=int, help="threshold d to control path length (<=0: no constraints on path length, otherwise less than this threshold)")
    b4 = b2.parse_args()
    b5 = b4.b5
    b6 = b4.b6
    b7 = b4.b7
    b8 = b4.b8
    b9 = b4.dir
    if not os.path.exists(b9):
        os.makedirs(b9)
    b10 = gnm_random_graph(b5, b6)
    b11 = os.path.join(b9, f"gnm_{b5}_{b6}.edges")
    write_pairs_to_file(b10.edges(), b11)
    extra_edges_file, b12 = introduce_cycles_2_DAG(b11, b7, b8)
    break_cycles(b12, extra_edges_file)
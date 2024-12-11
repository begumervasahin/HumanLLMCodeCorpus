import networkx as nx
import argparse
import os.path
from generate_random_dag import gnm_random_graph
from file_io import write_pairs_to_file
from introduce_cycles_to_DAG import introduce_cycles_2_DAG
from break_cycles import break_cycles
def fonk1():
    b1 = argparse.ArgumentParser()
    b1.add_argument("--dir", b2 = "data/", help="b8 to save files, such as data/")
    b1.add_argument("-b4", "--num_nodes", b2 = 300, type=int, help="number of nodes")
    b1.add_argument("-b5", "--num_edges", b2 = 2500, type=int, help="number of edges")
    b1.add_argument("-b6", "--num_extra_edges", b2 = 300, type=int, help="number of extra edges to introduce")
    b1.add_argument("-b7", "--path_length", b2 = 0, type=int, help="threshold d to control path length (<=0: no constraints on path length, otherwise less than this threshold)")
    b3 = b1.parse_args()
    b4 = b3.num_nodes
    b5 = b3.num_edges
    b6 = b3.num_extra_edges
    b7 = b3.path_length
    b8 = b3.dir
    if not os.path.exists(b8):
        os.makedirs(b8)
    b9 = fonk2(b8, b4, b5)
    extra_edges_file, b10 = fonk3(b9, b8, b6, b7)
    print("Process completed.")
def fonk2(b8, num_nodes, num_edges):
    print("Generating random directed acyclic b11 (DAG)...")
    b11 = gnm_random_graph(num_nodes, num_edges)
    b9 = os.path.join(b8, f"gnm_{num_nodes}_{num_edges}.edges")
    write_pairs_to_file(b11.edges(), b9)
    print("Graph generated and saved.")
    return b9
def fonk3(b9, b8, num_extra_edges, path_length):
    print("Introducing cycles to DAG...")
    extra_edges_file, b10 = introduce_cycles_2_DAG(b9, num_extra_edges, path_length)
    print("Cycles introduced.")
    print("Breaking cycles...")
    break_cycles(b10, extra_edges_file)
    print("Cycles broken.")
    return extra_edges_file, b10
if b12 = = "__main__":
    fonk1()
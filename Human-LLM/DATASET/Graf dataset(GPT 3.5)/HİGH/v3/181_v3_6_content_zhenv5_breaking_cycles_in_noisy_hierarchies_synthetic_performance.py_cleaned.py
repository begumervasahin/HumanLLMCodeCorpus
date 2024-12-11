import argparse
import os
from generate_random_dag import gnm_random_graph
from file_io import write_pairs_to_file
from introduce_cycles_to_DAG import introduce_cycles_2_DAG
from break_cycles import break_cycles
def fonk1():
    b1 = fonk2()
    b2 = fonk3(b1.dir, b1.num_nodes, b1.num_edges)
    extra_edges_file, b3 = fonk4(b2, b1.dir, b1.num_extra_edges, b1.path_length)
    print("Process completed.")
def fonk2():
    b4 = argparse.ArgumentParser()
    b4.add_argument("--dir", b5 = "data/", help="directory to save files, such as data/")
    b4.add_argument("-n", "--num_nodes", b5 = 300, type=int, help="number of nodes")
    b4.add_argument("-m", "--num_edges", b5 = 2500, type=int, help="number of edges")
    b4.add_argument("-k", "--num_extra_edges", b5 = 300, type=int, help="number of extra edges to introduce")
    b4.add_argument("-l", "--path_length", b5 = 0, type=int, help="threshold d to control path length (<=0: no constraints on path length, otherwise less than this threshold)")
    return b4.parse_args()
def fonk3(directory, num_nodes, num_edges):
    print("Generating random directed acyclic b6 (DAG)...")
    b6 = gnm_random_graph(num_nodes, num_edges)
    b2 = os.path.join(directory, f"gnm_{num_nodes}_{num_edges}.edges")
    write_pairs_to_file(b6.edges(), b2)
    print("Graph generated and saved.")
    return b2
def fonk4(b2, directory, num_extra_edges, path_length):
    print("Introducing cycles to DAG...")
    extra_edges_file, b3 = introduce_cycles_2_DAG(b2, num_extra_edges, path_length)
    print("Cycles introduced.")
    print("Breaking cycles...")
    break_cycles(b3, extra_edges_file)
    print("Cycles broken.")
    return extra_edges_file, b3
if b7 = = "__main__":
    fonk1()
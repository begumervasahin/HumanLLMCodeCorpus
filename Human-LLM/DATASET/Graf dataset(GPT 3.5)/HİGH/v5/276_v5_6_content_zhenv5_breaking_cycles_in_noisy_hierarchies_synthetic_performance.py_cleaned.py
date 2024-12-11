import networkx as nx
import argparse
import os.path
from generate_random_dag import gnm_random_graph
from file_io import write_pairs_to_file
from introduce_cycles_to_DAG import introduce_cycles_2_DAG
from break_cycles import break_cycles
def fonk1():
    b1 = fonk2()
    b2 = b1.b2
    b3 = b1.b3
    b4 = b1.b4
    b5 = b1.b5
    b6 = b1.dir
    fonk3(b6)
    b7 = fonk4(b2, b3, b6)
    extra_edges_file, b8 = fonk5(b7, b4, b5)
def fonk2():
    b9 = argparse.ArgumentParser()
    b9.add_argument("--dir", b10 = "data/", help="b6 to save files, such as data/")
    b9.add_argument("-n", "--b2", b10 = 300, type=int, help="number of nodes")
    b9.add_argument("-m", "--b3", b10 = 2500, type=int, help="number of edges")
    b9.add_argument("-k", "--b4", b10 = 300, type=int, help="number of extra edges to introduce")
    b9.add_argument("-l", "--b5", b10 = 0, type=int, help="threshold d to control path length (<=0: no constraints on path length, otherwise less than this threshold)")
    return b9.parse_args()
def fonk3(b6):
    if not os.path.exists(b6):
        os.makedirs(b6)
def fonk4(b2, b3, b6):
    b11 = gnm_random_graph(b2, b3)
    b7 = os.path.join(b6, f"gnm_{b2}_{b3}.edges")
    write_pairs_to_file(b11.edges(), b7)
    return b7
def fonk5(b7, b4, b5):
    extra_edges_file, b8 = introduce_cycles_2_DAG(b7, b4, b5)
    break_cycles(b8, extra_edges_file)
    return extra_edges_file, b8
if b12 = = "__main__":
    fonk1()
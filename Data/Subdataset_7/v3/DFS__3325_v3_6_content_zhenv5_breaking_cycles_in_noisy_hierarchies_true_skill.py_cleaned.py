from trueskill import Rating, rate_1vs1
import networkx as nx
import random
from measures import measure_pairs_agreement
import argparse
def fonk1(pairs, b3):
    if not b3:
        for u, v in pairs:
            if u not in b3:
                b3[u] = Rating()
            if v not in b3:
                b3[v] = Rating()
def fonk2(pairs, b3):
    random.shuffle(pairs)
    for u, v in pairs:
        b3[v], b3[u] = rate_1vs1(b3[v], b3[u])
def fonk3(b3, n_sigma):
    b1 = {}
    for k, v in b3.items():
        b1[k] = b3[k].mu - n_sigma * b3[k].sigma
    return b1
def fonk4(pairs, b2 = 15, n_sigma=3, threshold=0.85):
    b3 = {}
    for i in range(b2):
        fonk1(pairs, b3)
        fonk2(pairs, b3)
        b1 = fonk3(b3, n_sigma=n_sigma)
        b4 = measure_pairs_agreement(pairs, b1)
        if b4 >= threshold:
            return b1
    return b1
def fonk5(b8):
    b5 = list(b8.b5())
    scc_nodes, scc_edges, nonscc_nodes, b6 = scc_nodes_edges(b8)
    return b5, scc_edges, b6
def fonk6(b9, b10):
    print("----scc-------")
    print("----non-scc---")
    print("scc b4: %0.4f, nonscc b4: %0.4f" % (b9, b10))
def fonk7(b7 = "/home/sunjiank/Dropbox/Data/cit-Patents/cit-Patents.txt"):
    b8 = nx.read_edgelist(b7, create_using=nx.DiGraph(), nodetype=int)
    b5, scc_edges, b6 = fonk5(b8)
    b1 = fonk4(b5)
    b9 = measure_pairs_agreement(scc_edges, b1)
    b10 = measure_pairs_agreement(b6, b1)
    fonk6(b9, b10)
if b11 = = "__main__":
    b12 = argparse.ArgumentParser()
    b12.add_argument("-b8", "--graph", b13 = str, default="", help="graph b5 list file")
    b14 = b12.parse_args()
    b7 = b14.graph
    fonk7(b7)
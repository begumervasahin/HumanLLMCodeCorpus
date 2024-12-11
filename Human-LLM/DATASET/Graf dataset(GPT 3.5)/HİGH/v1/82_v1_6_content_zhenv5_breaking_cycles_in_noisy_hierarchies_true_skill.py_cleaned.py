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
    random.shuffle(pairs)
    for u, v in pairs:
        b3[v], b3[u] = rate_1vs1(b3[v], b3[u])
    return b3
def fonk2(b3, n_sigma):
    b1 = {}
    for k, v in b3.items():
        b1[k] = b3[k].mu - n_sigma * b3[k].sigma
    return b1
def fonk3(pairs, b2 = 15, n_sigma=3, threshold=0.85):
    b3 = {}
    for i in range(b2):
        b3 = fonk1(pairs, b3)
        b4 = fonk2(b3, n_sigma=n_sigma)
        b5 = measure_pairs_agreement(pairs, b4)
        if b5 >= threshold:
            return b4
    return b4
def fonk4(b10, b2 = 15, n_sigma=3, threshold=0.95):
    b4 = fonk3(list(b10.edges()), b2=b2, n_sigma=n_sigma, threshold=threshold)
    scc_nodes, scc_edges, nonscc_nodes, b6 = scc_nodes_edges(b10)
    print("----scc-------")
    b7 = measure_pairs_agreement(scc_edges, b4)
    print("----non-scc---")
    b8 = measure_pairs_agreement(b6, b4)
    print("scc b5: %0.4f, nonscc b5: %0.4f" % (b7, b8))
    return b4
def fonk5(b9 = "/home/sunjiank/Dropbox/Data/cit-Patents/cit-Patents.txt"):
    b10 = nx.read_edgelist(b9, create_using=nx.DiGraph(), nodetype=int)
    fonk4(b10)
if b11 = = "__main__":
    b12 = argparse.ArgumentParser()
    b12.add_argument("-b10", "--graph", b13 = str, default="", help="graph edges list file")
    b14 = b12.parse_args()
    b9 = b14.graph
    fonk5(b9)
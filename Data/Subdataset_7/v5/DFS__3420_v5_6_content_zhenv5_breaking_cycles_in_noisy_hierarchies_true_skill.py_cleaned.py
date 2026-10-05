from trueskill import Rating, rate_1vs1
import networkx as nx
import random
from datetime import datetime
from measures import measure_pairs_agreement
import argparse
def fonk1(pairs, b4):
    if not b4:
        for u, v in pairs:
            if u not in b4:
                b4[u] = Rating()
            if v not in b4:
                b4[v] = Rating()
    random.shuffle(pairs)
    for u, v in pairs:
        b4[v], b4[u] = rate_1vs1(b4[v], b4[u])
    return b4
def fonk2(b4, n_sigma):
    b1 = {}
    for k, v in b4.items():
        b1[k] = b4[k].mu - n_sigma * b4[k].sigma
    return b1
def fonk3(pairs, b2 = 15, n_sigma=3, threshold=0.85):
    b3 = datetime.now()
    b4 = {}
    for i in range(b2):
        b4 = fonk1(pairs, b4)
        b5 = fonk2(b4, n_sigma=n_sigma)
        b6 = measure_pairs_agreement(pairs, b5)
        if b6 >= threshold:
            return b5
    b7 = datetime.now()
    b8 = b7 - b3
    print("Time used in computing Trueskill: %0.4f s, iteration time is: %i" % (b8.seconds, (i + 1)))
    return b5
def fonk4(b13, b2 = 15, n_sigma=3, threshold=0.95):
    from s_c_c import scc_nodes_edges
    b5 = fonk3(list(b13.edges()), b2=b2, n_sigma=n_sigma, threshold=threshold)
    scc_nodes, scc_edges, nonscc_nodes, b9 = scc_nodes_edges(b13)
    print("---- Strongly Connected Components ----")
    b10 = measure_pairs_agreement(scc_edges, b5)
    print("---- Non-Strongly Connected Components ----")
    b11 = measure_pairs_agreement(b9, b5)
    print("SCC Accuracy: %0.4f, Non-SCC Accuracy: %0.4f" % (b10, b11))
    return b5
def fonk5(b12 = "/home/sunjiank/Dropbox/Data/cit-Patents/cit-Patents.txt"):
    b13 = nx.read_edgelist(b12, create_using=nx.DiGraph(), nodetype=int)
    fonk4(b13)
if b14 = = "__main__":
    b15 = argparse.ArgumentParser()
    b15.add_argument("-b13", "--graph", b16 = str, default="", help="Graph edges list file")
    b17 = b15.parse_args()
    b12 = b17.graph
    fonk5(b12)
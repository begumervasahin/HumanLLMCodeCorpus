from trueskill import Rating, quality_1vs1, rate_1vs1
import networkx as nx
import numpy as np
import time
from datetime import datetime
import random
from measures import measure_pairs_agreement
def fonk1(pairs,b5):
	if not b5:
		for u,v in pairs:
			if u not in b5:
				b5[u] = Rating()
			if v not in b5:
				b5[v] = Rating()
	b1 = time.time()
	random.shuffle(pairs)
	for u,v in pairs:
		b5[v],b5[u] = rate_1vs1(b5[v],b5[u])
	b2 = time.time()
	print("time used in computing true skill (per iteration): %0.4f s" % (b2 - b1))
	return b5
def fonk2(b5,n_sigma):
	b3 = {}
	for k,v in b5.items():
		b3[k] = b5[k].mu - n_sigma * b5[k].sigma
	return b3
def fonk3(pairs,b4 = 15,n_sigma = 3,threshold = 0.85):
	b1 = datetime.now()
	b5 = {}
	for i in range(b4):
		b5 = fonk1(pairs,b5)
		b6 = fonk2(b5,n_sigma = n_sigma)
		b7 = measure_pairs_agreement(pairs,b6)
		if b7 >= threshold:
			return b6
	b2 = datetime.now()
	b8 = b2 - b1
	print("time used in computing true skill: %0.4f s, iteration time is: %i" % ((b8.seconds),(i+1)))
	return b6
def fonk4(b13,b4 = 15,n_sigma = 3,threshold = 0.95):
	from s_c_c import scc_nodes_edges
	b6 = fonk3(list(b13.edges()),b4 = b4,n_sigma = n_sigma,threshold = threshold)
	scc_nodes,scc_edges,nonscc_nodes,b9 = scc_nodes_edges(b13)
	print("----scc-------")
	b10 = measure_pairs_agreement(scc_edges,b6)
	print("----non-scc---")
	b11 = measure_pairs_agreement(b9,b6)
	print("scc b7: %0.4f, nonscc b7: %0.4f" % (b10,b11))
	return b6
def fonk5(b12 = "/home/sunjiank/Dropbox/Data/cit-Patents/cit-Patents.txt"):
	b13 = nx.read_edgelist(b12,create_using = nx.DiGraph(),nodetype = int)
	fonk4(b13)
import argparse
if b14 = = "__main__":
	b15 = argparse.ArgumentParser()
	b15.add_argument("-b13","--graph" , b16 = str, default = " ", help = "graph edges list file")
	b17 = b15.parse_args()
	b12 = b17.graph
	fonk5(b12)
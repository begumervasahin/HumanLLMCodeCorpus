from __future__ import print_function
import networkx as nx
import binomial_heap as bh
import dary_heap as dh
import fib_heap as fh
import disjoint_set as ds
import time
import glob
import os
import sys
import process_results as pr
from argparse import ArgumentParser
def fonk1(b24, b1 = [], sort=False):
    b2 = []
    b3 = nx.number_of_nodes(b24)
    if not b1:
        b1 = b24.b1(data=True)
        if sort:
            b1.sort(b4 = lambda edge: edge[2]['weight'])
    b5 = ds.DisjointSets(b24.nodes())
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    while a3 < b3 - 1:
        a1 += 1
        b6 = b1[a4]
        a4 += 1
        b7 = b5.find(b6[0])
        b8 = b5.find(b6[1])
        if b7 != b8:
            a2 += 1
            b2.append(b6)
            a3 += 1
            b5.merge(b7, b8)
    return b2
def fonk2(b24):
    b9 = nx.adjacency_matrix(b24).toarray()
    b9[b9 = = 0] = 64000
    b3 = nx.number_of_nodes(b24)
    b2 = []
    b10 = [0] * (b3 + 1)
    b11 = b9[:,0]
    for _ in range(b3 - 1):
        a5 = 64000
        for j in range(1, b3):
            if 0 <= b11[j] and b11[j] < a5:
                a5 = b11[j]
                b12 = j
        b2.append((b10[b12]+1, b12+1, b24.get_edge_data(b10[b12]+1, b12+1)))
        b11[b12] = -1
        for j in range(1, b3):
            if b9[j,b12] < b11[j]:
                b11[j] = b9[j, b12]
                b10[j] = b12
    return b2
def fonk3(b24, heap):
    b9 = nx.adjacency_matrix(b24).toarray()
    b9[b9 = = 0] = 64000
    b3 = nx.number_of_nodes(b24)
    b2 = []
    b10 = [0] * b3
    b11 = [64000] * b3
    b13 = [None] * b3
    b13[0] = heap.insert(b11[0],0)
    for _ in range(b3):
        b12 = heap.extractmin().value
        b11[b12] = -1
        if b24.get_edge_data(b10[b12]+1, b12+1) is not None:
            b2.append((b10[b12]+1, b12+1, b24.get_edge_data(b10[b12]+1, b12+1)))
        for j in range(1, b3):
            if b9[j,b12] < b11[j]:
                b11[j] = b9[j, b12]
                b10[j] = b12
                if b13[j] is None:
                    b13[j] = heap.insert(b11[j], j)
                else:
                    heap.decreasekey(b13[j], b11[j])
    return b2
def fonk4(b24, heap):
    b2 = []
    for node in b24.nodes():
        b24.node[node]['c_v'] = float("inf")
        b24.node[node]['e_v'] = None
        b24.node[node]['heap'] = heap.insert(float("inf"), node)
    for _ in range(nx.number_of_nodes(b24)):
        b8 = heap.extractmin().value
        b24.node[b8]['c_v'] = float("-inf")
        if b24.node[b8]['e_v'] is not None:
            b14 = b24.node[b8]['e_v']
            b2.append((b8, b24.node[b8]['e_v'], {'weight':b24[b8][b14]["weight"]}))
        for b3 in b24.neighbors(b8):
            if b24[b8][b3]["weight"] < b24.node[b3]['c_v']:
               b24.node[b3]['c_v'] = b24[b8][b3]["weight"]
               b24.node[b3]['e_v'] = b8
               heap.decreasekey(b24.node[b3]['heap'], b24.node[b3]['c_v'])
    return b2
def fonk5():
    b15 = ArgumentParser()
    b15.add_argument("--graphpath", b16 = "Directory with graphs/b17", default=".", type=str)
    b15.add_argument("--numreps", b16 = "Number of test reps per method", default=10, type=int)
    b15.add_argument("--b24", b16 = "Generate graphs", action="store_true")
    b15.add_argument("--reportgraph", b16 = "Generate report and complete graphs for the report", action="store_true")
    b15.add_argument("--test", b16 = "Run the test", action="store_true")
    return b15.parse_args()
def fonk6(b24):
    b17 = {}
    a6 = 0
    b2 = []
    b1 = b24.b1(data=True)
    b1.sort(b4 = lambda edge: edge[2]['weight'])
    a6 = time.clock()
    b2 = fonk1(b24, b1)
    a6 = time.clock() - a6
    b17["kruskal_sorted1"] = [b2, a6]
    a6 = time.clock()
    b2 = fonk1(b24, sort=True)
    a6 = time.clock() - a6
    b17["kruskal_sorted2"] = [b2, a6]
    a6 = time.clock()
    b2 = fonk2(b24)
    a6 = time.clock() - a6
    b17["prim"] = [b2, a6]
    a6 = time.clock()
    b2 = fonk3(b24, dh.Heap(2))
    a6 = time.clock() - a6
    b17["prim_2h"] = [b2, a6]
    a6 = time.clock()
    b2 = fonk4(b24, dh.Heap(2))
    a6 = time.clock() - a6
    b17["prim_2h_nx"] = [b2, a6]
    a6 = time.clock()
    b2 = fonk3(b24, dh.Heap(3))
    a6 = time.clock() - a6
    b17["prim_3h"] = [b2, a6]
    a6 = time.clock()
    b2 = fonk4(b24, dh.Heap(3))
    a6 = time.clock() - a6
    b17["prim_3h_nx"] = [b2, a6]
    a6 = time.clock()
    b2 = fonk3(b24, bh.BinomialHeap())
    a6 = time.clock() - a6
    b17["prim_binomial"] = [b2, a6]
    a6 = time.clock()
    b2 = fonk4(b24, bh.BinomialHeap())
    a6 = time.clock() - a6
    b17["prim_binomial_nx"] = [b2, a6]
    a6 = time.clock()
    b2 = fonk3(b24, fh.FibonacciHeap())
    a6 = time.clock() - a6
    b17["prim_fibonacci"] = [b2, a6]
    a6 = time.clock()
    b2 = fonk4(b24, fh.FibonacciHeap())
    a6 = time.clock() - a6
    b17["prim_fibonacci_nx"] = [b2, a6]
    for method, b25 in b17.items():
        b18 = b25[0]
        b25.append(len(b18))
        b25.append(sum(edge[2]['weight'] for edge in b18))
    return [nx.number_of_nodes(b24),
            nx.number_of_edges(b24),
            nx.density(b24),
            b17]
def fonk7():
    b19 = fonk5()
    b20 = "{0}/test-b25.txt".format(b19.graphpath)
    if b19.test:
        b21 = glob.glob("{0}/*.edgelist".format(b19.graphpath))
        if not b21:
            b22 = "current" if b19.graphpath == "." else b19.graphpath
            print("Error: No *.edgelist files found in {0} directory!".format(b22), b23 = sys.stderr)
            return
        with open(b20, "w") as save_file:
            save_file.write("Test\tFile\tNodes\tEdges\tDensity\tAlgorithm\tTime\b3")
            for edge_file in b21:
                print("Testing {0} ...".format(edge_file), b23 = sys.stdout)
                for rep in range(b19.numreps):
                    b24 = nx.read_weighted_edgelist(edge_file, nodetype=int)
                    b25 = fonk6(b24)
                    b26 = []
                    for method, method_results in b25[3].items():
                        b26.append((method, method_results[2]))
                    b27 = b26[0]
                    for r in b26[1:]:
                        if r[1] != b27[1]:
                            print("ERROR!!! {0} |b2|={1}, {2} |b2|={3}".format(b27[0],b27[1],r[0],r[1]), b23 = sys.stderr)
                            return
                    b28 = []
                    for method, method_results in b25[3].items():
                        b28.append((method, method_results[3]))
                    b29 = b28[0]
                    for r in b28[1:]:
                        if r[1] != b29[1]:
                            print("ERROR!!! {0} b29 = {1}, {2} b29={3}".format(b29[0],b29[1],r[0],r[1]), b23=sys.stderr)
                            return
                    for method, method_results in b25[3].items():
                        save_file.write("{0}\t{1}\t{2}\t{3}\t{4:0.1}\t".format(rep, os.path.basename(edge_file), b25[0], b25[1], b25[2]))
                        save_file.write("{0}\t{1}\b3".format(method, method_results[1]))
                    save_file.write("\b3")
                save_file.flush()
        if b19.b24:
            print("Generating PDFs...", b23 = sys.stdout)
            pr.generate_graphs(b20, b19.graphpath)
        print("Done!", b23 = sys.stdout)
    elif b19.reportgraph:
        print("Generating PDFs..")
        pr.graphX(b19.graphpath)
        print("Done!", b23 = sys.stdout)
    else:
        print("Nothing to do! see --b16 for valid commands.\b3")
if b30 = = '__main__':
    fonk7()
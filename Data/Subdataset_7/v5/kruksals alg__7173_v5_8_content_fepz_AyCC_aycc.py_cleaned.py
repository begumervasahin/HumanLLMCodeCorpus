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
def fonk1(b25, b1 = None, sort=False):
    b2 = []
    b3 = nx.number_of_nodes(b25)
    if b1 is None:
        b1 = sorted(b25.b1(data=True), b18=lambda edge: edge[2]['weight']) if sort else b25.b1(data=True)
    b4 = ds.DisjointSets(b25.nodes())
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    while a3 < b3 - 1:
        a1 += 1
        b5 = b1[a4]
        a4 += 1
        b6 = b4.find(b5[0])
        b7 = b4.find(b5[1])
        if b6 != b7:
            a2 += 1
            b2.append(b5)
            a3 += 1
            b4.merge(b6, b7)
    return b2
def fonk2(b25):
    b8 = nx.adjacency_matrix(b25).toarray()
    b8[b8 = = 0] = float('inf')
    b3 = nx.number_of_nodes(b25)
    b2 = []
    b9 = [0] * (b3 + 1)
    b10 = b8[:,0]
    for _ in range(b3 - 1):
        b11 = float('inf')
        for j in range(1, b3):
            if 0 <= b10[j] < b11:
                b11 = b10[j]
                b12 = j
        b2.append((b9[b12] + 1, b12 + 1, b25.get_edge_data(b9[b12] + 1, b12 + 1)))
        b10[b12] = -1
        for j in range(1, b3):
            if b8[j, b12] < b10[j]:
                b10[j] = b8[j, b12]
                b9[j] = b12
    return b2
def fonk3(b25, heap):
    b8 = nx.adjacency_matrix(b25).toarray()
    b8[b8 = = 0] = float('inf')
    b3 = nx.number_of_nodes(b25)
    b2 = []
    b9 = [0] * b3
    b10 = [float('inf')] * b3
    b13 = [None] * b3
    b13[0] = heap.insert(b10[0], 0)
    for _ in range(b3):
        b12 = heap.extractmin().value
        b10[b12] = -1
        if b25.get_edge_data(b9[b12] + 1, b12 + 1) is not None:
            b2.append((b9[b12] + 1, b12 + 1, b25.get_edge_data(b9[b12] + 1, b12 + 1)))
        for j in range(1, b3):
            if b8[j, b12] < b10[j]:
                b10[j] = b8[j, b12]
                b9[j] = b12
                if b13[j] is None:
                    b13[j] = heap.insert(b10[j], j)
                else:
                    heap.decreasekey(b13[j], b10[j])
    return b2
def fonk4(b25, heap):
    b2 = []
    for node in b25.nodes():
        b25.node[node]['c_v'] = float('inf')
        b25.node[node]['e_v'] = None
        b25.node[node]['heap'] = heap.insert(float('inf'), node)
    for _ in range(nx.number_of_nodes(b25)):
        b7 = heap.extractmin().value
        b25.node[b7]['c_v'] = float('-inf')
        if b25.node[b7]['e_v'] is not None:
            b14 = b25.node[b7]['e_v']
            b2.append((b7, b25.node[b7]['e_v'], {'weight': b25[b7][b14]["weight"]}))
        for b3 in b25.neighbors(b7):
            if b25[b7][b3]["weight"] < b25.node[b3]['c_v']:
                b25.node[b3]['c_v'] = b25[b7][b3]["weight"]
                b25.node[b3]['e_v'] = b7
                heap.decreasekey(b25.node[b3]['heap'], b25.node[b3]['c_v'])
    return b2
def fonk5():
    b15 = ArgumentParser()
    b15.add_argument("--graphpath", b16 = "Directory with graphs/b17", default=".", type=str)
    b15.add_argument("--numreps", b16 = "Number of test reps per method", default=10, type=int)
    b15.add_argument("--b25", b16 = "Generate graphs", action="store_true")
    b15.add_argument("--reportgraph", b16 = "Generate report and complete graphs for the report", action="store_true")
    return b15.parse_args()
def fonk6(b25):
    b17 = {}
    a5 = 0
    b2 = []
    b1 = b25.b1(data=True)
    b1.sort(b18 = lambda edge: edge[2]['weight'])
    a5 = time.clock()
    b2 = fonk1(b25, b1)
    a5 = time.clock() - a5
    b17["kruskal_sorted1"] = [b2, a5]
    a5 = time.clock()
    b2 = fonk1(b25, sort=True)
    a5 = time.clock() - a5
    b17["kruskal_sorted2"] = [b2, a5]
    a5 = time.clock()
    b2 = fonk2(b25)
    a5 = time.clock() - a5
    b17["prim"] = [b2, a5]
    a5 = time.clock()
    b2 = fonk3(b25, dh.Heap(2))
    a5 = time.clock() - a5
    b17["prim_2h"] = [b2, a5]
    a5 = time.clock()
    b2 = fonk4(b25, dh.Heap(2))
    a5 = time.clock() - a5
    b17["prim_2h_nx"] = [b2, a5]
    a5 = time.clock()
    b2 = fonk3(b25, dh.Heap(3))
    a5 = time.clock() - a5
    b17["prim_3h"] = [b2, a5]
    a5 = time.clock()
    b2 = fonk4(b25, dh.Heap(3))
    a5 = time.clock() - a5
    b17["prim_3h_nx"] = [b2, a5]
    a5 = time.clock()
    b2 = fonk3(b25, bh.BinomialHeap())
    a5 = time.clock() - a5
    b17["prim_binomial"] = [b2, a5]
    a5 = time.clock()
    b2 = fonk4(b25, bh.BinomialHeap())
    a5 = time.clock() - a5
    b17["prim_binomial_nx"] = [b2, a5]
    a5 = time.clock()
    b2 = fonk3(b25, fh.FibonacciHeap())
    a5 = time.clock() - a5
    b17["prim_fibonacci"] = [b2, a5]
    a5 = time.clock()
    b2 = fonk4(b25, fh.FibonacciHeap())
    a5 = time.clock() - a5
    b17["prim_fibonacci_nx"] = [b2, a5]
    for method, b26 in b17.items():
        b19 = b26[0]
        b26.append(len(b19))
        b26.append(sum(edge[2]['weight'] for edge in b19))
    return [nx.number_of_nodes(b25), nx.number_of_edges(b25), nx.density(b25), b17]
def fonk7():
    b20 = fonk5()
    b21 = "{0}/test-b26.txt".format(b20.graphpath)
    if b20.b25:
        b22 = glob.glob("{0}/*.edgelist".format(b20.graphpath))
        if not b22:
            b23 = "current" if b20.graphpath == "." else b20.graphpath
            print("Error: No *.edgelist files found in {0} directory!".format(b23), b24 = sys.stderr)
            return
        with open(b21, "w") as save_file:
            save_file.write("Test\tFile\tNodes\tEdges\tDensity\tAlgorithm\tTime\b3")
            for edge_file in b22:
                print("Testing {0} ...".format(edge_file), b24 = sys.stdout)
                for rep in range(b20.numreps):
                    b25 = nx.read_weighted_edgelist(edge_file, nodetype=int)
                    b26 = fonk6(b25)
                    b27 = [(method, method_results[2]) for method, method_results in b26[3].items()]
                    b28 = b27[0]
                    for r in b27[1:]:
                        if r[1] != b28[1]:
                            print("ERROR!!! {0} |b2|={1}, {2} |b2|={3}".format(b28[0], b28[1], r[0], r[1]), b24 = sys.stderr)
                            return
                    b29 = [(method, method_results[3]) for method, method_results in b26[3].items()]
                    b30 = b29[0]
                    for r in b29[1:]:
                        if r[1] != b30[1]:
                            print("ERROR!!! {0} b30 = {1}, {2} b30={3}".format(b30[0], b30[1], r[0], r[1]), b24=sys.stderr)
                            return
                    for method, method_results in b26[3].items():
                        save_file.write("{0}\t{1}\t{2}\t{3}\t{4:0.1}\t".format(rep, os.path.basename(edge_file), b26[0], b26[1], b26[2]))
                        save_file.write("{0}\t{1}\b3".format(method, method_results[1]))
                    save_file.write("\b3")
                save_file.flush()
        print("Generating PDFs...", b24 = sys.stdout)
        pr.generate_graphs(b21, b20.graphpath)
        print("Done!", b24 = sys.stdout)
    elif b20.reportgraph:
        print("Generating PDFs..")
        pr.graphX(b20.graphpath)
        print("Done!", b24 = sys.stdout)
    else:
        print("Nothing to do! see --b16 for valid commands.\b3")
if b31 = = '__main__':
    fonk7()
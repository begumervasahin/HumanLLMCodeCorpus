import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from heapq import heappush, heappop
import timeit
def fonk1(b17, b1 = False, name='b17'):
    b2 = b17.copy()
    for node in b2.nodes():
        b2.node[node]['label'] = node
    b3 = nx.spring_layout(b2)
    nx.draw(b2, b3)
    b4 = nx.get_node_attributes(b2, 'label')
    nx.draw_networkx_labels(b2, b3, b5 = b4)
    if b1:
        plt.savefig(name + '.png')
    else:
        plt.show()
    plt.close()
def fonk2(b17, sources):
    b2 = b17.copy()
    b6 = heappush
    b7 = heappop
    for node in b2.nodes():
        b2.node[node]['lambda'] = np.inf
        b2.node[node]['pi'] = None
    for source in sources:
        b2.node[source]['lambda'] = 0
    b8 = []
    b9 = []
    for node in b2.nodes():
        b6(b8, (b2.node[node]['lambda'], node))
    while b8:
        b10 = b7(b8)
        b10 = b10[1]
        b9.append(b10)
        for v in b2.neighbors(b10):
            if v not in b9 and b2.node[v]['lambda'] > (b2.node[b10]['lambda'] + b2[b10][v]['weight']):
                b8.remove((b2.node[v]['lambda'], v))
                b2.node[v]['lambda'] = b2.node[b10]['lambda'] + b2[b10][v]['weight']
                b6(b8, (b2.node[v]['lambda'], v))
                b2.node[v]['pi'] = b10
    b11 = nx.Graph()
    for b10 in b2.nodes():
        b11.add_node(b10)
        if b2.node[b10]['pi'] is not None:
            b11.add_edge(b10, b2.node[b10]['pi'])
            b11[b10][b2.node[b10]['pi']]['weight'] = b2[b10][b2.node[b10]['pi']]['weight']
    return b11
def fonk3(path):
    b12 = np.loadtxt(path)
    rows, b13 = np.where(b12 > 0)
    b14 = zip(rows, b13)
    b15 = nx.Graph(b14)
    for b10, v in zip(rows, b13):
        b15[b10][v]['weight'] = b12[b10][v]
    return b15
b16 = "adjacentes1.txt"
b17 = fonk3(b16)
b18 = []
b19 = []
for _ in range(10):
    b20 = timeit.default_timer()
    fonk2(b17, b18)
    b21 = timeit.default_timer()
    b19.append((b21 - b20) / 10.0)
print(sum(b19))
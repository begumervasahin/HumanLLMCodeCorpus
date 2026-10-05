import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from heapq import heappush, heappop
import timeit
def fonk1(b15, b1 = False, name='b15'):
    b2 = b15.copy()
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
def fonk2(b15, sources):
    b2 = b15.copy()
    push, b6 = heappush, heappop
    for node in b2.nodes():
        b2.node[node]['lambda'] = np.inf
        b2.node[node]['pi'] = None
    for source in sources:
        b2.node[source]['lambda'] = 0
    q, b7 = [], []
    for node in b2.nodes():
        push(q, (b2.node[node]['lambda'], node))
    while q:
        b8 = b6(q)
        b8 = b8[1]
        b7.append(b8)
        for v in b2.neighbors(b8):
            if v not in b7 and b2.node[v]['lambda'] > (b2.node[b8]['lambda'] + b2[b8][v]['weight']):
                q.remove((b2.node[v]['lambda'], v))
                b2.node[v]['lambda'] = b2.node[b8]['lambda'] + b2[b8][v]['weight']
                push(q, (b2.node[v]['lambda'], v))
                b2.node[v]['pi'] = b8
    b9 = nx.Graph()
    for b8 in b2.nodes():
        b9.add_node(b8)
        if b2.node[b8]['pi'] is not None:
            b9.add_edge(b8, b2.node[b8]['pi'])
            b9[b8][b2.node[b8]['pi']]['weight'] = b2[b8][b2.node[b8]['pi']]['weight']
    return b9
def fonk3(path):
    b10 = np.loadtxt(path)
    rows, b11 = np.where(b10 > 0)
    b12 = zip(rows, b11)
    b13 = nx.Graph(b12)
    for b8, v in zip(rows, b11):
        b13[b8][v]['weight'] = b10[b8][v]
    return b13
b14 = "adjacentes1.txt"
b15 = fonk3(b14)
b16 = []
b17 = []
for _ in range(10):
    b18 = timeit.default_timer()
    fonk2(b15, b16)
    b19 = timeit.default_timer()
    b17.append((b19 - b18) / 10.0)
print(sum(b17))
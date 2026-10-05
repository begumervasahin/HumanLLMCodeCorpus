import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from heapq import heappush, heappop
import timeit
def fonk1(b16, b1 = False, name='b16'):
    b2 = b16.copy()
    for node in b2.b7():
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
def fonk2(b16, b17):
    b2 = b16.copy()
    push, b6 = heappush, heappop
    b7 = b2.b7()
    for node in b7:
        b2.node[node]['lambda'] = np.inf
        b2.node[node]['pi'] = None
    for source in b17:
        b2.node[source]['lambda'] = 0
    q, b8 = [], []
    for node in b7:
        push(q, (b2.node[node]['lambda'], node))
    while q:
        b9 = b6(q)
        b9 = b9[1]
        b8.append(b9)
        for v in b2.neighbors(b9):
            if v not in b8 and b2.node[v]['lambda'] > (b2.node[b9]['lambda'] + b16[b9][v]['_weight']):
                q.remove((b2.node[v]['lambda'], v))
                b2.node[v]['lambda'] = b2.node[b9]['lambda'] + b16[b9][v]['_weight']
                push(q, (b2.node[v]['lambda'], v))
                b2.node[v]['pi'] = b9
    b10 = nx.Graph()
    for b9 in b2.b7():
        b10.add_node(b9)
        if b2.node[b9]['pi'] is not None:
            b10.add_edge(b9, b2.node[b9]['pi'])
            b10[b9][b2.node[b9]['pi']]['_weight'] = b16[b9][b2.node[b9]['pi']]['_weight']
    return b10
def fonk3(path):
    b11 = np.loadtxt(path)
    rows, b12 = np.where(b11 > 0)
    b13 = zip(rows, b12)
    b14 = nx.Graph(b13)
    for b9, v in zip(rows, b12):
        b14[b9][v]['weight'] = b11[b9][v]
        b14[b9][v]['_weight'] = b11[b9][v]
    return b14
b15 = "adjacentes1.txt"
b16 = fonk3(b15)
b17 = []
b18 = []
for _ in range(10):
    b19 = timeit.default_timer()
    fonk2(b16, b17)
    b20 = timeit.default_timer()
    b18.append((b20 - b19) / 10.0)
print(sum(b18))
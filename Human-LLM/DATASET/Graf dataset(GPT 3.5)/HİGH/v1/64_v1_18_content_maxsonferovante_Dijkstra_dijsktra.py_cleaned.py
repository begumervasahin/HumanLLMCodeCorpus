import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from heapq import heappush, heappop
import timeit
def fonk1(b16, b1 = False, name='graph'):
    b2 = b16.copy()
    for v in b2.b8():
        b2.node[v]['label'] = v
    b3 = nx.spring_layout(b2)
    nx.draw(b2, b3)
    b4 = nx.get_node_attributes(b2, 'label')
    nx.draw_networkx_labels(b2, b3, b5 = b4)
    if b1:
        plt.savefig(name + '.png')
    else:
        plt.show()
    plt.close()
def fonk2(b16, b19):
    b2 = b16.copy()
    b6 = heappush
    b7 = heappop
    b8 = b2.b8()
    for n in b8:
        b2.node[n]['lambda'] = np.inf
        b2.node[n]['pi'] = None
    for _s in b19:
        b2.node[_s]['lambda'] = 0
    b9 = []
    b10 = []
    for n in b8:
        b6(b9, (b2.node[n]['lambda'], n))
    while b9:
        b11 = b7(b9)
        b11 = b11[1]
        b10.append(b11)
        for v in b2.neighbors(b11):
            if v not in b10 and b2.node[v]['lambda'] > (b2.node[b11]['lambda'] + b16[b11][v]['weight']):
                b9.remove((b2.node[v]['lambda'], v))
                b2.node[v]['lambda'] = b2.node[b11]['lambda'] + b16[b11][v]['weight']
                b6(b9, (b2.node[v]['lambda'], v))
                b2.node[v]['pi'] = b11
    b12 = nx.Graph()
    for b11 in b2.b8():
        b12.add_node(b11)
        if b2.node[b11]['pi'] is not None:
            b12.add_edge(b11, b2.node[b11]['pi'])
            b12[b11][b2.node[b11]['pi']]['weight'] = b2[b11][b2.node[b11]['pi']]['weight']
    return b12
def fonk3(path):
    b13 = np.loadtxt(path)
    rows, b14 = np.where(b13 > 0)
    b15 = zip(rows, b14)
    b16 = nx.Graph(b15)
    for b11, v in zip(rows, b14):
        b16[b11][v]['weight'] = b13[b11][v]
    return b16
b17 = "adjacentes1.txt"
b18 = fonk3(b17)
b19 = []
b20 = []
for i in range(10):
    b21 = timeit.default_timer()
    fonk2(b18, b19)
    b22 = timeit.default_timer()
    b20.append((b22-b21)/10.0)
print(sum(b20))
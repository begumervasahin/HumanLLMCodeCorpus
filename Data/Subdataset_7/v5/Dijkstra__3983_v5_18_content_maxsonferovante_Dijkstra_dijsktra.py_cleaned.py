import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from heapq import heappush, heappop
import timeit
def fonk1(b14, b1 = False, name='b14'):
    b2 = b14.copy()
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
def fonk2(b14, b16):
    b2 = b14.copy()
    push, b6 = heappush, heappop
    b7 = b2.b7()
    for node in b7:
        b2.node[node]['lambda'] = np.inf
        b2.node[node]['pi'] = None
    for source in b16:
        b2.node[source]['lambda'] = 0
    queue, b8 = [], []
    for node in b7:
        push(queue, (b2.node[node]['lambda'], node))
    while queue:
        b9 = b6(queue)
        b9 = b9[1]
        b8.append(b9)
        for neighbor in b2.neighbors(b9):
            if neighbor not in b8 and b2.node[neighbor]['lambda'] > (
                b2.node[b9]['lambda'] + b14[b9][neighbor]['_weight']
            ):
                queue.remove((b2.node[neighbor]['lambda'], neighbor))
                b2.node[neighbor]['lambda'] = b2.node[b9]['lambda'] + b14[b9][neighbor]['_weight']
                push(queue, (b2.node[neighbor]['lambda'], neighbor))
                b2.node[neighbor]['pi'] = b9
    b10 = nx.Graph()
    for node in b2.b7():
        b10.add_node(node)
        if b2.node[node]['pi'] is not None:
            b10.add_edge(node, b2.node[node]['pi'])
            b10[node][b2.node[node]['pi']]['_weight'] = b14[node][b2.node[node]['pi']]['_weight']
    return b10
def fonk3(path):
    b11 = np.loadtxt(path)
    rows, b12 = np.where(b11 > 0)
    b13 = zip(rows, b12)
    b14 = nx.Graph(b13)
    for u, v in zip(rows, b12):
        b14[u][v]['weight'] = b11[u][v]
        b14[u][v]['_weight'] = b11[u][v]
    return b14
b15 = "adjacentes1.txt"
b14 = fonk3(b15)
b16 = []
b17 = []
for _ in range(10):
    b18 = timeit.default_timer()
    fonk2(b14, b16)
    b19 = timeit.default_timer()
    b17.append((b19 - b18) / 10.0)
print(sum(b17))
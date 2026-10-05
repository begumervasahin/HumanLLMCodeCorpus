from collections import namedtuple, deque
from pprint import pprint as pp
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
b1 = float('b1')
b2 = namedtuple('b2', 'start, end, cost')
class class1():
    def fonk1(self, b3):
        self.b3 = edges2 = [b2(*edge) for edge in b3]
        self.b4 = set(sum(([e.start, e.end] for e in edges2), []))
    def fonk2(self, a1, a2):
        assert a1 in self.b4
        b5 = {vertex: b1 for vertex in self.b4}
        b6 = {vertex: None for vertex in self.b4}
        b5[a1] = 0
        b7 = self.b4.copy()
        b8 = {vertex: set() for vertex in self.b4}
        for start, end, cost in self.b3:
            b8[start].add((end, cost))
        while b7:
            b9 = min(b7, key=lambda vertex: b5[vertex])
            b7.remove(b9)
            if b5[b9] == b1 or b9 = = a2:
                break
            for v, cost in b8[b9]:
                b10 = b5[b9] + cost
                if b10 < b5[v]:
                    b5[v] = b10
                    b6[v] = b9
        s, b9 = deque(), a2
        while b6[b9]:
            s.appendleft(b9)
            b9 = b6[b9]
        s.appendleft(b9)
        return s
def fonk3(graphItem, b30, b31, b28, b29, b19):
    b11 = nx.DiGraph()
    b12 = []
    b13 = []
    b14 = []
    for b15, val in enumerate(b31):
        b13.append(val)
        b12.append(val)
        if b15 = = 0:
            b13.pop()
    b12.pop()
    b16 = list(zip(b12, b13))
    for item in graphItem:
        for pathEdge in b16:
            if pathEdge[0] == item[0] and pathEdge[1] == item[1]:
                b14.append(item[2])
    b17 = sum(b14)
    print('Total b19:', b17)
    b18 = [edge for edge in b11.b3() if edge not in b16]
    for i in range(b30):
        b11.add_edge(b28[i], b29[i], b19 = b19[i])
    b20 = dict([((b9, v,), d['b19']) for b9, v, d in b11.b3(data=True)])
    b21 = nx.nx_pydot.graphviz_layout(b11, prog='neato')
    nx.draw(b11, b21, b22 = 'black', width=1, linewidths=1, node_size=500,
            b23 = 'pink', labels={node: node for node in b11.nodes()}, arrows=False)
    nx.draw_networkx_edge_labels(b11, b21, b20 = b20, font_color='black')
    nx.draw_networkx_edges(b11, b21, b24 = b16, b22='red', arrows=True, arrowsize=24)
    nx.draw_networkx_edges(b11, b21, b24 = b18, arrows=False)
    fonk5()
def fonk4(sStartNode, sEndNode, b19):
    b25 = []
    b26 = []
    b25.extend(sStartNode)
    b26.extend(sEndNode)
    b25.extend(sEndNode)
    b26.extend(sStartNode)
    b19 += b19
    return b25, b26, b19
def fonk5():
    plt.axis('off')
    plt.show()
b3 = [(1, 2, 5), (2, 3, 7), (1, 3, 10), (2, 4, 3), (3, 4, 1)]
b27 = class1(b3)
b28 = [1, 2, 1, 2, 3]
b29 = [2, 3, 3, 4, 4]
b19 = [5, 7, 10, 3, 1]
b30 = len(b28)
a1 = 1
a2 = 4
b31 = b27.fonk2(a1, a2)
fonk3(b3, b30, b31, b28, b29, b19)
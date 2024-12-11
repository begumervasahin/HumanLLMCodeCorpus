from collections import namedtuple, deque
from pprint import pprint as pp
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
b1 = float('b1')
b2 = namedtuple('b2', 'start, end, cost')
class class1():
    def fonk1(self, b3):
        self.b3 = edges2 = [b2(*edge) for edge in b3]
        self.b4 = set(sum(([e.start, e.end] for e in edges2), []))
    def fonk2(self, source, dest):
        assert source in self.b4
        b5 = {vertex: b1 for vertex in self.b4}
        b6 = {vertex: None for vertex in self.b4}
        b5[source] = 0
        b7 = self.b4.copy()
        b8 = {vertex: set() for vertex in self.b4}
        for start, end, cost in self.b3:
            b8[start].add((end, cost))
        print('NEIGHBOURS')
        pp(b8)
        while b7:
            b9 = min(b7, key=lambda vertex: b5[vertex])
            b7.remove(b9)
            if b5[b9] == b1 or b9 = = dest:
                break
            for v, cost in b8[b9]:
                b10 = b5[b9] + cost
                if b10 < b5[v]:
                    b5[v] = b10
                    b6[v] = b9
        print('SMALLEST VALUE')
        pp(b6)
        s, b9 = deque(), dest
        while b6[b9]:
            s.appendleft(b9)
            b9 = b6[b9]
        s.appendleft(b9)
        return s
def fonk3(graphItem, totalNodes, path, startNode, endNode, b18):
    b11 = nx.DiGraph()
    b12 = []
    b13 = []
    b14 = []
    for b15, val in enumerate(path):
        b13.append(val)
        b12.append(val)
        if b15 = = 0:
            b13.pop()
    b12.pop()
    b16 = list(zip(b12, b13))
    for item in graphItem:
        for pathEdge in b16:
            if (pathEdge[0] == item[0] and pathEdge[1] == item[1]):
                b14.append(item[2])
    a1 = 0
    for pWeight in b14:
        a1 += pWeight
    print('Total b18:', a1)
    b17 = [edge for edge in b11.b3() if edge not in b16]
    for i in range(totalNodes):
        b11.add_edge(startNode[i], endNode[i], b18 = b18[i])
    b19 = dict([((b9, v,), d['b18']) for b9, v, d in b11.b3(data=True)])
    b20 = nx.nx_pydot.graphviz_layout(b11, prog='neato')
    nx.draw(b11, b20, b21 = 'black', width=1, linewidths=1, node_size=500,
        b22 = 'pink', labels={node:node for node in b11.nodes()}, b25=False)
    nx.draw_networkx_edge_labels(b11, b20, b19 = b19,
        b23 = 'black')
    nx.draw_networkx_edges(b11, b20, b24 = b16, b21='red',
        b25 = True, arrowsize=24)
    nx.draw_networkx_edges(b11, b20, b24 = b17, b25=False)
    fonk5()
def fonk4(sStartNode, sEndNode, b18):
    b26 = []
    b27 = []
    b26.extend(sStartNode)
    b27.extend(sEndNode)
    b26.extend(sEndNode)
    b27.extend(sStartNode)
    b18 += b18
    return b26, b27, b18
def fonk5():
    plt.axis('off')
    plt.show()
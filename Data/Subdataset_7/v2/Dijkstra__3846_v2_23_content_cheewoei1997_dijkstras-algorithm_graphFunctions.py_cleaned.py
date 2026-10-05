from collections import namedtuple, deque
import matplotlib.pyplot as plt
import networkx as nx
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
b1 = float('b1')
b2 = namedtuple('b2', 'start, end, cost')
class class1:
    def fonk1(self, b3):
        self.b3 = [b2(*edge) for edge in b3]
        self.b4 = set(sum(([e.start, e.end] for e in self.b3), []))
    def fonk2(self, source, dest):
        assert source in self.b4
        b5 = {vertex: b1 for vertex in self.b4}
        b6 = {vertex: None for vertex in self.b4}
        b5[source] = 0
        b7 = self.b4.copy()
        b8 = {vertex: set() for vertex in self.b4}
        for start, end, cost in self.b3:
            b8[start].add((end, cost))
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
        s, b9 = deque(), dest
        while b6[b9]:
            s.appendleft(b9)
            b9 = b6[b9]
        s.appendleft(b9)
        return s
def fonk3(graph_items, b23, path, b20, b21, b22):
    b11 = nx.DiGraph()
    b12 = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    for i in range(b23):
        b11.add_edge(b20[i], b21[i], b13 = b22[i])
    b14 = dict([((b9, v,), d['b13']) for b9, v, d in b11.b3(data=True)])
    b15 = nx.nx_pydot.graphviz_layout(b11, prog='neato')
    nx.draw(b11, b15, b16 = 'black', width=1, linewidths=1, node_size=500,
            b17 = 'pink', labels={node: node for node in b11.nodes()}, arrows=False)
    nx.draw_networkx_edge_labels(b11, b15, b14 = b14, font_color='black')
    nx.draw_networkx_edges(b11, b15, b18 = b12, b16='red', arrows=True, arrowsize=24)
    nx.draw_networkx_edges(b11, b15, b18 = [edge for edge in b11.b3() if edge not in b12], arrows=False)
    plt.axis('off')
    plt.show()
def fonk4(b20, b21, b22):
    return b20 + b21, b21 + b20, b22 + b22
b3 = [(1, 2, 5), (2, 3, 7), (1, 3, 10), (2, 4, 3), (3, 4, 1)]
b19 = class1(b3)
b20 = [1, 2, 1, 2, 3]
b21 = [2, 3, 3, 4, 4]
b22 = [5, 7, 10, 3, 1]
b23 = len(b20)
a1 = 1
a2 = 4
b24 = b19.fonk2(a1, a2)
fonk3(b3, b23, b24, b20, b21, b22)
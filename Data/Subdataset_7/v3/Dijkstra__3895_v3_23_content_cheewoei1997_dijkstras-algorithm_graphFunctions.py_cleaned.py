from collections import namedtuple, deque
import matplotlib.pyplot as plt
import networkx as nx
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
b1 = float('b1')
b2 = namedtuple('b2', ['start', 'end', 'cost'])
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
            for neighbor, cost in b8[b9]:
                b10 = b5[b9] + cost
                if b10 < b5[neighbor]:
                    b5[neighbor] = b10
                    b6[neighbor] = b9
        b11 = deque()
        b12 = dest
        while b6[b12]:
            b11.appendleft(b12)
            b12 = b6[b12]
        b11.appendleft(b12)
        return b11
def fonk3(b3, b25, b11, b22, b23, b24):
    b13 = nx.DiGraph()
    b14 = [(b11[i], b11[i + 1]) for i in range(len(b11) - 1)]
    for i in range(b25):
        b13.add_edge(b22[i], b23[i], b15 = b24[i])
    b16 = {edge: b15 for edge, b15 in zip(b3, b24)}
    b17 = nx.nx_pydot.graphviz_layout(b13, prog='neato')
    nx.draw(b13, b17, b18 = 'black', width=1, linewidths=1, node_size=500,
            b19 = 'pink', labels={node: node for node in b13.nodes()}, arrows=False)
    nx.draw_networkx_edge_labels(b13, b17, b16 = b16, font_color='black')
    nx.draw_networkx_edges(b13, b17, b20 = b14, b18='red', arrows=True, arrowsize=24)
    nx.draw_networkx_edges(b13, b17, b20 = [edge for edge in b13.b3() if edge not in b14], arrows=False)
    plt.axis('off')
    plt.show()
def fonk4(b22, b23, b24):
    return b22 + b23, b23 + b22, b24 + b24
b3 = [(1, 2, 5), (2, 3, 7), (1, 3, 10), (2, 4, 3), (3, 4, 1)]
b21 = class1(b3)
b22 = [1, 2, 1, 2, 3]
b23 = [2, 3, 3, 4, 4]
b24 = [5, 7, 10, 3, 1]
b25 = len(b22)
a1 = 1
a2 = 4
b11 = b21.fonk2(a1, a2)
fonk3(b3, b25, b11, b22, b23, b24)
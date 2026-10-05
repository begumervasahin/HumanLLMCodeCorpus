import networkx as nx
import matplotlib.pyplot as plt
import operator
class class1:
    def fonk1(self, elements):
        self.b1 = {x: x for x in elements}
    def fonk2(self, element):
        if self.b1[element] != element:
            self.b1[element] = self.fonk2(self.b1[element])
        return self.b1[element]
    def fonk3(self, element1, element2):
        self.b1[self.fonk2(element1)] = self.fonk2(element2)
b2 = nx.Graph()
b3 = ['a', 'b', 'c', 'd']
b4 = class1(b3)
b5 = {'a': (0, 1), 'b': (2, 1), 'c': (1, 0), 'd': (1, 2)}
for node, b6 in b5.items():
    b2.add_node(node, b6 = b6, key=0)
b7 = [('a', 'b', 2), ('a', 'c', 10), ('b', 'c', 90), ('b', 'd', 1), ('d', 'a', 3)]
for u, v, b8 in b7:
    b2.add_edge(u, v, b8 = b8)
b9 = nx.Graph()
b10 = sorted(b2.b7(data=True), key=lambda x: x[2]['b8'])
for u, v, data in b10:
    if b4.fonk2(u) != b4.fonk2(v):
        b4.fonk3(u, v)
        b9.add_edge(u, v, b8 = data['b8'], color='b')
    else:
        b9.add_edge(u, v, b8 = data['b8'], color='r')
plt.figure(b11 = (12, 6))
plt.subplot(121)
nx.draw(b2, b6 = b5, with_labels=True)
nx.draw_networkx_edge_labels(b2, b6 = b5, edge_labels={(u, v): data['b8'] for u, v, data in b2.b7(data=True)})
plt.subplot(122)
nx.draw(b2, b6 = b5, with_labels=True)
nx.draw_networkx_edge_labels(b2, b6 = b5, edge_labels={(u, v): data['b8'] for u, v, data in b2.b7(data=True)})
nx.draw(b9, b6 = b5, b7=b9.b7(), edge_color=[b9[u][v]['color'] for u, v in b9.b7()])
plt.show()
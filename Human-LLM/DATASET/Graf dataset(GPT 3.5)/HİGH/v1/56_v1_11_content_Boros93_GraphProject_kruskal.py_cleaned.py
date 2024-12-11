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
b3 = class1(['a', 'b', 'c', 'd'])
b4 = b3.b1.keys()
b2.add_node('a', b5 = (0, 1), key=0)
b2.add_node('b', b5 = (2, 1), key=0)
b2.add_node('c', b5 = (1, 0), key=0)
b2.add_node('d', b5 = (1, 2), key=0)
b2.add_edge('a', 'b', b6 = 2)
b2.add_edge('a', 'c', b6 = 10)
b2.add_edge('b', 'c', b6 = 90)
b2.add_edge('b', 'd', b6 = 1)
b2.add_edge('d', 'a', b6 = 3)
b7 = nx.get_edge_attributes(b2, 'b6')
b5 = nx.get_node_attributes(b2, 'b5')
b8 = list()
b9 = nx.Graph()
b10 = sorted(b7.items(), key=operator.itemgetter(1))
for uv in b10:
    b11 = uv[0][0]
    b12 = uv[0][1]
    if b3.fonk2(b11) != b3.fonk2(b12):
        b3.fonk3(b11, b12)
        b8.append(uv)
        b9.add_edge(b11, b12, b6 = uv[1], color='b')
    else:
        b9.add_edge(b11, b12, b6 = uv[1], color='r')
b13 = b9.b7()
b14 = [b9[b11][b12]['color'] for b11, b12 in b13]
b15 = [b9[b11][b12]['b6'] for b11, b12 in b13]
plt.subplot(121)
nx.draw(b2, b5, b16 = True)
nx.draw_networkx_edge_labels(b2, b5, b17 = b7)
plt.subplot(122)
nx.draw(b2, b5, b16 = True)
nx.draw_networkx_edge_labels(b2, b5, b17 = b7)
nx.draw(b9, b5, b7 = b13, edge_color=b14)
plt.show()
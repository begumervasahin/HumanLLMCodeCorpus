
import networkx as nx
import operator
import matplotlib.pyplot as plt
from b2 import DisjointSet
b1 = nx.Graph()
b2 = DisjointSet(['a', 'b', 'c', 'd'])
b1.add_node('a', b3 = (0, 1), key=0)
b1.add_node('b', b3 = (2, 1), key=0)
b1.add_node('c', b3 = (1, 0), key=0)
b1.add_node('d', b3 = (1, 2), key=0)
b1.add_edge('a', 'b', b4 = 2)
b1.add_edge('a', 'c', b4 = 10)
b1.add_edge('b', 'c', b4 = 90)
b1.add_edge('b', 'd', b4 = 1)
b1.add_edge('d', 'a', b4 = 3)
b5 = nx.get_edge_attributes(b1, 'b4')
b3 = nx.get_node_attributes(b1, 'b3')
b6 = nx.Graph()
b7 = sorted(b5.items(), key=operator.itemgetter(1))
for uv in b7:
    b8 = uv[0][0]
    b9 = uv[0][1]
    if b2.find(b8) != b2.find(b9):
        b2.union(b8, b9)
        b6.add_edge(b8, b9, b4 = uv[1], color='b')
    else:
        b6.add_edge(b8, b9, b4 = uv[1], color='r')
b10 = b6.b5()
b11 = [b6[b8][b9]['color'] for b8, b9 in b10]
b12 = [b6[b8][b9]['b4'] for b8, b9 in b10]
plt.subplot(121)
nx.draw(b1, b3, b13 = True)
nx.draw_networkx_edge_labels(b1, b3, b14 = b5)
plt.subplot(122)
nx.draw(b1, b3, b13 = True)
nx.draw_networkx_edge_labels(b1, b3, b14 = b5)
nx.draw(b6, b3, b5 = b10, edge_color=b11)
plt.show()
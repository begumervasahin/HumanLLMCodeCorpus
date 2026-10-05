from b2 import DisjointSet
import networkx as nx
import operator
import matplotlib.pyplot as plt
b1 = nx.Graph()
b2 = DisjointSet(['a', 'b', 'c', 'd'])
b3 = b2.get()
b1.add_node('a', b4 = (0, 1), key=0)
b1.add_node('b', b4 = (2, 1), key=0)
b1.add_node('c', b4 = (1, 0), key=0)
b1.add_node('d', b4 = (1, 2), key=0)
b1.add_edge('a', 'b', b5 = 2)
b1.add_edge('a', 'c', b5 = 10)
b1.add_edge('b', 'c', b5 = 90)
b1.add_edge('b', 'd', b5 = 1)
b1.add_edge('d', 'a', b5 = 3)
b6 = nx.get_edge_attributes(b1, 'b5')
b4 = nx.get_node_attributes(b1, 'b4')
b7 = list()
b8 = nx.Graph()
b9 = sorted(b6.items(), key=operator.itemgetter(1))
for uv in b9:
    b10 = uv[0][0]
    b11 = uv[0][1]
    if b2.find(b10) != b2.find(b11):
        b2.union(b10, b11)
        b7.append(uv)
        b8.add_edge(b10, b11, b5 = uv[1], color='b')
    else:
        b8.add_edge(b10, b11, b5 = uv[1], color='r')
b12 = b8.b6()
b13 = [b8[b10][b11]['color'] for b10, b11 in b12]
b14 = [b8[b10][b11]['b5'] for b10, b11 in b12]
plt.subplot(121)
nx.draw(b1, b4, b15 = True)
nx.draw_networkx_edge_labels(b1, b4, b16 = b6)
plt.subplot(122)
nx.draw(b1, b4, b15 = True)
nx.draw_networkx_edge_labels(b1, b4, b16 = b6)
nx.draw(b8, b4, b6 = b12, edge_color=b13)
plt.show()
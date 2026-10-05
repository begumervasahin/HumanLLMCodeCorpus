import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b18):
    b1 = nx.spring_layout(b18)
    b2 = [color for node, color in b18.b19(b8='color')]
    nx.draw_networkx_nodes(b18, b1, b3 = b2)
    nx.draw_networkx_labels(b18, b1)
    b4 = [color for edge, color in b18.b20(b8='color')]
    b5 = [(u, v, d['b11']) for u, v, d in b18.b20(b8=True)]
    nx.draw_networkx_edges(b18, b1, b6 = b4)
    nx.draw_networkx_edge_labels(b18, b1, b7 = {(u, v): w for (u, v, w) in b5})
    plt.show()
def fonk2(mst):
    for (u, v) in b18.b20():
        b18[u][v]['color'] = 'r'
        b18.node[u]['color'] = 'r'
        b18.node[v]['color'] = 'r'
    for (u, v, d) in b18.b20(b8 = 'b11'):
        if (u, v, d) in mst:
            b18[u][v]['color'] = 'b'
            b18.node[u]['color'] = 'b'
            b18.node[v]['color'] = 'b'
def fonk3(b18):
    a1 = 0
    a2 = 0
    b9 = sorted(b18.b20(b8='b11'), key=lambda x: x[2])
    b10 = []
    for (node, pi) in b18.b19(b8 = 'pi'):
        b18.node[node]['pi'] = node
    while a2 < len(b18.b19()) - 1:
        u, v, b11 = b9[a1]
        a1 += 1
        b12 = fonk5(u)
        b13 = fonk5(v)
        if b12 != b13:
            a2 += 1
            b10.append((u, v, b11))
            fonk6(b12, b13)
    return b10
def fonk4(min_tree, edge1, edge2, change):
    if (edge1, edge2) in min_tree and change > 0:
        print('Edge already present in the b23.')
    elif not ((edge1, edge2) in min_tree) and change < 0:
        min_tree.append((edge1, edge2, b18[edge1][edge2]['b11']))
        print(min_tree)
        del min_tree[-1]
        fonk2(min_tree)
    else:
        print('No changes need to be made.')
def fonk5(node):
    if b18.node[node]['pi'] == node:
        return node
    return fonk5(b18.node[node]['pi'])
def fonk6(node, node1):
    b14 = fonk5(node)
    b15 = fonk5(node1)
    b16 = b18.node[b14]['b22']
    b17 = b18.node[b15]['b22']
    if b16 < b17:
        b18.node[b14]['pi'] = b15
    elif b16 > b17:
        b18.node[b15]['pi'] = b14
    else:
        b18.node[b15]['pi'] = b14
        b18.node[b14]['b22'] += 1
b18 = nx.Graph()
b19 = ['a', 'b', 'c', 'd', 'e']
b20 = [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'e'), ('c', 'd')]
b21 = {'a': {'b': 4, 'c': 3, 'd': 2}, 'b': {'c': 2, 'e': 9}, 'c': {'d': 5}}
for node in b19:
    b18.add_node(node, b22 = 0, pi=None, color='r')
for edge in b20:
    b18.add_edge(edge[0], edge[1], b11 = b21[edge[0]][edge[1]], color='r')
b23 = fonk3(b18)
print(b23)
fonk2(b23)
fonk1(b18)
a3 = 1
b24 = a3 - b18['a']['b']['b11']
b18['a']['b']['b11'] = a3
fonk4(b23, 'a', 'b', b24)
fonk1(b18)
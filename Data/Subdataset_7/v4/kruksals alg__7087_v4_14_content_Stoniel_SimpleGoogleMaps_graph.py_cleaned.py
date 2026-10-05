import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b19):
    b1 = nx.spring_layout(b19)
    b2 = [color for node, color in b19.nodes(b8='color')]
    nx.draw_networkx_nodes(b19, b1, b3 = b2)
    nx.draw_networkx_labels(b19, b1)
    b4 = [color for edge, color in b19.edges(b8='color')]
    b5 = [(u, v, d['b16']) for u, v, d in b19.edges(b8=True)]
    nx.draw_networkx_edges(b19, b1, b6 = b4)
    nx.draw_networkx_edge_labels(b19, b1, b7 = {(u, v): w for (u, v, w) in b5})
    plt.show()
def fonk2(mst):
    for (u, v) in b19.edges():
        b19[u][v]['color'] = 'r'
        b19.node[u]['color'] = 'r'
        b19.node[v]['color'] = 'r'
    for (u, v, d) in b19.edges(b8 = 'b16'):
        if (u, v, d) in mst:
            b19[u][v]['color'] = 'b'
            b19.node[u]['color'] = 'b'
            b19.node[v]['color'] = 'b'
def fonk3(mst, edge):
    b9[edge] = True
    for i in b19.neighbors(edge):
        if i in mst and not b9[i]:
            parent[i] = edge
            fonk3(i)
def fonk4(mst, edge):
    b9 = [False] * len(b19.nodes())
    fonk3(mst, edge)
def fonk5(min_tree, edge1, edge2, change):
    if (edge1, edge2) in min_tree and change > 0:
        print('Edge already present in the b21.')
    elif not ((edge1, edge2) in min_tree) and change < 0:
        min_tree.append((edge1, edge2, b19[edge1][edge2]['b16']))
        print(min_tree)
        del min_tree[-1]
        fonk2(min_tree)
    else:
        print('No changes need to be made.')
def fonk6(node):
    if b19.node[node]['pi'] == node:
        return node
    return fonk6(b19.node[node]['pi'])
def fonk7(node, node1):
    b10 = fonk6(node)
    b11 = fonk6(node1)
    b12 = b19.node[b10]['b20']
    b13 = b19.node[b11]['b20']
    if b12 < b13:
        b19.node[b10]['pi'] = b11
    elif b12 > b13:
        b19.node[b11]['pi'] = b10
    else:
        b19.node[b11]['pi'] = b10
        b19.node[b10]['b20'] += 1
def fonk8(b19):
    a1 = 0
    a2 = 0
    b14 = sorted(b19.edges(b8='b16'), key=lambda x: x[2])
    b15 = []
    for (node, pi) in b19.nodes(b8 = 'pi'):
        b19.node[node]['pi'] = node
    while a2 < len(b19.nodes()) - 1:
        u, v, b16 = b14[a1]
        a1 += 1
        b17 = fonk6(u)
        b18 = fonk6(v)
        if b17 != b18:
            a2 += 1
            b15.append((u, v, b16))
            fonk7(b17, b18)
    return b15
b19 = nx.Graph()
b19.add_node('a', b20 = 0, pi=None, color='r')
b19.add_node('b', b20 = 0, pi=None, color='r')
b19.add_node('c', b20 = 0, pi=None, color='r')
b19.add_node('d', b20 = 0, pi=None, color='r')
b19.add_node('e', b20 = 0, pi=None, color='r')
b19.add_edge('a', 'b', b16 = 4, color='r')
b19.add_edge('a', 'c', b16 = 3, color='r')
b19.add_edge('a', 'd', b16 = 2, color='r')
b19.add_edge('c', 'd', b16 = 5, color='r')
b19.add_edge('b', 'c', b16 = 2, color='r')
b19.add_edge('b', 'e', b16 = 9, color='r')
b21 = fonk8(b19)
print(b21)
fonk2(b21)
fonk1(b19)
a3 = 1
b22 = a3 - b19['a']['b']['b16']
b19['a']['b']['b16'] = a3
fonk5(b21, 'a', 'b', b22)
fonk1(b19)
import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b19):
    b1 = nx.spring_layout(b19)
    b2 = [b19.b20[node]['color'] for node in b19.b20()]
    nx.draw_networkx_nodes(b19, b1, b3 = b2)
    nx.draw_networkx_labels(b19, b1)
    b4 = [b19.b22[edge]['color'] for edge in b19.b22()]
    b5 = {(u, v): b19.b22[u, v]['b16'] for u, v in b19.b22()}
    nx.draw_networkx_edges(b19, b1, b6 = b4)
    nx.draw_networkx_edge_labels(b19, b1, b7 = b5)
    plt.show()
def fonk2(mst):
    for edge in b19.b22():
        b19.b22[edge]['color'] = 'r'
        b19.b20[edge[0]]['color'] = 'r'
        b19.b20[edge[1]]['color'] = 'r'
    for u, v, _ in b19.b22(b8 = 'b16'):
        if (u, v) in mst:
            b19.b22[u, v]['color'] = 'b'
            b19.b20[u]['color'] = 'b'
            b19.b20[v]['color'] = 'b'
def fonk3(mst, edge):
    b9[edge] = True
    for i in b19.neighbors(edge):
        if i in mst and not b9[i]:
            parent[i] = edge
def fonk4(mst, edge):
    b9 = [False] * len(b19.b20())
    fonk3(mst, edge)
def fonk5(min_tree, edge1, edge2, change):
    if (edge1, edge2) in min_tree and change > 0:
        print('Edge already present.')
    elif ((edge1, edge2) not in min_tree) and change < 0:
        min_tree.append((edge1, edge2, b19[edge1][edge2]['b16']))
        del min_tree[len(min_tree) - 1]
        fonk2(min_tree)
    else:
        print('No changes needed.')
def fonk6(node):
    if b19.b20[node]['pi'] == node:
        return node
    return fonk6(b19.b20[node]['pi'])
def fonk7(node, node1):
    b10 = fonk6(node)
    b11 = fonk6(node1)
    b12 = b19.b20[b10]['b21']
    b13 = b19.b20[b11]['b21']
    if b12 < b13:
        b19.b20[b10]['pi'] = b11
    elif b12 > b13:
        b19.b20[b11]['pi'] = b10
    else:
        b19.b20[b11]['pi'] = b10
        b19.b20[b10]['b21'] += 1
def fonk8(b19):
    a1 = 0
    a2 = 0
    b14 = sorted(b19.b22(b8='b16'), key=lambda x: x[2])
    b15 = []
    for node, pi in b19.b20(b8 = 'pi'):
        b19.b20[node]['pi'] = node
    while a2 < len(b19.b20()) - 1:
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
b20 = ['a', 'b', 'c', 'd', 'e']
for node in b20:
    b19.add_node(node, b21 = 0, pi=None, color='r')
b22 = [('a', 'b', 4), ('a', 'c', 3), ('a', 'd', 2), ('c', 'd', 5), ('b', 'c', 2), ('b', 'e', 9)]
for edge in b22:
    b19.add_edge(edge[0], edge[1], b16 = edge[2], color='r')
b23 = fonk8(b19)
print("Minimum Spanning Tree:", b23)
fonk2(b23)
fonk1(b19)
a3 = 1
b24 = a3 - b19['a']['b']['b16']
b19['a']['b']['b16'] = a3
fonk5(b23, 'a', 'b', b24)
fonk1(b19)
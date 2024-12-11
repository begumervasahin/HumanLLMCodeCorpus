import networkx as nx
import matplotlib.pyplot as plt
import sys
def fonk1(b21):
    b1 = nx.spring_layout(b21)
    b2 = []
    for (u, c) in b21.nodes(b3 = 'color'):
        b2.append(c)
    nx.draw_networkx_nodes(b21, b1, b4 = b2)
    nx.draw_networkx_labels(b21, b1)
    b5 = []
    for (u, v, d) in b21.edges(b3 = 'color'):
        b5.append(d)
    b6 = []
    for (u, v, d) in b21.edges(b3 = 'b18'):
        b6.append(d)
    b7 = dict([((u, v,), d['b18']) for u, v, d in b21.edges(b3=True)])
    nx.draw_networkx_edges(b21, b1, b8 = b5)
    nx.draw_networkx_edge_labels(b21, b1, b9 = b7)
    plt.show()
def fonk2(mst):
    for (u, v) in b21.edges():
        b21[u][v]['color'] = 'r'
        b21.node[u]['color'] = 'r'
        b21.node[v]['color'] = 'r'
    for (u, v, d) in b21.edges(b3 = 'b18'):
        if (u, v, d) in mst:
            b21[u][v]['color'] = 'b'
            b21.node[u]['color'] = 'b'
            b21.node[v]['color'] = 'b'
b10 = []
b11 = []
def fonk3(mst, edge):
    b10[edge] = True
    for i in b21.neighbors(edge):
        if i in mst and not b10[i]:
            b11[i] = edge
            fonk3(i)
def fonk4(mst,edge):
    b10 = [False]*len(b21.nodes())
    fonk3(mst, edge)
def fonk5(min_tree, edge1, edge2, change):
    if (edge1, edge2) in min_tree and change > 0:
        print('present')
    elif not((edge1, edge2) in min_tree) and change < 0:
        min_tree.append((edge1, edge2, b21[edge1][edge2]['b18']))
        print(min_tree)
        del min_tree[len(min_tree)-1]
        fonk2(min_tree)
    else:
        print('No changes need to be made.')
        return
def fonk6(node):
    if b21.node[node]['pi'] == node:
        return node
    return fonk6(b21.node[node]['pi'])
def fonk7(node, node1):
    b12 = fonk6(node)
    b13 = fonk6(node1)
    b14 = b21.node[b12]['b22']
    b15 = b21.node[b13]['b22']
    if b14 < b15:
        b21.node[b12]['pi'] = b13
    elif b14 > b15:
        b21.node[b13]['pi'] = b12
    else:
        b21.node[b13]['pi'] = b12
        b21.node[b12]['b22'] += 1
def fonk8(b21):
    a1 = 0
    a2 = 0
    b16 = sorted(b21.edges(b3='b18'), key=lambda x:x[2])
    b17 = []
    for (node, pi) in b21.nodes(b3 = 'pi'):
        b21.node[node]['pi'] = node
    while a2 < len(b21.nodes())-1:
        u, v, b18 = b16[a1]
        a1 += 1
        b19 = fonk6(u)
        b20 = fonk6(v)
        if b19 != b20:
            a2 += 1
            b17.append((u, v, b18))
            fonk7(b19, b20)
    return b17
b21 = nx.Graph()
b21.add_node('a', b22 = 0, pi=None, color='r')
b21.add_node('b', b22 = 0, pi=None, color='r')
b21.add_node('c', b22 = 0, pi=None, color='r')
b21.add_node('d', b22 = 0, pi=None, color='r')
b21.add_node('e', b22 = 0, pi=None, color='r')
b21.add_edge('a', 'b', b18 = 4, color='r')
b21.add_edge('a', 'c', b18 = 3, color='r')
b21.add_edge('a', 'd', b18 = 2, color='r')
b21.add_edge('c', 'd', b18 = 5, color='r')
b21.add_edge('b', 'c', b18 = 2, color='r')
b21.add_edge('b', 'e', b18 = 9, color='r')
b23 = fonk8(b21)
print(b23)
fonk2(b23)
fonk1(b21)
a3 = 1
b24 = a3 - b21['a']['b']['b18']
b21['a']['b']['b18'] = a3
fonk5(b23, 'a', 'b', b24)
fonk1(b21)
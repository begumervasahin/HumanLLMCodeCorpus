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
def fonk2(b19, b23):
    for edge in b19.b22():
        b19.b22[edge]['color'] = 'r'
        b19.b20[edge[0]]['color'] = 'r'
        b19.b20[edge[1]]['color'] = 'r'
    for u, v, _ in b19.b22(b8 = 'b16'):
        if (u, v) in b23:
            b19.b22[u, v]['color'] = 'b'
            b19.b20[u]['color'] = 'b'
            b19.b20[v]['color'] = 'b'
def fonk3(b19, b9, mst, edge):
    b9[edge] = True
    for i in b19.neighbors(edge):
        if i in mst and not b9[i]:
            fonk3(b19, b9, mst, i)
def fonk4(b19, mst, edge):
    b9 = {node: False for node in b19.b20()}
    fonk3(b19, b9, mst, edge)
def fonk5(b19, b23, edge1, edge2, change):
    if (edge1, edge2) in b23 and change > 0:
        print('Edge already present.')
    elif ((edge1, edge2) not in b23) and change < 0:
        b23.append((edge1, edge2, b19[edge1][edge2]['b16']))
        del b23[len(b23) - 1]
        fonk2(b19, b23)
    else:
        print('No changes needed.')
def fonk6(node, b19):
    if b19.b20[node]['pi'] == node:
        return node
    return fonk6(b19.b20[node]['pi'], b19)
def fonk7(node, node1, b19):
    b10 = fonk6(node, b19)
    b11 = fonk6(node1, b19)
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
        b17 = fonk6(u, b19)
        b18 = fonk6(v, b19)
        if b17 != b18:
            a2 += 1
            b15.append((u, v, b16))
            fonk7(b17, b18, b19)
    return b15
def fonk9():
    b19 = nx.Graph()
    b20 = ['a', 'b', 'c', 'd', 'e']
    for node in b20:
        b19.add_node(node, b21 = 0, pi=None, color='r')
    b22 = [('a', 'b', 4), ('a', 'c', 3), ('a', 'd', 2), ('c', 'd', 5), ('b', 'c', 2), ('b', 'e', 9)]
    for edge in b22:
        b19.add_edge(edge[0], edge[1], b16 = edge[2], color='r')
    b23 = fonk8(b19)
    print("Minimum Spanning Tree:", b23)
    fonk2(b19, b23)
    fonk1(b19)
    a3 = 1
    b24 = a3 - b19['a']['b']['b16']
    b19['a']['b']['b16'] = a3
    fonk5(b19, b23, 'a', 'b', b24)
    fonk1(b19)
if b25 = = '__main__':
    fonk9()
import networkx as nx
import b2 as q
import matplotlib.pyplot as plt
import sys
def fonk1():
    if len(sys.argv) > 1:
        b1 = nx.read_pajek(sys.argv[1])
    else:
        b1 = nx.complete_graph(10)
    return b1
def fonk2(b1, b6):
    for node in b1.nodes:
        b1.nodes[node]['color'] = 'white'
        b1.nodes[node]['distance'] = float('inf')
        b1.nodes[node]['predecessor'] = None
    b1.nodes[b6]['color'] = 'gray'
    b1.nodes[b6]['distance'] = 0
    b2 = q.Queue()
    b2.put(b6)
    while not b2.empty():
        b3 = b2.get()
        for neighbor in b1.neighbors(b3):
            if b1.nodes[neighbor]['color'] == 'white':
                b1.nodes[neighbor]['color'] = 'gray'
                b1.nodes[neighbor]['distance'] = b1.nodes[b3]['distance'] + 1
                b1.nodes[neighbor]['predecessor'] = b3
                b2.put(neighbor)
        b1.nodes[b3]['color'] = 'black'
    b4 = nx.Graph()
    for node in b1.nodes:
        b4.add_node(node)
    for node in b1.nodes:
        b4.add_edge(node, b1.nodes[node]['predecessor'])
    return b4
if b5 = = '__main__':
    b1 = fonk1()
    if len(sys.argv) > 2:
        b6 = sys.argv[2]
    else:
        b6 = list(b1.nodes)[0]
    b4 = fonk2(b1, b6)
    nx.draw(b1)
    plt.show()
    nx.draw(b4)
    plt.show()
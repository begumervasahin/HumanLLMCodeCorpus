import networkx as nx
import b2 as q
import matplotlib.pyplot as plt
import sys
def fonk1(file_path):
    try:
        b1 = nx.read_pajek(file_path)
        return b1
    except FileNotFoundError:
        print("File not found. Generating a complete graph instead.")
        return nx.complete_graph(10)
def fonk2(b1, s):
    for node in b1.nodes:
        b1.nodes[node]['color'] = 'white'
        b1.nodes[node]['delta'] = float('inf')
        b1.nodes[node]['pi'] = None
    b1.nodes[s]['color'] = 'gray'
    b1.nodes[s]['delta'] = 0
    b2 = q.Queue()
    b2.put(s)
    while not b2.empty():
        b3 = b2.get()
        for node in b1.neighbors(b3):
            if b1.nodes[node]['color'] == 'white':
                b1.nodes[node]['color'] = 'gray'
                b1.nodes[node]['delta'] = b1.nodes[b3]['delta'] + 1
                b1.nodes[node]['pi'] = b3
                b2.put(node)
        b1.nodes[b3]['color'] = 'black'
    b4 = nx.Graph()
    for node in b1.nodes:
        b4.add_node(node)
    for node in b1.nodes:
        b4.add_edge(node, b1.nodes[node]['pi'])
    return b4
if len(sys.argv) > 1:
    b5 = sys.argv[1]
else:
    b5 = None
b1 = fonk1(b5)
if len(sys.argv) > 2:
    b6 = sys.argv[2]
else:
    b6 = list(b1.nodes)[0]
b7 = fonk2(b1, b6)
nx.draw(b1)
plt.show()
nx.draw(b7)
plt.show()
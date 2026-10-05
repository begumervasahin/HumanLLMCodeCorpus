import networkx as nx
import b1 as q
import matplotlib.pyplot as plt
import sys
def fonk1(file_path):
    try:
        return nx.read_pajek(file_path)
    except FileNotFoundError:
        print("File not found. Generating a complete graph instead.")
        return nx.complete_graph(10)
def fonk2(b6, start_node):
    for node in b6.nodes:
        fonk3(b6, node)
    b6.nodes[start_node]['color'] = 'gray'
    b6.nodes[start_node]['delta'] = 0
    b1 = q.Queue()
    b1.put(start_node)
    while not b1.empty():
        b2 = b1.get()
        fonk4(b6, b2, b1)
    return fonk5(b6)
def fonk3(b6, node):
    b6.nodes[node]['color'] = 'white'
    b6.nodes[node]['delta'] = float('inf')
    b6.nodes[node]['pi'] = None
def fonk4(b6, node, b1):
    for neighbor in b6.neighbors(node):
        if b6.nodes[neighbor]['color'] == 'white':
            b6.nodes[neighbor]['color'] = 'gray'
            b6.nodes[neighbor]['delta'] = b6.nodes[node]['delta'] + 1
            b6.nodes[neighbor]['pi'] = node
            b1.put(neighbor)
    b6.nodes[node]['color'] = 'black'
def fonk5(b6):
    b3 = nx.Graph()
    for node in b6.nodes:
        b3.add_node(node)
    for node in b6.nodes:
        b3.add_edge(node, b6.nodes[node]['pi'])
    return b3
if b4 = = '__main__':
    b5 = sys.argv[1] if len(sys.argv) > 1 else None
    b6 = fonk1(b5)
    b7 = sys.argv[2] if len(sys.argv) > 2 else list(b6.nodes)[0]
    b3 = fonk2(b6, b7)
    nx.draw(b6)
    plt.show()
    nx.draw(b3)
    plt.show()
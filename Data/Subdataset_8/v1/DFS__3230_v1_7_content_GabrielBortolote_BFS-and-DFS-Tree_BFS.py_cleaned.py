import networkx as nx
import queue as q
import matplotlib.pyplot as plt
import sys
def read_graph(file_path):
    try:
        G = nx.read_pajek(file_path)
        return G
    except FileNotFoundError:
        print("File not found. Generating a complete graph instead.")
        return nx.complete_graph(10)
def breadth_first_search(G, s):
    for node in G.nodes:
        G.nodes[node]['color'] = 'white'
        G.nodes[node]['delta'] = float('inf')
        G.nodes[node]['pi'] = None
    G.nodes[s]['color'] = 'gray'
    G.nodes[s]['delta'] = 0
    queue = q.Queue()
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        for node in G.neighbors(u):
            if G.nodes[node]['color'] == 'white':
                G.nodes[node]['color'] = 'gray'
                G.nodes[node]['delta'] = G.nodes[u]['delta'] + 1
                G.nodes[node]['pi'] = u
                queue.put(node)
        G.nodes[u]['color'] = 'black'
    BFS_Tree = nx.Graph()
    for node in G.nodes:
        BFS_Tree.add_node(node)
    for node in G.nodes:
        BFS_Tree.add_edge(node, G.nodes[node]['pi'])
    return BFS_Tree
if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = None
G = read_graph(input_file)
if len(sys.argv) > 2:
    starting_node = sys.argv[2]
else:
    starting_node = list(G.nodes)[0]
Tree = breadth_first_search(G, starting_node)
nx.draw(G)
plt.show()
nx.draw(Tree)
plt.show()
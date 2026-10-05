import networkx as nx
import queue as q
import matplotlib.pyplot as plt
import sys
if len(sys.argv) > 1:
    G = nx.read_pajek(sys.argv[1])
else:
    G = nx.complete_graph(10)
def breadth_first_search(G, start_node):
    for node in G.nodes:
        G.nodes[node]['color'] = 'white'
        G.nodes[node]['delta'] = float('inf')
        G.nodes[node]['pi'] = None
    G.nodes[start_node]['color'] = 'gray'
    G.nodes[start_node]['delta'] = 0
    queue = q.Queue()
    queue.put(start_node)
    while not queue.empty():
        current_node = queue.get()
        for neighbor in G.neighbors(current_node):
            if G.nodes[neighbor]['color'] == 'white':
                G.nodes[neighbor]['color'] = 'gray'
                G.nodes[neighbor]['delta'] = G.nodes[current_node]['delta'] + 1
                G.nodes[neighbor]['pi'] = current_node
                queue.put(neighbor)
        G.nodes[current_node]['color'] = 'black'
    bfs_tree = nx.Graph()
    for node in G.nodes:
        bfs_tree.add_node(node)
    for node in G.nodes:
        bfs_tree.add_edge(node, G.nodes[node]['pi'])
    return bfs_tree
if len(sys.argv) > 2:
    start_node = sys.argv[2]
else:
    start_node = list(G.nodes)[0]
BFS_Tree = breadth_first_search(G, start_node)
nx.draw(G)
plt.show()
nx.draw(BFS_Tree)
plt.show()
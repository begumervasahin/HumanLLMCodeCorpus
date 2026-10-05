import networkx as nx
import queue as q
import matplotlib.pyplot as plt
import sys
def read_graph(file_path):
    try:
        return nx.read_pajek(file_path)
    except FileNotFoundError:
        print("File not found. Generating a complete graph instead.")
        return nx.complete_graph(10)
def breadth_first_search(G, start_node):
    for node in G.nodes:
        initialize_node(G, node)
    G.nodes[start_node]['color'] = 'gray'
    G.nodes[start_node]['delta'] = 0
    queue = q.Queue()
    queue.put(start_node)
    while not queue.empty():
        current_node = queue.get()
        process_neighbors(G, current_node, queue)
    return construct_bfs_tree(G)
def initialize_node(G, node):
    G.nodes[node]['color'] = 'white'
    G.nodes[node]['delta'] = float('inf')
    G.nodes[node]['pi'] = None
def process_neighbors(G, node, queue):
    for neighbor in G.neighbors(node):
        if G.nodes[neighbor]['color'] == 'white':
            G.nodes[neighbor]['color'] = 'gray'
            G.nodes[neighbor]['delta'] = G.nodes[node]['delta'] + 1
            G.nodes[neighbor]['pi'] = node
            queue.put(neighbor)
    G.nodes[node]['color'] = 'black'
def construct_bfs_tree(G):
    bfs_tree = nx.Graph()
    for node in G.nodes:
        bfs_tree.add_node(node)
    for node in G.nodes:
        bfs_tree.add_edge(node, G.nodes[node]['pi'])
    return bfs_tree
if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else None
    G = read_graph(input_file)
    starting_node = sys.argv[2] if len(sys.argv) > 2 else list(G.nodes)[0]
    bfs_tree = breadth_first_search(G, starting_node)
    nx.draw(G)
    plt.show()
    nx.draw(bfs_tree)
    plt.show()
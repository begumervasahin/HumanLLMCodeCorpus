import networkx as nx
import queue as q
import matplotlib.pyplot as plt
import sys
def read_graph():
    if len(sys.argv) > 1:
        graph = nx.read_pajek(sys.argv[1])
    else:
        graph = nx.complete_graph(10)
    return graph
def breadth_first_search(graph, start_node):
    for node in graph.nodes:
        graph.nodes[node]['color'] = 'white'
        graph.nodes[node]['distance'] = float('inf')
        graph.nodes[node]['predecessor'] = None
    graph.nodes[start_node]['color'] = 'gray'
    graph.nodes[start_node]['distance'] = 0
    queue = q.Queue()
    queue.put(start_node)
    while not queue.empty():
        current_node = queue.get()
        for neighbor in graph.neighbors(current_node):
            if graph.nodes[neighbor]['color'] == 'white':
                graph.nodes[neighbor]['color'] = 'gray'
                graph.nodes[neighbor]['distance'] = graph.nodes[current_node]['distance'] + 1
                graph.nodes[neighbor]['predecessor'] = current_node
                queue.put(neighbor)
        graph.nodes[current_node]['color'] = 'black'
    bfs_tree = nx.Graph()
    for node in graph.nodes:
        bfs_tree.add_node(node)
    for node in graph.nodes:
        bfs_tree.add_edge(node, graph.nodes[node]['predecessor'])
    return bfs_tree
if __name__ == '__main__':
    graph = read_graph()
    if len(sys.argv) > 2:
        start_node = sys.argv[2]
    else:
        start_node = list(graph.nodes)[0]
    bfs_tree = breadth_first_search(graph, start_node)
    nx.draw(graph)
    plt.show()
    nx.draw(bfs_tree)
    plt.show()
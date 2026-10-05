import random
import time
import matplotlib.pyplot as plt
import networkx as nx
from scipy.interpolate import interp1d
from graph import Graph, Algorithms
def generate_random_graph(vertices):
    graph = nx.DiGraph()
    weights = [[random.randint(1, 1000) for _ in range(vertices)] for _ in range(vertices)]
    for i in range(vertices):
        weights[i][i] = 0
    for i in range(vertices):
        for j in range(vertices):
            if weights[i][j] != 0:
                graph.add_edges_from([(i, j)], weight=weights[i][j])
    return graph, weights
def remove_random_edges(graph, factor):
    edges_to_remove = int(len(graph.edges) / factor)
    for _ in range(edges_to_remove):
        edge = random.choice(list(graph.edges()))
        graph.remove_edge(*edge)
def main():
    vertices_list = []
    floyd_times = []
    dijkstra_times = []
    for graph_index in range(5):
        while True:
            vertices = random.randint(4, 8)
            if vertices not in vertices_list:
                vertices_list.append(vertices)
                break
        graph, weights = generate_random_graph(vertices)
        remove_random_edges(graph, random.uniform(1.0, 1.1))
        print('Total Remaining Edges for Graph {}: {}'.format(graph_index, len(graph.edges)))
        edge_labels = dict([((u, v), d['weight']) for u, v, d in graph.edges(data=True)])
        pos = nx.spring_layout(graph)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
        nx.draw(graph, pos, with_labels=True, node_size=1500, edge_color='black', edge_cmap=plt.cm.Reds)
        plt.show()
        algorithms = Algorithms()
        start_time = time.time()
        algorithms.floydWarshal(weights)
        floyd_elapsed_time = time.time() - start_time
        floyd_times.append(floyd_elapsed_time)
        start_time1 = time.time()
        algorithms.dijkstra(weights)
        dijkstra_elapsed_time = time.time() - start_time1
        dijkstra_times.append(dijkstra_elapsed_time)
        print("Floyd Execution Time:", floyd_elapsed_time)
        print("Dijkstra Execution Time:", dijkstra_elapsed_time)
    floyd_times.sort()
    dijkstra_times.sort()
    vertices_list.sort()
    floyd_interpolation = interp1d(vertices_list, floyd_times)
    dijkstra_interpolation = interp1d(vertices_list, dijkstra_times)
    floyd_cubic_interpolation = interp1d(vertices_list, floyd_times, kind='cubic')
    dijkstra_cubic_interpolation = interp1d(vertices_list, dijkstra_times, kind='cubic')
    plt.plot(vertices_list, floyd_times, 'o', vertices_list, floyd_interpolation(vertices_list), '-', vertices_list, floyd_cubic_interpolation(vertices_list), '-')
    plt.plot(vertices_list, dijkstra_times, 'o', vertices_list, dijkstra_interpolation(vertices_list), '-', vertices_list, dijkstra_cubic_interpolation(vertices_list), '-')
    plt.legend(['Floyd', '', 'Floyd Interpolated', 'Dijkstra', '', 'Dijkstra Interpolated'], loc='best')
    plt.show()
if __name__ == "__main__":
    main()
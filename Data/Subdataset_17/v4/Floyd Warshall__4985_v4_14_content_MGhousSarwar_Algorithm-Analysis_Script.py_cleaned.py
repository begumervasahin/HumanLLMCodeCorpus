import random
import sys
import time
import matplotlib.pyplot as plt
import networkx as nx
from scipy.interpolate import interp1d
class Algorithms:
    def __init__(self):
        self.v = 0
    def floyd_warshall(self, graph):
        self.v = len(graph)
        dist = [[graph[i][j] for j in range(self.v)] for i in range(self.v)]
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        self.print_solution(dist)
    def print_solution(self, dist):
        for i in range(self.v):
            for j in range(self.v):
                if dist[i][j] == float('inf'):
                    print("INF", end="\t")
                else:
                    print(f"{dist[i][j]:.2f}", end="\t")
            print()
        print()
    def minimum_distance(self, distance, shortest_path_tree_set):
        min_value = sys.maxsize
        min_index = -1
        for v in range(self.v):
            if not shortest_path_tree_set[v] and distance[v] <= min_value:
                min_value = distance[v]
                min_index = v
        return min_index
    def print_dijkstra(self, source, distance):
        print(f"Distance from vertex {source}:")
        print("Vertex\tDistance from source")
        for i in range(self.v):
            print(f"{i}\t\t{distance[i]}")
        print()
    def dijkstra(self, graph):
        self.v = len(graph)
        for source in range(self.v):
            distance = [sys.maxsize] * self.v
            shortest_path_tree_set = [False] * self.v
            distance[source] = 0
            for _ in range(self.v - 1):
                u = self.minimum_distance(distance, shortest_path_tree_set)
                shortest_path_tree_set[u] = True
                for v in range(self.v):
                    if (not shortest_path_tree_set[v] and graph[u][v] and distance[u] != sys.maxsize
                            and distance[u] + graph[u][v] < distance[v]):
                        distance[v] = distance[u] + graph[u][v]
            self.print_dijkstra(source, distance)
def create_random_graph(v):
    return [[random.randint(1, 1000) if i != j else 0 for j in range(v)] for i in range(v)]
def visualize_graph(G, pos, edge_labels):
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw(G, pos, with_labels=True, node_size=1500, edge_color='black', edge_cmap=plt.cm.Reds)
    plt.show()
def main():
    vlist = []
    floyd_times = []
    dijkstra_times = []
    for ip in range(5):
        print(f"Graph {ip + 1}")
        while True:
            v = random.randint(4, 8)
            if v not in vlist:
                vlist.append(v)
                break
        G = nx.DiGraph()
        data = create_random_graph(v)
        for i in range(v):
            for j in range(v):
                if data[i][j] != 0:
                    G.add_edge(i, j, weight=data[i][j])
        edges_to_remove = int(len(G.edges) / 1.1)
        for _ in range(edges_to_remove):
            edge = random.choice(list(G.edges))
            G.remove_edge(*edge)
        print(f"Total remaining edges: {len(G.edges)}")
        pos = nx.spring_layout(G)
        edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
        visualize_graph(G, pos, edge_labels)
        algo = Algorithms()
        start_time = time.time()
        algo.floyd_warshall(data)
        floyd_times.append(time.time() - start_time)
        start_time = time.time()
        algo.dijkstra(data)
        dijkstra_times.append(time.time() - start_time)
        print(f"Floyd-Warshall time: {floyd_times[-1]:.6f} seconds")
        print(f"Dijkstra time: {dijkstra_times[-1]:.6f} seconds")
    vlist.sort()
    floyd_times.sort()
    dijkstra_times.sort()
    floyd_interp = interp1d(vlist, floyd_times)
    dijkstra_interp = interp1d(vlist, dijkstra_times)
    floyd_cubic = interp1d(vlist, floyd_times, kind='cubic')
    dijkstra_cubic = interp1d(vlist, dijkstra_times, kind='cubic')
    plt.plot(vlist, floyd_times, 'o', vlist, floyd_interp(vlist), '-', vlist, floyd_cubic(vlist), '-')
    plt.plot(vlist, dijkstra_times, 'o', vlist, dijkstra_interp(vlist), '-', vlist, dijkstra_cubic(vlist), '-')
    plt.legend(['Floyd-Warshall', '', 'Floyd-Warshall (Cubic)', 'Dijkstra', '', 'Dijkstra (Cubic)'], loc='best')
    plt.show()
if __name__ == "__main__":
    main()
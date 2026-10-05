import sys
import time
import random
import matplotlib.pyplot as plt
import networkx as nx
from kruskal import Algoritimo_kruskal as kr
import prim_graph as prim
def generate_random_weighted_graph(num_vertices, connected=True):
    if connected:
        G = nx.connected_watts_strogatz_graph(num_vertices, 25, 0.5)
    else:
        G = nx.fast_gnp_random_graph(num_vertices, 0.1)
    for v1, v2 in G.edges():
        weight = random.randint(10, 100)
        G.edges[v1, v2]['weight'] = weight
    return G
def compute_mst_times(graph, num_trials=10):
    kruskal = kr()
    prim_graph = prim.Graph(graph.number_of_nodes())
    prim_graph.graph = nx.to_numpy_array(graph)
    kruskal_time_sum = 0
    prim_time_sum = 0
    for _ in range(num_trials):
        start_time = time.time()
        kruskal_mst = kruskal.kruskal(graph)
        kruskal_time_sum += time.time() - start_time
        start_time = time.time()
        prim_mst = prim_graph.primMST()
        prim_time_sum += time.time() - start_time
    kruskal_avg_time = kruskal_time_sum / num_trials
    prim_avg_time = prim_time_sum / num_trials
    return kruskal_avg_time, prim_avg_time
def plot_execution_times(vertices_list, kruskal_avg_times, prim_avg_times, graph_type):
    plt.plot(vertices_list, prim_avg_times, label="Prim's Algorithm")
    plt.plot(vertices_list, kruskal_avg_times, label="Kruskal's Algorithm")
    plt.legend()
    plt.xlabel('Number of Vertices')
    plt.ylabel('Execution Time (Seconds)')
    plt.title(f"Performance Comparison: Kruskal vs Prim ({graph_type} Graphs)")
    plt.savefig(f'Kruskal_vs_Prim_{graph_type}_Graphs.png')
    plt.show()
def generate_graphs(connected=True):
    vertices_list = []
    kruskal_avg_times = []
    prim_avg_times = []
    total_vertices = 2011
    for num_vertices in range(10, total_vertices, 100):
        print('Number of Vertices:', num_vertices)
        G = generate_random_weighted_graph(num_vertices, connected=connected)
        kruskal_avg_time, prim_avg_time = compute_mst_times(G)
        vertices_list.append(num_vertices)
        kruskal_avg_times.append(kruskal_avg_time)
        prim_avg_times.append(prim_avg_time)
        print("Average Execution Time (Kruskal):", kruskal_avg_time, "seconds")
        print("Average Execution Time (Prim):", prim_avg_time, "seconds")
    plot_execution_times(vertices_list, kruskal_avg_times, prim_avg_times, "Complete" if connected else "Incomplete")
if __name__ == "__main__":
    generate_graphs(connected=False)
    generate_graphs(connected=True)

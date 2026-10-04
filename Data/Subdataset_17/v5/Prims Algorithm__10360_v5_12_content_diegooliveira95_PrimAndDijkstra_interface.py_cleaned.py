import random
import time
from graph import Vertex, Graph
from dijkstra import dijkstra as Dijkstra
from prim import prim as Prim
def generate_random_weighted_graph(num_vertices, probability, lower_weight, higher_weight):
    graph = Graph()
    for i in range(1, num_vertices + 1):
        graph.addVertex(str(i))
    for vertex in graph:
        for other_vertex in graph:
            if other_vertex.getId() == vertex.getId() or other_vertex.getId() in vertex.getConnections():
                continue
            if probability > random.randrange(0, 100):
                graph.addEdge(vertex.getId(), other_vertex.getId(), random.randint(lower_weight, higher_weight))
    return graph
def measure_algorithm_performance(graph, algorithm, algorithm_name, start_vertex_id='1'):
    start_time = time.time()
    algorithm(graph, graph.getVertex(start_vertex_id))
    total_time = time.time() - start_time
    return total_time
def print_performance_results(graph_label, dijkstra_time, prim_time):
    print(f"----------------- {graph_label} -----------------")
    print(f"Dijkstra: {dijkstra_time:.6f} seconds")
    print(f"Prim: {prim_time:.6f} seconds")
    print("----------------------------------------------------\n")
if __name__ == '__main__':
    graph_configs = [
        (200, 90, 1, 5, "First Sample"),
        (300, 90, 1, 5, "Second Sample"),
        (400, 90, 1, 5, "Third Sample"),
        (200, 20, 1, 5, "Fourth Sample"),
        (300, 20, 1, 5, "Fifth Sample"),
        (400, 20, 1, 5, "Sixth Sample")
    ]
    for num_vertices, probability, lower_weight, higher_weight, label in graph_configs:
        graph = generate_random_weighted_graph(num_vertices, probability, lower_weight, higher_weight)
        dijkstra_time = measure_algorithm_performance(graph, Dijkstra, 'Dijkstra')
        prim_time = measure_algorithm_performance(graph, Prim, 'Prim')
        print_performance_results(label, dijkstra_time, prim_time)
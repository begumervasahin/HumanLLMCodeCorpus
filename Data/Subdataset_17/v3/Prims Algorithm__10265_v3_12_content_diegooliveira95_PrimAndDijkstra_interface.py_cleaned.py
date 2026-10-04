import random
import time
from graph import Vertex, Graph
from dijkstra import dijkstra as Dijkstra
from prim import prim as Prim
def generate_random_weighted_graph(num_vertices, edge_probability, weight_min, weight_max):
    graph = Graph()
    for vertex_id in range(1, num_vertices + 1):
        graph.addVertex(str(vertex_id))
    for vertex_a in graph:
        for vertex_b in graph:
            if vertex_a.getId() == vertex_b.getId() or vertex_b.getId() in vertex_a.getConnections():
                continue
            if edge_probability > random.uniform(0, 100):
                weight = random.randint(weight_min, weight_max)
                graph.addEdge(vertex_a.getId(), vertex_b.getId(), weight)
    return graph
def measure_algorithm_time(graph, algorithm, start_vertex_id):
    start_time = time.time()
    algorithm(graph, graph.getVertex(start_vertex_id))
    return time.time() - start_time
def main():
    sample_graphs = [
        (200, 90, 1, 5),
        (300, 90, 1, 5),
        (400, 90, 1, 5),
        (200, 20, 1, 5),
        (300, 20, 1, 5),
        (400, 20, 1, 5)
    ]
    for i, (num_vertices, edge_probability, weight_min, weight_max) in enumerate(sample_graphs):
        graph = generate_random_weighted_graph(num_vertices, edge_probability, weight_min, weight_max)
        dijkstra_time = measure_algorithm_time(graph, Dijkstra, '1')
        prim_time = measure_algorithm_time(graph, Prim, '1')
        print(f"----------------- Sample {i + 1} -----------------")
        print(f"Dijkstra: {dijkstra_time:.6f} seconds")
        print(f"Prim: {prim_time:.6f} seconds")
        print("----------------------------------------------------\n")
if __name__ == '__main__':
    main()
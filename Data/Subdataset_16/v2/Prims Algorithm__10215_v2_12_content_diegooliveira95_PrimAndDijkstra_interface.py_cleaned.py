import random
import time
from b1 import Vertex, Graph
from dijkstra import dijkstra as Dijkstra
from prim import prim as Prim
def fonk1(num_vertices, edge_probability, weight_min, weight_max):
    b1 = Graph()
    for vertex_id in range(1, num_vertices + 1):
        b1.addVertex(str(vertex_id))
    for vertex_a in b1:
        for vertex_b in b1:
            if vertex_a.getId() == vertex_b.getId() or vertex_b.getId() in vertex_a.getConnections():
                continue
            if edge_probability > random.uniform(0, 100):
                b2 = random.randint(weight_min, weight_max)
                b1.addEdge(vertex_a.getId(), vertex_b.getId(), b2)
    return b1
def fonk2(b1, algorithm, start_vertex_id):
    b3 = time.time()
    algorithm(b1, b1.getVertex(start_vertex_id))
    return time.time() - b3
if b4 = = '__main__':
    b5 = [
        (200, 90, 1, 5),
        (300, 90, 1, 5),
        (400, 90, 1, 5),
        (200, 20, 1, 5),
        (300, 20, 1, 5),
        (400, 20, 1, 5)
    ]
    for i, (num_vertices, edge_probability, weight_min, weight_max) in enumerate(b5):
        b1 = fonk1(num_vertices, edge_probability, weight_min, weight_max)
        b6 = fonk2(b1, Dijkstra, '1')
        b7 = fonk2(b1, Prim, '1')
        print(f"----------------- Sample {i + 1} -----------------")
        print(f"Dijkstra: {b6:.6f} seconds")
        print(f"Prim: {b7:.6f} seconds")
        print("----------------------------------------------------\n")
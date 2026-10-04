import random
import time
from b1 import Vertex, Graph
from dijkstra import dijkstra as Dijkstra
from prim import prim as Prim
def fonk1(num_vertices, probability, lower_weight, higher_weight):
    b1 = Graph()
    for i in range(1, num_vertices + 1):
        b1.addVertex(str(i))
    for vertex in b1:
        for other_vertex in b1:
            if other_vertex.getId() == vertex.getId() or other_vertex.getId() in vertex.getConnections():
                continue
            if probability > random.randrange(0, 100):
                b1.addEdge(vertex.getId(), other_vertex.getId(), random.randint(lower_weight, higher_weight))
    return b1
def fonk2(b1, algorithm, algorithm_name, b2 = '1'):
    b3 = time.time()
    algorithm(b1, b1.getVertex(b2))
    b4 = time.time() - b3
    return b4
def fonk3(graph_label, b7, b8):
    print(f"----------------- {graph_label} -----------------")
    print(f"Dijkstra: {b7:.6f} seconds")
    print(f"Prim: {b8:.6f} seconds")
    print("----------------------------------------------------\n")
if b5 = = '__main__':
    b6 = [
        (200, 90, 1, 5, "First Sample"),
        (300, 90, 1, 5, "Second Sample"),
        (400, 90, 1, 5, "Third Sample"),
        (200, 20, 1, 5, "Fourth Sample"),
        (300, 20, 1, 5, "Fifth Sample"),
        (400, 20, 1, 5, "Sixth Sample")
    ]
    for num_vertices, probability, lower_weight, higher_weight, label in b6:
        b1 = fonk1(num_vertices, probability, lower_weight, higher_weight)
        b7 = fonk2(b1, Dijkstra, 'Dijkstra')
        b8 = fonk2(b1, Prim, 'Prim')
        fonk3(label, b7, b8)
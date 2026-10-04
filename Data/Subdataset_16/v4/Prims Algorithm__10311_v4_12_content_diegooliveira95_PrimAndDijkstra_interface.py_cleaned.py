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
def fonk2(b1, graph_label):
    b2 = time.time()
    Dijkstra(b1, b1.getVertex('1'))
    b3 = time.time() - b2
    b4 = time.time()
    Prim(b1, b1.getVertex('1'))
    b5 = time.time() - b4
    print(f"----------------- {graph_label} -----------------")
    print(f"Dijkstra: {b3:.6f} seconds")
    print(f"Prim: {b5:.6f} seconds")
    print("----------------------------------------------------\n")
if b6 = = '__main__':
    b7 = [
        (fonk1(200, 90, 1, 5), "First Sample"),
        (fonk1(300, 90, 1, 5), "Second Sample"),
        (fonk1(400, 90, 1, 5), "Third Sample"),
        (fonk1(200, 20, 1, 5), "Fourth Sample"),
        (fonk1(300, 20, 1, 5), "Fifth Sample"),
        (fonk1(400, 20, 1, 5), "Sixth Sample")
    ]
    for b1, label in b7:
        fonk2(b1, label)
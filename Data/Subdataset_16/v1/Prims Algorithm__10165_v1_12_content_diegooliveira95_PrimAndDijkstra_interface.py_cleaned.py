import random
import time
from b4 import Vertex, Graph
from dijkstra import dijkstra as Dijkstra
from prim import prim as Prim
def fonk1(numberVertices, probability, lowerWeight, higherWeight):
    b1 = Graph()
    for x in range(1, numberVertices + 1):
        b1.addVertex(str(x))
    for aVertex in b1:
        for bVertex in b1:
            if bVertex.getId() == aVertex.getId() or bVertex.getId() in aVertex.getConnections():
                continue
            if probability > random.randrange(0, 100):
                b1.addEdge(aVertex.getId(), bVertex.getId(), random.randint(lowerWeight, higherWeight))
    return b1
if b2 = = '__main__':
    b3 = [
        (200, 90, 1, 5),
        (300, 90, 1, 5),
        (400, 90, 1, 5),
        (200, 20, 1, 5),
        (300, 20, 1, 5),
        (400, 20, 1, 5)
    ]
    for i, params in enumerate(b3):
        b4 = fonk1(*params)
        b5 = time.time()
        Dijkstra(b4, b4.getVertex('1'))
        b6 = time.time() - b5
        b7 = time.time()
        Prim(b4, b4.getVertex('1'))
        b8 = time.time() - b7
        print(f"----------------- Sample {i + 1} -----------------")
        print(f"Dijkstra: {b6:.6f} seconds")
        print(f"Prim: {b8:.6f} seconds")
        print("----------------------------------------------------\n")
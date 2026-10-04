import random
import time
from graph import Vertex, Graph
from dijkstra import dijkstra as Dijkstra
from prim import prim as Prim
def generateRandomWeightedGraph(numberVertices, probability, lowerWeight, higherWeight):
    aGraph = Graph()
    for x in range(1, numberVertices + 1):
        aGraph.addVertex(str(x))
    for aVertex in aGraph:
        for bVertex in aGraph:
            if bVertex.getId() == aVertex.getId() or bVertex.getId() in aVertex.getConnections():
                continue
            if probability > random.randrange(0, 100):
                aGraph.addEdge(aVertex.getId(), bVertex.getId(), random.randint(lowerWeight, higherWeight))
    return aGraph
if __name__ == '__main__':
    sample_graphs = [
        (200, 90, 1, 5),
        (300, 90, 1, 5),
        (400, 90, 1, 5),
        (200, 20, 1, 5),
        (300, 20, 1, 5),
        (400, 20, 1, 5)
    ]
    for i, params in enumerate(sample_graphs):
        graph = generateRandomWeightedGraph(*params)
        startTimeDijkstra = time.time()
        Dijkstra(graph, graph.getVertex('1'))
        totalTimeDijkstra = time.time() - startTimeDijkstra
        startTimePrim = time.time()
        Prim(graph, graph.getVertex('1'))
        totalTimePrim = time.time() - startTimePrim
        print(f"----------------- Sample {i + 1} -----------------")
        print(f"Dijkstra: {totalTimeDijkstra:.6f} seconds")
        print(f"Prim: {totalTimePrim:.6f} seconds")
        print("----------------------------------------------------\n")
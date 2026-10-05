
from graph import Vertex, Graph
from pythonds.graphs import PriorityQueue
import sys
def prim_minimum_spanning_tree(graph, start_vertex):
    priority_queue = PriorityQueue()
    for vertex in graph:
        vertex.setDistance(sys.maxsize)
        vertex.setPrevious(None)
    start_vertex.setDistance(0)
    priority_queue.buildHeap([(vertex.getDistance(), vertex) for vertex in graph])
    while not priority_queue.isEmpty():
        current_vertex = priority_queue.delMin()
        for neighbor_vertex in current_vertex.getConnections():
            new_cost = current_vertex.getWeight(neighbor_vertex)
            if neighbor_vertex in priority_queue and new_cost < neighbor_vertex.getDistance():
                neighbor_vertex.setPrevious(current_vertex)
                neighbor_vertex.setDistance(new_cost)
                priority_queue.decreaseKey(neighbor_vertex, new_cost)
if __name__ == "__main__":
    sample_graph = Graph()
    for i in range(6):
        sample_graph.addVertex(i)
    sample_graph.addEdge(0, 1, 5)
    sample_graph.addEdge(0, 5, 2)
    sample_graph.addEdge(1, 2, 4)
    sample_graph.addEdge(2, 3, 9)
    sample_graph.addEdge(3, 4, 7)
    sample_graph.addEdge(3, 5, 3)
    sample_graph.addEdge(4, 0, 1)
    sample_graph.addEdge(5, 4, 8)
    sample_graph.addEdge(5, 2, 1)
    prim_minimum_spanning_tree(sample_graph, sample_graph.getVertex(0))
    for vertex in sample_graph:
        previous_vertex = vertex.getPrevious()
        if previous_vertex:
            print("(%s, %s) -> %s" % (previous_vertex.getId(), vertex.getId(), vertex.getDistance()))
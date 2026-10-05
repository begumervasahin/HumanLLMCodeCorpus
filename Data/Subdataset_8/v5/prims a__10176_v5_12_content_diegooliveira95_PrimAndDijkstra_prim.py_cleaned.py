from graph import Vertex
from graph import Graph
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
        for next_vertex in current_vertex.getConnections():
            new_cost = current_vertex.getWeight(next_vertex)
            if next_vertex in priority_queue and new_cost < next_vertex.getDistance():
                next_vertex.setPrevious(current_vertex)
                next_vertex.setDistance(new_cost)
                priority_queue.decreaseKey(next_vertex, new_cost)
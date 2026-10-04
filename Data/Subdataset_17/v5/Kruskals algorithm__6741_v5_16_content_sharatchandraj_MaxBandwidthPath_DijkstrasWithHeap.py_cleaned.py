from collections import namedtuple
import MaxHeap
NUM_VERTICES = 5000
Edge = namedtuple('Edge', ['vertex', 'weight'])
def initialize_status_and_weights(num_vertices):
    status = ['unseen'] * num_vertices
    weights = [float('-inf')] * num_vertices
    return status, weights
def update_fringe_for_source(source, graph, status, weights, parents):
    for edge in graph.get_edge(source):
        status[edge.vertex] = 'fringe'
        weights[edge.vertex] = edge.weight
        MaxHeap.Insert(edge.vertex, edge.weight)
        parents[edge.vertex] = source
def dijkstra_with_heap(graph, source, destination):
    MaxHeap.initialize()
    parents = [None] * NUM_VERTICES
    status, weights = initialize_status_and_weights(NUM_VERTICES)
    status[source] = 'intree'
    update_fringe_for_source(source, graph, status, weights, parents)
    while 'fringe' in status:
        max_vertex = MaxHeap.Max()
        if max_vertex == destination:
            break
        status[max_vertex] = 'intree'
        MaxHeap.Delete(max_vertex)
        for edge in graph.get_edge(max_vertex):
            if status[edge.vertex] == 'unseen':
                status[edge.vertex] = 'fringe'
                parents[edge.vertex] = max_vertex
                weights[edge.vertex] = min(weights[max_vertex], edge.weight)
                MaxHeap.Insert(edge.vertex, weights[edge.vertex])
            elif status[edge.vertex] == 'fringe' and weights[edge.vertex] < min(weights[max_vertex], edge.weight):
                parents[edge.vertex] = max_vertex
                MaxHeap.Delete(edge.vertex)
                weights[edge.vertex] = min(weights[max_vertex], edge.weight)
                MaxHeap.Insert(edge.vertex, weights[edge.vertex])
    path = reconstruct_path(parents, destination)
    return path, weights[destination]
def reconstruct_path(parents, destination):
    path = []
    current_vertex = destination
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = parents[current_vertex]
    path.reverse()
    return path
from collections import namedtuple
from typing import List, Tuple, Optional
Edge = namedtuple('Edge', ['vertex', 'weight'])
def pick_best_vertex(status: List[str], weights: List[float]) -> Optional[int]:
    best_vertex = None
    best_weight = float('-inf')
    for i, (st, wt) in enumerate(zip(status, weights)):
        if st == 'fringe' and wt > best_weight:
            best_weight = wt
            best_vertex = i
    return best_vertex
def dijkstra_no_heap(graph, source: int, destination: int) -> Tuple[List[int], float]:
    number_of_vertices = len(graph.get_vertex())
    status = ['unseen'] * number_of_vertices
    weights = [float('-inf')] * number_of_vertices
    predecessors = [None] * number_of_vertices
    status[source] = 'intree'
    weights[source] = float('inf')
    for edge in graph.get_edge(source):
        status[edge.vertex] = 'fringe'
        weights[edge.vertex] = edge.weight
        predecessors[edge.vertex] = source
    while 'fringe' in status:
        v = pick_best_vertex(status, weights)
        if v is None:
            break
        status[v] = 'intree'
        for edge in graph.get_edge(v):
            if status[edge.vertex] == 'unseen':
                status[edge.vertex] = 'fringe'
                predecessors[edge.vertex] = v
                weights[edge.vertex] = min(weights[v], edge.weight)
            elif status[edge.vertex] == 'fringe' and weights[edge.vertex] < min(weights[v], edge.weight):
                predecessors[edge.vertex] = v
                weights[edge.vertex] = min(weights[v], edge.weight)
    max_bandwidth_path = []
    current_vertex = destination
    while current_vertex is not None:
        max_bandwidth_path.append(current_vertex)
        current_vertex = predecessors[current_vertex]
    max_bandwidth_path.reverse()
    return max_bandwidth_path, weights[destination]
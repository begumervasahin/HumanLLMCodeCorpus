from heapq import heappush, heappop, heapify
from collections import defaultdict
def prims_mst(graph):
    num_vertices = len(graph)
    seen = set()
    start_vertex = next(iter(graph))
    seen.add(start_vertex)
    edge_heap = list(graph[start_vertex])
    heapify(edge_heap)
    selected_nodes = [start_vertex]
    total_cost = 0
    while len(selected_nodes) != num_vertices:
        weight, next_vertex = heappop(edge_heap)
        if next_vertex in seen:
            continue
        total_cost += weight
        selected_nodes.append(next_vertex)
        seen.add(next_vertex)
        for neighbor_weight, neighbor_vertex in graph[next_vertex]:
            if neighbor_vertex not in seen:
                heappush(edge_heap, (neighbor_weight, neighbor_vertex))
    return selected_nodes, total_cost
data_file = open('edges.txt')
graph = defaultdict(set)
next(data_file)
for line in data_file:
    vertex1, vertex2, weight = line.split()
    weight = int(weight)
    graph[vertex1].add((weight, vertex2))
    graph[vertex2].add((weight, vertex1))
print(prims_mst(graph))
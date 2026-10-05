from heapq import heappush, heappop, heapify
from collections import defaultdict
def prims_mst(graph):
    num_vertices = len(graph)
    seen = set()
    source = next(iter(graph))
    seen.add(source)
    source_connections = list(graph[source])
    edge_costs = source_connections
    heapify(edge_costs)
    selected_nodes = [source]
    total_cost = 0
    while len(selected_nodes) != num_vertices:
        next_edge = heappop(edge_costs)
        if next_edge[1] in seen:
            continue
        total_cost += next_edge[0]
        added_vertex = next_edge[1]
        selected_nodes.append(added_vertex)
        seen.add(added_vertex)
        for edge in graph[added_vertex]:
            if edge[1] not in seen:
                heappush(edge_costs, edge)
    return selected_nodes, total_cost
data_file = open('edges.txt')
graph = defaultdict(set)
next(data_file)
for line in data_file:
    vals = line.split()
    graph[vals[0]].add((int(vals[2]), vals[1]))
    graph[vals[1]].add((int(vals[2]), vals[0]))
print(prims_mst(graph))
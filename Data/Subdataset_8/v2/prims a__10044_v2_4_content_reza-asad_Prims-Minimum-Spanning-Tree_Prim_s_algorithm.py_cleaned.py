from heapq import heappush, heappop, heapify
from collections import defaultdict
def prims_minimum_spanning_tree(graph):
    num_vertices = len(graph)
    visited = set()
    source_vertex = next(iter(graph.keys()))
    visited.add(source_vertex)
    source_connections = list(graph[source_vertex])
    edge_costs = source_connections
    heapify(edge_costs)
    selected_nodes = [source_vertex]
    total_cost = 0
    while len(selected_nodes) != num_vertices:
        next_edge = heappop(edge_costs)
        if next_edge[1] in visited:
            continue
        total_cost += next_edge[0]
        added_vertex = next_edge[1]
        selected_nodes.append(added_vertex)
        visited.add(added_vertex)
        for edge in graph[added_vertex]:
            if edge[1] not in visited:
                heappush(edge_costs, edge)
    return selected_nodes, total_cost
def read_graph_from_file(filename):
    graph = defaultdict(set)
    with open(filename, 'r') as data_file:
        next(data_file)
        for line in data_file:
            vals = line.split()
            graph[vals[0]].add((int(vals[2]), vals[1]))
            graph[vals[1]].add((int(vals[2]), vals[0]))
    return graph
if __name__ == "__main__":
    graph = read_graph_from_file('edges.txt')
    mst_nodes, total_cost = prims_minimum_spanning_tree(graph)
    print("Minimum Spanning Tree Nodes:", mst_nodes)
    print("Total Cost:", total_cost)
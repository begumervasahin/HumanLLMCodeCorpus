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
        cost, added_vertex = next_edge
        if added_vertex in visited:
            continue
        total_cost += cost
        selected_nodes.append(added_vertex)
        visited.add(added_vertex)
        for edge_cost, adjacent_vertex in graph[added_vertex]:
            if adjacent_vertex not in visited:
                heappush(edge_costs, (edge_cost, adjacent_vertex))
    return selected_nodes, total_cost
def read_graph_from_file(filename):
    graph = defaultdict(set)
    with open(filename, 'r') as data_file:
        next(data_file)
        for line in data_file:
            vertex1, vertex2, cost = line.split()
            cost = int(cost)
            graph[vertex1].add((cost, vertex2))
            graph[vertex2].add((cost, vertex1))
    return graph
if __name__ == "__main__":
    graph = read_graph_from_file('edges.txt')
    mst_nodes, total_cost = prims_minimum_spanning_tree(graph)
    print("Minimum Spanning Tree Nodes:", mst_nodes)
    print("Total Cost:", total_cost)
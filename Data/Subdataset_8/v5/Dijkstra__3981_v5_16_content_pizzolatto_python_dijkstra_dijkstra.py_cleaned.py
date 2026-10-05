
graph = {
    "inicio": {"a": 6, "b": 2},
    "a": {"fim": 1},
    "b": {"a": 3, "fim": 5},
    "fim": {}
}
infinity = float("inf")
costs = {"a": 6, "b": 2, "fim": infinity}
parents = {"a": "inicio", "b": "inicio", "fim": None}
processed_nodes = []
def find_lowest_cost_node(costs, processed_nodes):
    min_cost = infinity
    min_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < min_cost and node not in processed_nodes:
            min_cost = cost
            min_cost_node = node
    return min_cost_node
def dijkstra(graph, costs, parents, processed_nodes):
    node = find_lowest_cost_node(costs, processed_nodes)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for neighbor in neighbors:
            new_cost = cost + neighbors[neighbor]
            if costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        processed_nodes.append(node)
        node = find_lowest_cost_node(costs, processed_nodes)
dijkstra(graph, costs, parents, processed_nodes)
print(costs)

print("[+] Dijkstra's algorithm running!")
INFINITY = float("inf")
processed_nodes = []
graph = {
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {}
}
costs = {
    "a": 6,
    "b": 2,
    "fin": INFINITY
}
parents = {
    "a": "start",
    "b": "start",
    "fin": None
}
def find_lowest_cost_node(costs, processed):
    min_cost = INFINITY
    min_cost_node = None
    for node, cost in costs.items():
        if cost < min_cost and node not in processed:
            min_cost = cost
            min_cost_node = node
    return min_cost_node
current_node = find_lowest_cost_node(costs, processed_nodes)
while current_node is not None:
    cost = costs[current_node]
    neighbors = graph[current_node]
    for neighbor, edge_cost in neighbors.items():
        new_cost = cost + edge_cost
        if costs[neighbor] > new_cost:
            costs[neighbor] = new_cost
            parents[neighbor] = current_node
    processed_nodes.append(current_node)
    current_node = find_lowest_cost_node(costs, processed_nodes)
print("Costs:", costs)
print("Parents:", parents)
print("Processed Nodes:", processed_nodes)
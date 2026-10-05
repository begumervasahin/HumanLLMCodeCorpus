print("[+] Dijkstra's algorithm running!")
infinity = float("inf")
processed = []
graph = {
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {}
}
costs = {
    "a": 6,
    "b": 2,
    "fin": infinity
}
parents = {
    "a": "start",
    "b": "start",
    "fin": None
}
def find_lowest_cost_node(costs, processed):
    lowest_cost = infinity
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
node = find_lowest_cost_node(costs, processed)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for n, edge_cost in neighbours.items():
        new_cost = cost + edge_cost
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs, processed)
print("Costs:", costs)
print("Parents:", parents)
print("Processed:", processed)
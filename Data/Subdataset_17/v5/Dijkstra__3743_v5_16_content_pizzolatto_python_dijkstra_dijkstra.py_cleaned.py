
graph = {
    "start": {"a": 6, "b": 2},
    "a": {"end": 1},
    "b": {"a": 3, "end": 5},
    "end": {}
}
infinity = float("inf")
costs = {
    "a": 6,
    "b": 2,
    "end": infinity
}
parents = {
    "a": "start",
    "b": "start",
    "end": None
}
processed = []
def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for neighbor in neighbors:
        new_cost = cost + neighbors[neighbor]
        if costs[neighbor] > new_cost:
            costs[neighbor] = new_cost
            parents[neighbor] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print("Costs to reach each node:", costs)
print("Parents of each node:", parents)
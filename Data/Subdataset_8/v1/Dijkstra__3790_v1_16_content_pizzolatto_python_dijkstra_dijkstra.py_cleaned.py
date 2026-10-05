from collections import defaultdict
graph = defaultdict(dict)
graph["inicio"]["a"] = 6
graph["inicio"]["b"] = 2
graph["a"]["fim"] = 1
graph["b"]["a"] = 3
graph["b"]["fim"] = 5
INFINITY = float("inf")
costs = {"a": 6, "b": 2, "fim": INFINITY}
parents = {"a": "inicio", "b": "inicio", "fim": None}
processed = []
def find_lowest_cost_node(costs, processed):
    lowest_cost = INFINITY
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
node = find_lowest_cost_node(costs, processed)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for neighbor, neighbor_cost in neighbors.items():
        new_cost = cost + neighbor_cost
        if costs[neighbor] > new_cost:
            costs[neighbor] = new_cost
            parents[neighbor] = node
    processed.append(node)
    node = find_lowest_cost_node(costs, processed)
print(costs)
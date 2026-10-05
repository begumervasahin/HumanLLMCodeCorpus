from collections import defaultdict
graph = defaultdict(dict)
graph["inicio"]["a"] = 6
graph["inicio"]["b"] = 2
graph["a"]["fim"] = 1
graph["b"]["a"] = 3
graph["b"]["fim"] = 5
INFINITY = float("inf")
node_costs = {"a": 6, "b": 2, "fim": INFINITY}
node_parents = {"a": "inicio", "b": "inicio", "fim": None}
processed_nodes = []
def find_lowest_cost_node(costs, processed):
    lowest_cost = INFINITY
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
current_node = find_lowest_cost_node(node_costs, processed_nodes)
while current_node is not None:
    current_cost = node_costs[current_node]
    neighbors = graph[current_node]
    for neighbor, neighbor_cost in neighbors.items():
        new_cost = current_cost + neighbor_cost
        if node_costs[neighbor] > new_cost:
            node_costs[neighbor] = new_cost
            node_parents[neighbor] = current_node
    processed_nodes.append(current_node)
    current_node = find_lowest_cost_node(node_costs, processed_nodes)
print(node_costs)
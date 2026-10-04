def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
def dijkstra_algorithm():
    print("[+] Dijkstra's algorithm running!")
    graph = {
        "start": {"a": 6, "b": 2},
        "a": {"fin": 1},
        "b": {"a": 3, "fin": 5},
        "fin": {}
    }
    infinity = float("inf")
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
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for neighbor, weight in neighbors.items():
            new_cost = cost + weight
            if costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    print("Costs:", costs)
    print("Parents:", parents)
    print("Processed nodes:", processed)
if __name__ == "__main__":
    dijkstra_algorithm()
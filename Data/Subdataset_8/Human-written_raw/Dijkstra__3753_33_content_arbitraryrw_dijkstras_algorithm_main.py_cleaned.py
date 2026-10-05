print("[+] Dijkstra's algorithm running!")
infinity = float("inf")
processed = []
graph = dict()
graph["a"] = dict()
graph["a"]["fin"] = 1
graph["b"] = dict()
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = dict()
costs = dict()
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
parents = dict()
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for n in neighbours.keys():
        new_cost = cost + neighbours[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print(costs)
print(parents)
print(processed)
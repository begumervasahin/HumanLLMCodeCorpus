import math
node_values = {
    "a": [math.inf, ""],
    "b": [math.inf, ""],
    "c": [math.inf, ""],
    "d": [math.inf, ""],
    "e": [math.inf, ""],
    "f": [math.inf, ""],
    "g": [math.inf, ""]
}
edges = [
    ["a", "b", 9],
    ["a", "c", 2],
    ["b", "c", 6],
    ["b", "e", 1],
    ["c", "f", 9],
    ["d", "b", 3],
    ["d", "c", 2],
    ["d", "e", 5],
    ["d", "f", 6],
    ["e", "f", 3],
    ["e", "g", 7],
    ["f", "g", 4]
]
def update_node_values(origin, destination, value):
    if value < node_values[destination][0]:
        node_values[destination][0] = value
        node_values[destination][1] = origin
        return True
    return False
start_node = "a"
end_node = "g"
node_values[start_node][0] = 0
while True:
    done = True
    for edge in edges:
        origin, destination, weight = edge
        if update_node_values(origin, destination, node_values[origin][0] + weight):
            done = False
        if update_node_values(destination, origin, node_values[destination][0] + weight):
            done = False
    if done:
        break
shortest_path = [end_node]
while True:
    current_node = shortest_path[-1]
    if current_node == start_node:
        break
    shortest_path.append(node_values[current_node][1])
print(f"The shortest path from node '{start_node}' to node '{end_node}' is: {shortest_path[::-1]}")
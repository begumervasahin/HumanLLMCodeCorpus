import math
values = {
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
def update_values(origin, destination, value):
    if value < values[destination][0]:
        values[destination][0] = value
        values[destination][1] = origin
        return True
    return False
start_node = "a"
end_node = "g"
values[start_node][0] = 0
while True:
    done = True
    for edge in edges:
        if update_values(edge[0], edge[1], values[edge[0]][0] + edge[2]):
            done = False
        if update_values(edge[1], edge[0], values[edge[1]][0] + edge[2]):
            done = False
    if done:
        break
shortest_path = [end_node]
while True:
    if shortest_path[-1] == start_node:
        break
    shortest_path.append(values[shortest_path[-1]][1])
print(f"The shortest path from node '{start_node}' to node '{end_node}' is: {shortest_path[::-1]}")
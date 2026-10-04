import sys
def read(filename, debug=False):
    graph = {}
    with open(filename) as file:
        for line in file:
            parts = line.strip().split()
            if debug:
                print("parts:", parts, "len(parts):", len(parts))
            if parts:
                graph[parts[0]] = ('white', parts[1:])
    return graph
def dump(graph):
    print("Dumping graph: nodeName (color, [adj list])")
    for node, details in graph.items():
        print(node, details)
def bfs(graph, start_node):
    queue = [start_node]
    graph[start_node] = ("black", graph[start_node][1], 0)
    bfs_list = [(start_node, 0)]
    while queue:
        current_node = queue.pop(0)
        for neighbor in graph[current_node][1]:
            if graph[neighbor][0] == "white":
                graph[neighbor] = ('grey', graph[neighbor][1], graph[current_node][2] + 1)
                bfs_list.append((neighbor, graph[neighbor][2]))
                queue.append(neighbor)
        graph[current_node] = ("black", graph[current_node][1])
    return bfs_list
def reset_colors(graph):
    for node in graph:
        graph[node] = ('white', graph[node][1])
def dfs(graph, node):
    graph[node] = ("grey", graph[node][1])
    for neighbor in graph[node][1]:
        if graph[neighbor][0] == "white":
            dfs(graph, neighbor)
        elif graph[neighbor][0] == "grey":
            print(f"Cycle detected at node {neighbor}")
    graph[node] = ("black", graph[node][1])
if __name__ == "__main__":
    debug = len(sys.argv) > 3
    graph = read(sys.argv[1], debug)
    root = sys.argv[2]
    if debug:
        dump(graph)
    print("Root node:", root)
    bfs_result = bfs(graph, root)
    print("BFS result:")
    print(bfs_result)
    if debug:
        dump(graph)
    reset_colors(graph)
    if debug:
        dump(graph)
    print("DFS result:")
    dfs(graph, root)
    if debug:
        dump(graph)
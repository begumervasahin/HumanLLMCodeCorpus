import sys
def read(filename, debug=False):
    graph = {}
    with open(filename) as file:
        for line in file:
            line = line.strip().split()
            if debug:
                print("Line:", line, "Length:", len(line))
            if line:
                graph[line[0]] = ('white', line[1:])
    return graph
def dump(graph):
    print("Graph representation: nodeName (color, [adjacent nodes])")
    for node in graph:
        print(node, graph[node])
def bfs(graph, start_node):
    queue = [start_node]
    graph[start_node] = ("black", graph[start_node][1], 0)
    bfs_result = [(start_node, 0)]
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node][1]:
            if graph[neighbor][0] == "white":
                graph[neighbor] = ('grey', graph[neighbor][1], graph[node][2] + 1)
                bfs_result.append((neighbor, graph[neighbor][2]))
                queue.append(neighbor)
        graph[node] = ("black", graph[node][1])
    return bfs_result
def paint_all_white(graph):
    for node in graph:
        graph[node] = ('white', graph[node][1])
def dfs(node):
    graph[node] = ("grey", graph[node][1])
    for neighbor in graph[node][1]:
        if graph[neighbor][0] == "white":
            dfs(neighbor)
        elif graph[neighbor][0] == "grey":
            print(f"Cycle detected in node {neighbor}")
    graph[node] = ("black", graph[node][1])
if __name__ == "__main__":
    debug = len(sys.argv) > 3
    graph = read(sys.argv[1], debug)
    root_node = sys.argv[2]
    if debug:
        dump(graph)
    print("Root node:", root_node)
    graph[root_node] = ('black', graph[root_node][1])
    bfs_result = bfs(graph, root_node)
    print("BFS Result:")
    print(bfs_result)
    if debug:
        dump(graph)
    paint_all_white(graph)
    if debug:
        dump(graph)
    print("DFS Result:")
    dfs(root_node)
    if debug:
        dump(graph)
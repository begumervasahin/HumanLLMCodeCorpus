import sys
def read(filename, debug=False):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            l = line.strip().split(" ")
            if debug:
                print("l:", l, "len(l):", len(l))
            if l == ['']:
                continue
            graph[l[0]] = ('white', l[1:])
    return graph
def dump(graph):
    print("Dumping graph: nodeName (color, [adj list])")
    for node in graph:
        print(node, graph[node])
def bfs(graph, root):
    queue = [(root, 0)]
    graph[root] = ("black", graph[root][1], 0)
    result = []
    if len(graph[root][1]) == 0:
        return result
    while queue:
        node, distance = queue.pop(0)
        for i in graph[node][1]:
            if graph[i][0] == "white":
                graph[i] = ('grey', graph[i][1], distance + 1)
                result.append((i, graph[i][2]))
                queue.append((i, distance + 1))
        graph[node] = ("black", graph[node][1], distance)
    return result
def white(graph):
    for node in graph:
        graph[node] = ('white', graph[node][1])
def dfs(graph, root):
    graph[root] = ("grey", graph[root][1])
    for v in graph[root][1]:
        if graph[v][0] == "white":
            dfs(graph, v)
        if graph[v][0] == "grey":
            print("Cycle in {}".format(v))
    graph[root] = ("black", graph[root][1])
if __name__ == "__main__":
    debug = len(sys.argv) > 4
    graph = read(sys.argv[1], debug)
    root = sys.argv[2]
    if debug:
        dump(graph)
    print("Root key:", root)
    graph[root] = ('black', graph[root][1])
    bfs_result = bfs(graph, root)
    print("BFS")
    print(bfs_result)
    if debug:
        dump(graph)
    white(graph)
    if debug:
        dump(graph)
    print("DFS")
    dfs(graph, root)
    if debug:
        dump(graph)
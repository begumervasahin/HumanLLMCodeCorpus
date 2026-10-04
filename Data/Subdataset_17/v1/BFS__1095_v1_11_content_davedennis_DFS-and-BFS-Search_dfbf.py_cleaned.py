import sys
def read(fnm, db):
    file = open(fnm)
    graph = {}
    for line in file:
        l = line.strip().split(" ")
        if db:
            print("l:", l, "len(l):", len(l))
        if l == ['']: continue
        graph[l[0]] = ('white', l[1:])
    return graph
def dump(graph):
    print("Dumping graph: nodeName (color, [adj list])")
    for node in graph:
        print(node, graph[node])
def bfs(graph, start_node):
    queue = []
    queue.append(start_node)
    graph[start_node] = ("black", graph[start_node][1], 0)
    bfs_list = [(start_node, 0)]
    while queue:
        node = queue.pop(0)
        for i in graph[node][1]:
            if graph[i][0] == "white":
                graph[i] = ('grey', graph[i][1], graph[node][2] + 1)
                bfs_list.append((i, graph[i][2]))
                queue.append(i)
        graph[node] = ("black", graph[node][1])
    return bfs_list
def white(graph):
    for node in graph:
        graph[node] = ('white', graph[node][1])
def dfs(graph, node):
    graph[node] = ("grey", graph[node][1])
    for v in graph[node][1]:
        if graph[v][0] == "white":
            dfs(graph, v)
        if graph[v][0] == "grey":
            print("Cycle in {}".format(v))
    graph[node] = ("black", graph[node][1])
if __name__ == "__main__":
    db = len(sys.argv) > 3
    graph = read(sys.argv[1], db)
    root = sys.argv[2]
    if db:
        dump(graph)
    print("Root key:", root)
    graph[root] = ('black', graph[root][1])
    bfs_result = bfs(graph, root)
    print("BFS")
    print(bfs_result)
    if db:
        dump(graph)
    white(graph)
    if db:
        dump(graph)
    print("DFS")
    dfs(graph, root)
    if db:
        dump(graph)
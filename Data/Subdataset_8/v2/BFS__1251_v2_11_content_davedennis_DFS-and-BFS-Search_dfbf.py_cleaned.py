import sys
def read_graph(filename, debug=False):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            nodes = line.strip().split(" ")
            if nodes == ['']:
                continue
            node_name = nodes[0]
            adjacent_nodes = nodes[1:]
            graph[node_name] = ('white', adjacent_nodes)
            if debug:
                print("Node:", node_name, "Adjacent nodes:", adjacent_nodes)
    return graph
def print_graph(graph):
    print("Graph Contents: Node (Color, [Adjacent Nodes])")
    for node, data in graph.items():
        print(node, data)
def bfs(graph, root):
    queue = [(root, 0)]
    graph[root] = ("black", graph[root][1], 0)
    result = []
    if len(graph[root][1]) == 0:
        return result
    while queue:
        node, distance = queue.pop(0)
        for neighbor in graph[node][1]:
            if graph[neighbor][0] == "white":
                graph[neighbor] = ('grey', graph[neighbor][1], distance + 1)
                result.append((neighbor, distance + 1))
                queue.append((neighbor, distance + 1))
        graph[node] = ("black", graph[node][1], distance)
    return result
def dfs(graph, root):
    graph[root] = ("grey", graph[root][1])
    for neighbor in graph[root][1]:
        if graph[neighbor][0] == "white":
            dfs(graph, neighbor)
        if graph[neighbor][0] == "grey":
            print("Cycle detected in node:", neighbor)
    graph[root] = ("black", graph[root][1])
if __name__ == "__main__":
    debug = len(sys.argv) > 4
    graph = read_graph(sys.argv[1], debug)
    root = sys.argv[2]
    print("Root key:", root)
    graph[root] = ('black', graph[root][1])
    bfs_result = bfs(graph, root)
    print("BFS Result:")
    print(bfs_result)
    for node in graph:
        graph[node] = ('white', graph[node][1])
    print("DFS Result:")
    dfs(graph, root)
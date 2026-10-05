import sys
def read_graph(file_name, debug=False):
    graph = {}
    with open(file_name) as file:
        for line in file:
            parts = line.strip().split(" ")
            if not parts:
                continue
            node_name, adjacent_nodes = parts[0], parts[1:]
            graph[node_name] = ('white', adjacent_nodes)
            if debug:
                print("Node:", node_name, "Adjacent Nodes:", adjacent_nodes)
    return graph
def print_graph(graph):
    print("Graph Structure: nodeName (color, [adjacent nodes])")
    for node, data in graph.items():
        print(node, data)
def bfs(graph, root):
    queue = []
    queue.append(root)
    graph[root] = ("black", graph[root][1], 0)
    if not graph[root][1]:
        return []
    result = [(root, 0)]
    while queue:
        node = queue.pop(0)
        for adj_node in graph[node][1]:
            if graph[adj_node][0] == "white":
                graph[adj_node] = ('grey', graph[adj_node][1], graph[node][2] + 1)
                result.append((adj_node, graph[adj_node][2]))
                queue.append(adj_node)
        graph[node] = ("black", graph[node][1])
    return result
def dfs(graph, root):
    visited = set()
    def dfs_helper(node):
        visited.add(node)
        graph[node] = ("grey", graph[node][1])
        for adj_node in graph[node][1]:
            if adj_node not in visited:
                dfs_helper(adj_node)
            elif graph[adj_node][0] == "grey":
                print("Cycle detected in {}".format(adj_node))
        graph[node] = ("black", graph[node][1])
    dfs_helper(root)
if __name__ == "__main__":
    debug = len(sys.argv) > 3
    graph_file = sys.argv[1]
    root_node = sys.argv[2]
    graph = read_graph(graph_file, debug)
    if debug:
        print_graph(graph)
    print("Root node:", root_node)
    graph[root_node] = ('black', graph[root_node][1])
    bfs_result = bfs(graph, root_node)
    print("BFS Result:")
    print(bfs_result)
    if debug:
        print_graph(graph)
    for node in graph:
        graph[node] = ('white', graph[node][1])
    print("DFS:")
    dfs(graph, root_node)
    if debug:
        print_graph(graph)
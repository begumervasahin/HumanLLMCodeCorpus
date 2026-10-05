import sys
def read_graph(filename, debug=False):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            nodes = line.strip().split(" ")
            if not nodes:
                continue
            node_name = nodes[0]
            adjacent_nodes = nodes[1:]
            graph[node_name] = {
                'color': 'white',
                'adjacent_nodes': adjacent_nodes
            }
            if debug:
                print("Node:", node_name, "Adjacent nodes:", adjacent_nodes)
    return graph
def print_graph(graph):
    print("Graph Contents: Node (Color, [Adjacent Nodes])")
    for node, data in graph.items():
        print(node, data)
def bfs(graph, root):
    queue = [(root, 0)]
    graph[root]['color'] = "black"
    result = []
    if not graph[root]['adjacent_nodes']:
        return result
    while queue:
        node, distance = queue.pop(0)
        for neighbor in graph[node]['adjacent_nodes']:
            if graph[neighbor]['color'] == "white":
                graph[neighbor]['color'] = 'grey'
                result.append((neighbor, distance + 1))
                queue.append((neighbor, distance + 1))
        graph[node]['color'] = "black"
    return result
def dfs(graph, root, parent=None):
    graph[root]['color'] = "grey"
    for neighbor in graph[root]['adjacent_nodes']:
        if graph[neighbor]['color'] == "white":
            dfs(graph, neighbor, root)
        elif graph[neighbor]['color'] == "grey" and neighbor != parent:
            print("Cycle detected between nodes:", root, "and", neighbor)
    graph[root]['color'] = "black"
if __name__ == "__main__":
    debug = len(sys.argv) > 4
    graph = read_graph(sys.argv[1], debug)
    root = sys.argv[2]
    print("Root key:", root)
    bfs_result = bfs(graph, root)
    print("BFS Result:")
    print(bfs_result)
    for node in graph:
        graph[node]['color'] = 'white'
    print("DFS Result:")
    dfs(graph, root)
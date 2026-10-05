import queue
def find_max(a, b):
    return max(a, b)
def write_output(distances, farthest_node, parents):
    with open('output.txt', 'w') as output_file:
        output_file.write(str(distances[farthest_node]) + '\n')
        node = farthest_node
        output_file.write(str(farthest_node) + ' ')
        while parents[node] != -1:
            output_file.write(str(parents[node] + 1) + ' ')
            node = parents[node]
def bfs(graph, start_node):
    q = queue.Queue()
    q.put(start_node)
    num_nodes = len(graph)
    distances = [-1] * num_nodes
    visited = [False] * num_nodes
    parents = [None] * num_nodes
    distances[start_node] = 0
    visited[start_node] = True
    parents[start_node] = -1
    while not q.empty():
        node = q.get()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[node] + 1
                parents[neighbor] = node
                q.put(neighbor)
    farthest_node = start_node
    for node in range(num_nodes):
        if distances[node] > distances[farthest_node]:
            farthest_node = node
    write_output(distances, farthest_node, parents)
if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        num_edges, start_node = map(int, input_file.readline().split())
        start_node -= 1
        num_nodes = 0
        pairs = []
        for _ in range(num_edges):
            from_node, to_node = map(int, input_file.readline().split())
            pairs.append((from_node, to_node))
            num_nodes = find_max(num_nodes, find_max(pairs[-1][0], pairs[-1][1]))
        graph = [[] for _ in range(num_nodes)]
        for from_node, to_node in pairs:
            graph[from_node - 1].append(to_node - 1)
    bfs(graph, start_node)
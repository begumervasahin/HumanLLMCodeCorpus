import queue
def max(a, b):
    return a if a >= b else b
def output(dist, farthest_node, parents):
    with open('output.txt', 'w') as output_file:
        output_file.write(f"{dist}\n")
        node = farthest_node
        path = []
        while node != -1:
            path.append(node + 1)
            node = parents[node]
        output_file.write(' '.join(map(str, path[::-1])) + '\n')
def bfs(graph, start, nodes):
    q = queue.Queue()
    q.put(start)
    distances = [-1] * nodes
    visited = [False] * nodes
    parents = [None] * nodes
    distances[start] = 0
    visited[start] = True
    parents[start] = -1
    while not q.empty():
        node = q.get()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[node] + 1
                parents[neighbor] = node
                q.put(neighbor)
    farthest_node = distances.index(max(distances))
    output(distances[farthest_node], farthest_node, parents)
def read_input_file(filename):
    with open(filename, 'r') as input_file:
        edges, start = map(int, input_file.readline().split())
        start -= 1
        nodes = 0
        pairs = []
        for _ in range(edges):
            f, t = map(int, input_file.readline().split())
            pairs.append((f - 1, t - 1))
            nodes = max(nodes, max(f, t))
        graph = [[] for _ in range(nodes)]
        for f, t in pairs:
            graph[f].append(t)
    return graph, start, nodes
if __name__ == "__main__":
    graph, start, nodes = read_input_file('input.txt')
    bfs(graph, start, nodes)
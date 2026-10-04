import queue
def max(a, b):
    return a if a >= b else b
def output(dist, farthest_node, parents):
    with open('output.txt', 'w') as output:
        output.write(str(dist) + '\n')
        node = farthest_node
        output.write(str(farthest_node + 1) + ' ')
        while parents[node] != -1:
            output.write(str(parents[node] + 1) + ' ')
            node = parents[node]
def bfs(graph, start):
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
    farthest_node = start
    for node in range(nodes):
        if distances[node] > distances[farthest_node]:
            farthest_node = node
    output(distances[farthest_node], farthest_node, parents)
with open('input.txt', 'r') as input_file:
    edges, start = map(int, input_file.readline().split())
    start -= 1
    nodes = 0
    pairs = []
    for _ in range(edges):
        f, t = map(int, input_file.readline().split())
        pairs.append((f, t))
        nodes = max(nodes, max(f, t))
    graph = [[] for _ in range(nodes)]
    for f, t in pairs:
        graph[f - 1].append(t - 1)
bfs(graph, start)
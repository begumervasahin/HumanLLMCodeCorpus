import queue
def max(a, b):
    if a >= b:
        return a
    else:
        return b
def output(dist, farthest_node, parents):
    with open('output.txt', 'w') as output_file:
        output_file.write(str(dist) + '\n')
        node = farthest_node
        output_file.write(str(farthest_node) + ' ')
        while parents[node] != -1:
            output_file.write(str(parents[node] + 1) + ' ')
            node = parents[node]
def bfs(graph, start):
    q = queue.Queue()
    q.put(start)
    nodes = len(graph)
    dist = [-1] * nodes
    used = [False] * nodes
    parents = [None] * nodes
    dist[start] = 0
    used[start] = True
    parents[start] = -1
    while not q.empty():
        node = q.get()
        for neighbor in graph[node]:
            if not used[neighbor]:
                used[neighbor] = True
                dist[neighbor] = dist[node] + 1
                parents[neighbor] = node
                q.put(neighbor)
    farthest_node = start
    for node in range(nodes):
        if dist[node] > dist[farthest_node]:
            farthest_node = node
    output(dist[farthest_node], farthest_node, parents)
if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        edges, start = map(int, input_file.readline().split())
        start -= 1
        nodes = 0
        pair = []
        for _ in range(edges):
            f, t = map(int, input_file.readline().split())
            pair.append((f, t))
            nodes = max(nodes, max(pair[-1][0], pair[-1][1]))
        graph = [[] for _ in range(nodes)]
        for f, t in pair:
            graph[f - 1].append(t - 1)
    bfs(graph, start)
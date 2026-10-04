import queue
def max(a, b):
    return a if a >= b else b
def output(dist, farthest_node, parents):
    with open('output.txt', 'w') as output:
        output.write(str(dist) + '\n')
        node = farthest_node
        path = []
        while node != -1:
            path.append(node + 1)
            node = parents[node]
        output.write(' '.join(map(str, path[::-1])))
def bfs(graph, start, nodes):
    q = queue.Queue()
    q.put(start)
    d = [-1] * nodes
    used = [False] * nodes
    p = [None] * nodes
    d[start] = 0
    used[start] = True
    p[start] = -1
    while not q.empty():
        node = q.get()
        for to in graph[node]:
            if not used[to]:
                used[to] = True
                d[to] = d[node] + 1
                p[to] = node
                q.put(to)
    farthest_node = start
    for node in range(nodes):
        if d[node] > d[farthest_node]:
            farthest_node = node
    output(d[farthest_node], farthest_node, p)
def main():
    with open('input.txt', 'r') as input:
        edges, start = map(int, input.readline().split())
        start = start - 1
        nodes = 0
        pair = []
        for i in range(edges):
            f, t = map(int, input.readline().split())
            pair.append((f - 1, t - 1))
            nodes = max(nodes, max(f, t))
        nodes += 1
        graph = [[] for _ in range(nodes)]
        for f, t in pair:
            graph[f].append(t)
    bfs(graph, start, nodes)
if __name__ == "__main__":
    main()
def fonk1(graph, source):
    b1 = {}
    b2 = {}
    for node in graph:
        b1[node] = float('Inf')
        b2[node] = None
    b1[source] = 0
    return b1, b2
def fonk2(node, neighbour, graph, b1, b2):
    if b1[neighbour] > b1[node] + graph[node][neighbour]:
        b1[neighbour] = b1[node] + graph[node][neighbour]
        b2[neighbour] = node
def fonk3(graph, source):
    b1, b2 = fonk1(graph, source)
    for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                fonk2(u, v, graph, b1, b2)
    for u in graph:
        for v in graph[u]:
            if b1[v] > b1[u] + graph[u][v]:
                raise RuntimeError('Negative cycle detected, cannot find the shortest paths')
    return b1, b2
import pdb
def initialize(graph, source):
    d = {}
    p = {}
    for node in graph:
        d[node] = float('Inf')
        p[node] = None
    d[source] = 0
    return d, p
def relax(node, neighbour, graph, d, p):
    if d[neighbour] > d[node] + graph[node][neighbour]:
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node
def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, d, p)
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]
    return d, p
def test():
    graph = {
        'a': {'b': -2, 'c': 1, 'd': 4},
        'b': {'e': 3},
        'c': {'b': -3, 'd': 2},
        'd': {'e': -1},
        'e': {'c': 5}
        }
    d, p = bellman_ford(graph, 'a')
    print ("The shortest distance from source a to all other nodes is:")
    for u in graph:
        print(u,"=",d[u])
    print ("Paths from source a to all other nodes(predecessors of nodes):")
    for u in graph:
        print(u,"=",p[u])
if __name__ == '__main__': test()
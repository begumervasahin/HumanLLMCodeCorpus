def popmin(pqueue):
    lowest = 1000
    keylowest = None
    for key in pqueue:
        if pqueue[key] < lowest:
            lowest = pqueue[key]
            keylowest = key
    del pqueue[keylowest]
    return keylowest
def dijkstra(graph, start):
    pqueue = {}
    dist = {}
    pred = {}
    for v in graph:
        dist[v] = 1000
        pred[v] = -1
    dist[start] = 0
    for v in graph:
       pqueue[v] = dist[v]
    while pqueue:
        u = popmin(pqueue)
        for v in graph[u].keys():
            w = graph[u][v]
            newdist = dist[u] + w
            if (newdist < dist[v]):
                pqueue[v] = newdist
                dist[v] = newdist
                pred[v] = u
    return dist, pred
graph = {
    0 : {1:6, 2:1, 3:4},
    1 : {4:3},
    2 : {1:-3, 3:2},
    3 : {4:-1},
    4 : {2:5},
}
dist, pred = dijkstra(graph, 0)
print ("Shortest distance from start node 0 to all other nodes is:")
for v in dist:
    print (v,'=',dist[v])
print ("Paths from start noe to all other nodes (predecessors of nodes):")
for v in pred:
    print (v,'=',pred[v])
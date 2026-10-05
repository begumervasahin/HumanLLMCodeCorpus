from collections import defaultdict
from heapq import *
def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))
    q, seen = [(0, f, ())], set()
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t:
                return (cost, path)
            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))
    return float("inf")
edges = [
    ('A', 'B', 1),
    ('B', 'C', 2),
    ('A', 'C', 4),
    ('B', 'D', 5),
    ('C', 'D', 1)
]
source = 'A'
target = 'D'
cost, path = dijkstra(edges, source, target)
if cost != float("inf"):
    print("Shortest path from {} to {}: Cost = {}".format(source, target, cost))
    print("Path:", ' -> '.join(path[0]), "=", path[1])
else:
    print("There is no path from {} to {}.".format(source, target))
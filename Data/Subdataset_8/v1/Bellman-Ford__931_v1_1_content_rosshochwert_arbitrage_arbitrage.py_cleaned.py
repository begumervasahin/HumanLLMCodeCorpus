import math
import urllib.request
import json
import re
def download():
    graph = {}
    page = urllib.request.urlopen("http:
    jsrates = json.loads(page.read().decode())
    pattern = re.compile("([A-Z]{3})_([A-Z]{3})")
    for key in jsrates:
        matches = pattern.match(key)
        conversion_rate = -math.log(float(jsrates[key]))
        from_rate = matches.group(1)
        to_rate = matches.group(2)
        if from_rate != to_rate:
            if from_rate not in graph:
                graph[from_rate] = {}
            graph[from_rate][to_rate] = float(conversion_rate)
    return graph
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
        d[neighbour] = d[node] + graph[node][neighbour]
        p[neighbour] = node
def retrace_negative_loop(p, start):
    arbitrageLoop = [start]
    next_node = start
    while True:
        next_node = p[next_node]
        if next_node not in arbitrageLoop:
            arbitrageLoop.append(next_node)
        else:
            arbitrageLoop.append(next_node)
            arbitrageLoop = arbitrageLoop[arbitrageLoop.index(next_node):]
            return arbitrageLoop
def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, d, p)
    for u in graph:
        for v in graph[u]:
            if d[v] < d[u] + graph[u][v]:
                return retrace_negative_loop(p, source)
    return None
paths = []
graph = download()
for key in graph:
    path = bellman_ford(graph, key)
    if path and path not in paths:
        paths.append(path)
for path in paths:
    if not path:
        print("No opportunity here :(")
    else:
        money = 100
        print("Starting with {} in {}".format(money, path[0]))
        for i, value in enumerate(path):
            if i + 1 < len(path):
                start = path[i]
                end = path[i + 1]
                rate = math.exp(-graph[start][end])
                money *= rate
                print("{} to {} at {} = {}".format(start, end, rate, money))
    print("\n")
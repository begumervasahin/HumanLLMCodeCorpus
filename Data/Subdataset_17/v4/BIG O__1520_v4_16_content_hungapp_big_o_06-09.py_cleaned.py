import queue
INF = int(1e9)
class Node:
    def __init__(self, cell, time):
        self.cell = cell
        self.time = time
    def __lt__(self, other):
        return self.time <= other.time
def dijkstra(start):
    pq = queue.PriorityQueue()
    pq.put(Node(start, 0))
    time[start] = 0
    while not pq.empty():
        top = pq.get()
        u = top.cell
        w = top.time
        for neighbor in graph[u]:
            if w + neighbor.time < time[neighbor.cell]:
                time[neighbor.cell] = w + neighbor.time
                pq.put(Node(neighbor.cell, time[neighbor.cell]))
def main_task1():
    n = int(input())
    e = int(input())
    t = int(input())
    m = int(input())
    global graph, time
    graph = [[] for _ in range(n + 1)]
    time = [INF for _ in range(n + 1)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[b].append(Node(a, w))
    dijkstra(e)
    count = sum(1 for i in range(1, n + 1) if time[i] <= t)
    print(count)
class CityNode:
    def __init__(self, city, cost):
        self.city = city
        self.cost = cost
    def __lt__(self, other):
        return self.cost <= other.cost
def dijkstra_path(s, f):
    pq = queue.PriorityQueue()
    pq.put(CityNode(s, 0))
    cost[s] = 0
    while not pq.empty():
        top = pq.get()
        u = top.city
        w = top.cost
        if u == f:
            return
        for neighbor in graph[u]:
            if w + neighbor.cost < cost[neighbor.city]:
                cost[neighbor.city] = w + neighbor.cost
                pq.put(CityNode(neighbor.city, cost[neighbor.city]))
def main_task2():
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        global graph
        graph = [[] for _ in range(n + 1)]
        cities = []
        for i in range(n):
            city = input().strip()
            cities.append(city)
            p = int(input())
            for _ in range(p):
                nr, c = map(int, input().split())
                graph[i + 1].append(CityNode(nr, c))
        r = int(input())
        for _ in range(r):
            global cost
            cost = [INF for _ in range(n + 1)]
            source, destination = input().split()
            start = cities.index(source) + 1
            end = cities.index(destination) + 1
            dijkstra_path(start, end)
            print(cost[end])
class DistNode:
    def __init__(self, city, dist):
        self.city = city
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist
def dijkstra_dist(s, distance):
    pq = queue.PriorityQueue()
    pq.put(DistNode(s, 0))
    distance[s] = 0
    while not pq.empty():
        top = pq.get()
        u = top.city
        w = top.dist
        for neighbor in graph[u]:
            if w + neighbor.dist < distance[neighbor.city]:
                distance[neighbor.city] = w + neighbor.dist
                pq.put(DistNode(neighbor.city, distance[neighbor.city]))
def main_task3():
    n, m, k, x = map(int, input().split())
    ks = list(map(int, input().split()))
    global graph
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, d = map(int, input().split())
        graph[u].append(DistNode(v, d))
        graph[v].append(DistNode(u, d))
    a, b = map(int, input().split())
    distA = [INF for _ in range(n + 1)]
    dijkstra_dist(a, distA)
    distB = [INF for _ in range(n + 1)]
    dijkstra_dist(b, distB)
    min_time = min((distA[ks[i]] + distB[ks[i]] for i in range(k) if distB[ks[i]] <= x), default=INF)
    print(min_time if min_time < INF else -1)
def bfs(s, distance):
    q = queue.Queue()
    q.put(s)
    distance[s] = 0
    while not q.empty():
        u = q.get()
        for neighbor in graph[u]:
            if distance[neighbor] == INF:
                distance[neighbor] = distance[u] + 1
                q.put(neighbor)
def main_task4():
    t = int(input())
    for c in range(t):
        n = int(input())
        global graph
        graph = [[] for _ in range(n)]
        r = int(input())
        for _ in range(r):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        s, d = map(int, input().split())
        distS = [INF for _ in range(n)]
        distD = [INF for _ in range(n)]
        bfs(s, distS)
        bfs(d, distD)
        max_time = max(distS[i] + distD[i] for i in range(n) if distS[i] != INF and distD[i] != INF)
        print(f'Case {c + 1}: {max_time}')
if __name__ == "__main__":
    main_task1()
    main_task2()
    main_task3()
    main_task4()
import queue
INF = int(1e9)
class Node:
  def __init__(self, cell, time):
    self.cell = cell
    self.time = time
  def __lt__(self, other):
    return self.time <= other.time
def Dijkstra(e):
  pq = queue.PriorityQueue()
  pq.put(Node(e, 0))
  time[e] = 0
  while pq.empty() == False:
    top = pq.get()
    u = top.cell
    w = top.time
    for neighbor in graph[u]:
      if w + neighbor.time  < time[neighbor.cell]:
        time[neighbor.cell] = w + neighbor.time
        pq.put(Node(neighbor.cell, time[neighbor.cell]))
n = int(input())
e = int(input())
t = int(input())
m = int(input())
graph = [[] for i in range(n + 1)]
time = [INF for i in range(n + 1)]
for _ in range(m):
  a, b, w = map(int, input().split())
  graph[b].append(Node(a, w))
Dijkstra(e)
c = 0
for i in range(1, n + 1):
  if time[i] <= t:
    c += 1
print(c)
import queue
INF = int(1e9)
class Node:
  def __init__(self, city, cost):
    self.city = city
    self.cost = cost
  def __lt__(self, other):
    return self.cost <= other.cost
def Dijkstra(s, f):
  pq = queue.PriorityQueue()
  pq.put(Node(s, 0))
  cost[s] = 0
  while pq.empty() == False:
    top = pq.get()
    u = top.city
    w = top.cost
    if u == f:
      return
    for neighbor in graph[u]:
      if w + neighbor.cost  < cost[neighbor.city]:
        cost[neighbor.city] = w + neighbor.cost
        pq.put(Node(neighbor.city, cost[neighbor.city]))
tc = int(input())
for _ in range(tc):
  n = int(input())
  graph = [[] for i in range(n + 1)]
  cities = []
  for i in range(n):
    city = input()
    cities.append(city)
    p = int(input())
    for j in range(p):
      nr, c = map(int, input().split())
      graph[i + 1].append(Node(nr, c))
  r = int(input())
  for i in range(r):
    cost = [INF for j in range(n + 1)]
    source, destination = input().split()
    start = cities.index(source) + 1
    end = cities.index(destination) + 1
    Dijkstra(start, end)
    print(cost[end])
  input()
import queue
INF = int(1e9)
class Node:
  def __init__(self, city, dist):
    self.city = city
    self.dist = dist
  def __lt__(self, other):
    return self.dist <= other.dist
def Dijkstra(s, distance):
  pq = queue.PriorityQueue()
  pq.put(Node(s, 0))
  distance[s] = 0
  while pq.empty() == False:
    top = pq.get()
    u = top.city
    w = top.dist
    for neighbor in graph[u]:
      if w + neighbor.dist < distance[neighbor.city]:
        distance[neighbor.city] = w + neighbor.dist
        pq.put(Node(neighbor.city, distance[neighbor.city]))
n, m, k, x = map(int, input().split())
ks = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(m):
  u, v, d = map(int, input().split())
  graph[u].append(Node(v, d))
  graph[v].append(Node(u, d))
a, b = map(int, input().split())
distA = [INF for _ in range(n + 1)]
Dijkstra(a, distA)
distB = [INF for _ in range(n + 1)]
Dijkstra(b, distB)
min_time = INF
for i in range(k):
  if distB[ks[i]] <= x:
    min_time = min(min_time, distA[ks[i]] + distB[ks[i]])
if min_time < INF:
  print(min_time)
else:
  print(-1)
import queue
INF = int(1e9)
def BFS(s, distance):
  pq = queue.Queue()
  pq.put(s)
  distance[s] = 0
  while pq.empty() == False:
    u = pq.get()
    for neighbor in graph[u]:
      if distance[neighbor] == INF:
        distance[neighbor] = distance[u] + 1
        pq.put(neighbor)
t = int(input())
for c in range(t):
  n = int(input())
  graph = [[] for _ in range(n)]
  r = int(input())
  for i in range(r):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
  s, d = map(int, input().split())
  distS = [INF for _ in range(n)]
  distD = [INF for _ in range(n)]
  BFS(s, distS)
  BFS(d, distD)
  max_time = 0
  for i in range(n):
    if distS[i] != INF and distD[i] != INF:
      max_time = max(max_time, distS[i] + distD[i])
  print('Case {}: {}'.format(c + 1, max_time))
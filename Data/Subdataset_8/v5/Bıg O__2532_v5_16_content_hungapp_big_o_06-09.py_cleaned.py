import queue
INF = int(1e9)
class Node:
    def __init__(self, city, cost):
        self.city = city
        self.cost = cost
    def __lt__(self, other):
        return self.cost <= other.cost
def dijkstra(graph, start, end):
    pq = queue.PriorityQueue()
    pq.put(Node(start, 0))
    cost = [INF] * len(graph)
    cost[start] = 0
    while not pq.empty():
        top = pq.get()
        u = top.city
        w = top.cost
        if u == end:
            return cost[end]
        for neighbor in graph[u]:
            if w + neighbor.cost < cost[neighbor.city]:
                cost[neighbor.city] = w + neighbor.cost
                pq.put(Node(neighbor.city, cost[neighbor.city]))
def process_test_case():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    cities = []
    for i in range(n):
        city = input()
        cities.append(city)
        p = int(input())
        for _ in range(p):
            nr, c = map(int, input().split())
            graph[i + 1].append(Node(nr, c))
    r = int(input())
    for _ in range(r):
        source, destination = input().split()
        start = cities.index(source) + 1
        end = cities.index(destination) + 1
        shortest_path_cost = dijkstra(graph, start, end)
        print(shortest_path_cost)
def main():
    tc = int(input())
    for _ in range(tc):
        process_test_case()
        if _ < tc - 1:
            input()
if __name__ == "__main__":
    main()
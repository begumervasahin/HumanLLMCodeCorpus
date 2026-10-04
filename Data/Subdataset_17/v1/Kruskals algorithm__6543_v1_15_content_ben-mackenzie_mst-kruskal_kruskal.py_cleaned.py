import heapq
class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    def make_group(self, item):
        self.parent[item] = item
        self.rank[item] = 0
        return item
    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    def union_sets(self, item1, item2):
        root1 = self.find(item1)
        root2 = self.find(item2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1
class HeapPriorityQueue:
    def __init__(self):
        self.heap = []
    def insert(self, item):
        heapq.heappush(self.heap, item)
    def delete_min(self):
        return heapq.heappop(self.heap)
    def is_empty(self):
        return len(self.heap) == 0
def MST_Kruskal(graph):
    tree = []
    pq = HeapPriorityQueue()
    forest = DisjointSet()
    position = {}
    for v in graph['V']:
        position[v] = forest.make_group(v)
    for edge in graph['E']:
        pq.insert(edge)
    size = len(graph['V'])
    total_weight = 0
    while len(tree) != size - 1 and not pq.is_empty():
        weight, u, v = pq.delete_min()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append((u, v, weight))
            total_weight += weight
            forest.union_sets(a, b)
    return tree, total_weight
graph = {
    'V': ['A', 'B', 'C', 'D', 'E'],
    'E': [
        (1, 'A', 'B'),
        (2, 'B', 'C'),
        (3, 'C', 'D'),
        (4, 'D', 'E'),
        (5, 'A', 'E'),
        (6, 'B', 'D')
    ]
}
mst, total_weight = MST_Kruskal(graph)
print("Minimum Spanning Tree:", mst)
print("Total Weight of MST:", total_weight)
import heapq
class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    def make_group(self, item):
        self.parent[item] = item
        self.rank[item] = 0
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
def kruskal_mst(graph):
    mst = []
    pq = HeapPriorityQueue()
    disjoint_set = DisjointSet()
    for vertex in graph['V']:
        disjoint_set.make_group(vertex)
    for edge in graph['E']:
        pq.insert(edge)
    total_weight = 0
    while len(mst) < len(graph['V']) - 1 and not pq.is_empty():
        weight, u, v = pq.delete_min()
        root_u = disjoint_set.find(u)
        root_v = disjoint_set.find(v)
        if root_u != root_v:
            mst.append((u, v, weight))
            total_weight += weight
            disjoint_set.union_sets(root_u, root_v)
    return mst, total_weight
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
mst, total_weight = kruskal_mst(graph)
print("Minimum Spanning Tree:", mst)
print("Total Weight of MST:", total_weight)
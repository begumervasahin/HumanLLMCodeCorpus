class Graph:
    def __init__(self, nodes):
        self.V = nodes
        self.edges = []
    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
    def kruskal_mst(self):
        mst = []
        self.edges.sort(key=lambda edge: edge[2])
        parent = list(range(self.V))
        rank = [0] * self.V
        for u, v, w in self.edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)
            if root_u != root_v:
                mst.append((u, v, w))
                self.union(parent, rank, root_u, root_v)
            if len(mst) == self.V - 1:
                break
        print("Resulting Minimum Spanning Tree (MST):")
        total_weight = 0
        for u, v, w in mst:
            print(f"{u} -- {v} == weight: {w}")
            total_weight += w
        print(f"The total weight of the MST is {total_weight}")
        return mst
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 9)
    g.add_edge(0, 2, 7)
    g.add_edge(0, 3, 2)
    g.add_edge(1, 2, 2)
    g.add_edge(2, 3, 2)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 3)
    g.add_edge(3, 4, 3)
    g.kruskal_mst()
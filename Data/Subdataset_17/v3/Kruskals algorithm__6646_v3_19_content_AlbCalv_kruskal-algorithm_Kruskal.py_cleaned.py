class Graph:
    def __init__(self, nodes):
        self.num_nodes = nodes
        self.edges = []
    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))
    def find(self, parent, node):
        if parent[node] != node:
            parent[node] = self.find(parent, parent[node])
        return parent[node]
    def union(self, parent, rank, root1, root2):
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root2] = root1
            rank[root1] += 1
    def kruskal_mst(self):
        mst = []
        self.edges.sort(key=lambda edge: edge[2])
        parent = list(range(self.num_nodes))
        rank = [0] * self.num_nodes
        for u, v, w in self.edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)
            if root_u != root_v:
                mst.append((u, v, w))
                self.union(parent, rank, root_u, root_v)
                if len(mst) == self.num_nodes - 1:
                    break
        self._print_mst(mst)
        return mst
    def _print_mst(self, mst):
        print("Resulting Minimum Spanning Tree (MST):")
        total_weight = sum(weight for _, _, weight in mst)
        for u, v, weight in mst:
            print(f"{u} -- {v} == weight: {weight}")
        print(f"The total weight of the MST is {total_weight}")
if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0, 1, 9)
    graph.add_edge(0, 2, 7)
    graph.add_edge(0, 3, 2)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 3, 2)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 3)
    graph.add_edge(3, 4, 3)
    graph.kruskal_mst()
import math
from DataGenerator import Adjacency_List, Edge, DataGenerator
class UnionFind:
    def __init__(self, num_vertices):
        self.trees = [Node(i) for i in range(num_vertices)]
    def find(self, i):
        path = []
        root = self.trees[i].get_root(path)
        for node in path:
            node.parent = root
        return root
    def union(self, root_x, root_y, edge, mst):
        mst.add_edge(edge)
        if root_x.rank <= root_y.rank:
            root_y.make_child_of(root_x)
            root_y.rank += 1
        else:
            root_x.make_child_of(root_y)
            root_x.rank += 1
class Node:
    def __init__(self, vertex, parent=None):
        self.vertex = vertex
        self.parent = parent
        self.rank = 1 if parent is None else parent.rank + 1
    def get_root(self, path):
        if self.parent is None:
            return self
        path.append(self)
        return self.parent.get_root(path)
    def make_child_of(self, parent):
        self.parent = parent
def merge_sort(edges, low, high):
    if low < high:
        middle = (low + high)
        merge_sort(edges, low, middle)
        merge_sort(edges, middle + 1, high)
        merge(edges, low, middle, high)
def merge(edges, low, middle, high):
    left = edges[low:middle + 1]
    right = edges[middle + 1:high + 1]
    i = j = 0
    k = low
    while i < len(left) and j < len(right):
        if left[i].weight <= right[j].weight:
            edges[k] = left[i]
            i += 1
        else:
            edges[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        edges[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        edges[k] = right[j]
        j += 1
        k += 1
def kruskal(adj):
    mst = Adjacency_List(adj.get_vertices(), [])
    uf = UnionFind(adj.get_number_of_vertices())
    edges = adj.get_edges()
    merge_sort(edges, 0, len(edges) - 1)
    for edge in edges:
        set_x = uf.find(edge.u)
        set_y = uf.find(edge.v)
        if set_x.vertex != set_y.vertex:
            uf.union(set_x, set_y, edge, mst)
    return mst
if __name__ == '__main__':
    print("Original Adjacency List")
    dg = DataGenerator(100, 0.1, method=2)
    G = dg.generate_data()
    G.print_me()
    mst = kruskal(G)
    print("MST: Kruskal Algorithm")
    mst.print_me()
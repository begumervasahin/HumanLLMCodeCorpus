import math
from DataGenerator import Adjacency_List, Edge, DataGenerator
class MinHeapPrim:
    def __init__(self, vertices):
        self.list = []
        self.positions = []
        self.parents = []
        self.size = len(vertices)
        for i in range(len(vertices)):
            if i == 0:
                self.list.append((0, 0))
                self.positions.append(0)
                self.parents.append(-1)
            else:
                self.list.append((i, math.inf))
                self.positions.append(i)
                self.parents.append(-1)
        self.totalCost = 0
    def print_me(self):
        for vertex, weight in self.list:
            print(f"(v={vertex} w={weight}) ", end='')
        print('')
    def set_parent(self, vertex, parent):
        self.parents[vertex] = parent
    def get_min_node(self, MST, added_vertices):
        smallest = self.list[0][0]
        if self.parents[smallest] != -1 and added_vertices[smallest] == 0:
            MST.addEdge(Edge(self.parents[smallest], smallest, self.list[0][1]))
            added_vertices[smallest] = 1
        self.list[0] = self.list[self.size - 1]
        self.positions[smallest] = -1
        self.positions[self.list[0][0]] = 0
        self.size -= 1
        self.min_heapify(0)
        return smallest
    def min_heapify(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child < self.size and self.list[smallest][1] > self.list[left_child][1]:
            smallest = left_child
        if right_child < self.size and self.list[smallest][1] > self.list[right_child][1]:
            smallest = right_child
        if smallest != index:
            self.swap(index, smallest)
            self.min_heapify(smallest)
    def swap(self, index1, index2):
        self.list[index1], self.list[index2] = self.list[index2], self.list[index1]
        self.positions[self.list[index1][0]], self.positions[self.list[index2][0]] = self.positions[self.list[index2][0]], self.positions[self.list[index1][0]]
    def decrease_key_value(self, index, vertex):
        while index > 0:
            parent_index = (index - 1)
            if self.list[parent_index][1] > self.list[index][1]:
                self.swap(index, parent_index)
                index = parent_index
            else:
                break
    def is_empty(self):
        return self.size == 0
    def get_weight(self, vertex):
        return self.list[self.positions[vertex]][1]
    def update_heap(self, vertex, weight):
        index = self.positions[vertex]
        self.list[index] = (vertex, weight)
        self.decrease_key_value(index, vertex)
def prim(Adj):
    vertices = Adj.getVertices()
    MST = Adjacency_List(vertices, [])
    added_vertices = [0] * len(vertices)
    min_heap = MinHeapPrim(vertices)
    while not min_heap.is_empty():
        u = min_heap.get_min_node(MST, added_vertices)
        for i in range(Adj.numberOfNeighborsTo(u)):
            neighbor, weight = Adj.adjacentTo(u, i)
            if added_vertices[neighbor] == 0 and min_heap.get_weight(neighbor) > weight:
                min_heap.set_parent(neighbor, u)
                min_heap.update_heap(neighbor, weight)
    return MST
if __name__ == '__main__':
    print("Original Adjacency List")
    dg = DataGenerator(100, 0.1, method=2)
    G = dg.generateData()
    G.print_me()
    MST = prim(G)
    print("MST: Prim's Algorithm")
    MST.print_me()
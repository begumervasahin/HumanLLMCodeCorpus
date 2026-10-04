import sys
class Vertex:
    def __init__(self, id, distance=9999999, parent_id=0, position=0):
        self.id = id
        self.distance = distance
        self.parent_id = parent_id
        self.position = position
class Graph:
    def __init__(self, n):
        self.adjacency_list = [[] for _ in range(n)]
    def insert(self, u, v, w):
        vertex = Vertex(id=v, parent_id=u, distance=w)
        self.adjacency_list[u - 1].append(vertex)
class MinHeap:
    def __init__(self):
        self.array = [0]
        self.vertex_vector = []
    def insert(self, vertex):
        self.array.append(vertex)
        self.array[0] = len(self.array) - 1
        self.heapify_up(self.array[0])
        self.vertex_vector[vertex.id - 1].position = self.array[0]
    def heapify_up(self, index):
        while index > 1:
            parent_index = index
            if self.array[parent_index].distance > self.array[index].distance:
                self.swap(parent_index, index)
                index = parent_index
            else:
                break
    def extract_min(self):
        self.swap(1, self.array[0])
        min_vertex = self.array.pop()
        self.array[0] -= 1
        if self.array[0] > 1:
            self.heapify_down(1)
        return min_vertex
    def decrease_key(self, heap_index, updated_distance, parent_id):
        if heap_index > 0:
            self.array[heap_index].distance = updated_distance
            self.array[heap_index].parent_id = parent_id
            self.heapify_up(heap_index)
    def heapify_down(self, index):
        while 2 * index <= self.array[0]:
            child_index = 2 * index
            if child_index < self.array[0] and self.array[child_index + 1].distance < self.array[child_index].distance:
                child_index += 1
            if self.array[child_index].distance < self.array[index].distance:
                self.swap(index, child_index)
                index = child_index
            else:
                break
    def swap(self, i, j):
        self.vertex_vector[self.array[i].id - 1].position = j
        self.vertex_vector[self.array[j].id - 1].position = i
        self.array[i], self.array[j] = self.array[j], self.array[i]
def mst_prim(graph, start_vertex):
    heap = MinHeap()
    heap.insert(start_vertex)
    mst_set = []
    for i in range(len(heap.vertex_vector)):
        if i != start_vertex.id - 1:
            vertex = Vertex(id=i + 1)
            heap.insert(vertex)
    while len(heap.array) > 1:
        min_vertex = heap.extract_min()
        mst_set.append(min_vertex)
        for neighbor in graph.adjacency_list[min_vertex.id - 1]:
            if neighbor.distance < heap.vertex_vector[neighbor.id - 1].distance:
                heap.decrease_key(heap.vertex_vector[neighbor.id - 1].position, neighbor.distance, min_vertex.id)
                heap.vertex_vector[neighbor.id - 1].parent_id = min_vertex.id
    return mst_set
def main():
    input_data = input().split()
    node_num = int(input_data[0])
    edge_num = int(input_data[1])
    graph = Graph(node_num)
    for _ in range(edge_num):
        u, v, w = map(int, input().split())
        graph.insert(u, v, w)
        graph.insert(v, u, w)
    heap = MinHeap()
    for i in range(node_num):
        vertex = Vertex(id=i + 1)
        heap.vertex_vector.append(vertex)
    start_vertex = Vertex(id=1)
    mst = mst_prim(graph, start_vertex)
    total_distance = sum(vertex.distance for vertex in mst if vertex.id != 0 and vertex.parent_id != 0)
    print(total_distance)
if __name__ == "__main__":
    main()
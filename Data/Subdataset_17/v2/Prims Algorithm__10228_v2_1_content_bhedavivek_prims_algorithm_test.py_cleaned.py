import sys
class Graph:
    def __init__(self, n):
        self.adj_list = [[] for _ in range(n)]
    def insert(self, u, v, w):
        vert = Vertex(v, u, w)
        self.adj_list[u - 1].append(vert)
class Vertex:
    def __init__(self, vid=0, parent_id=0, distance=float('inf')):
        self.id = vid
        self.parent_id = parent_id
        self.distance = distance
        self.position = 0
def insert(vert):
    array.append(vert)
    array[0] = len(array) - 1
    heapify_up(array[0])
    vertex_vector[vert.id - 1].position = array[0]
def heapify_up(index):
    while index > 1:
        parent_index = index
        if array[parent_index].distance > array[index].distance:
            swap_positions(index, parent_index)
            index = parent_index
        else:
            break
def extract_min():
    vertex_vector[array[1].id - 1].position = 0
    last_index = array[0]
    vertex_vector[array[last_index].id - 1].position = 1
    min_vertex = array[1]
    array[1] = array[last_index]
    array[0] -= 1
    if array[0] > 1:
        heapify_down(1)
    array.pop()
    return min_vertex
def decrease_key(heap_index, updated_distance, parent_id):
    if heap_index > 0:
        array[heap_index].distance = updated_distance
        array[heap_index].parent_id = parent_id
        heapify_up(heap_index)
def heapify_down(index):
    while 2 * index <= array[0]:
        left_child = 2 * index
        right_child = 2 * index + 1
        smaller_child = left_child
        if right_child <= array[0] and array[right_child].distance < array[left_child].distance:
            smaller_child = right_child
        if array[smaller_child].distance < array[index].distance:
            swap_positions(index, smaller_child)
            index = smaller_child
        else:
            break
def swap_positions(index1, index2):
    vertex_vector[array[index1].id - 1].position = index2
    vertex_vector[array[index2].id - 1].position = index1
    array[index1], array[index2] = array[index2], array[index1]
def mst_prim(g, start_vertex):
    insert(start_vertex)
    mst_set = []
    for i in range(len(vertex_vector)):
        if i != start_vertex.id - 1:
            vert = Vertex(i + 1)
            insert(vert)
    while len(array) > 1:
        min_vertex = extract_min()
        mst_set.append(min_vertex)
        for neighbor in g.adj_list[min_vertex.id - 1]:
            if neighbor.distance < vertex_vector[neighbor.id - 1].distance:
                vertex_vector[neighbor.id - 1].distance = neighbor.distance
                decrease_key(vertex_vector[neighbor.id - 1].position, neighbor.distance, min_vertex.id)
                vertex_vector[neighbor.id - 1].parent_id = min_vertex.id
    return mst_set
if __name__ == "__main__":
    node_num = int(input("Enter the number of nodes: "))
    edge_num = int(input("Enter the number of edges: "))
    g = Graph(node_num)
    for _ in range(edge_num):
        u, v, w = map(int, input("Enter edge (u, v, w): ").split())
        g.insert(u, v, w)
        g.insert(v, u, w)
    vertex_vector = [Vertex(i + 1) for i in range(node_num)]
    start_vertex = Vertex(1, distance=0)
    array = [0]
    mst = mst_prim(g, start_vertex)
    total_distance = sum(vert.distance for vert in mst if vert.id != 0 and vert.parent_id != 0)
    print(f"Total distance of MST: {total_distance}")
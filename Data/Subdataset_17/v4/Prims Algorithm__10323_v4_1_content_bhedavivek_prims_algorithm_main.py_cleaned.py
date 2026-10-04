import sys
class Vertex:
    def __init__(self, id=0, parent_id=0, distance=float('inf'), position=0):
        self.id = id
        self.parent_id = parent_id
        self.distance = distance
        self.position = position
    def get_distance(self):
        return self.distance
class Graph:
    def __init__(self, n):
        self.adjacency_list = [[] for _ in range(n)]
    def insert(self, u, v, w):
        vert = Vertex(id=v, parent_id=u, distance=w)
        self.adjacency_list[u-1].append(vert)
def insert(vertex):
    array.append(vertex)
    array[0] = len(array) - 1
    heapify_up(array[0])
    vertex_vector[vertex.id - 1].position = array[0]
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
        child_index = 2 * index
        if child_index < array[0] and array[child_index].distance > array[child_index + 1].distance:
            child_index += 1
        if array[child_index].distance < array[index].distance:
            swap_positions(index, child_index)
            index = child_index
        else:
            break
def swap_positions(index1, index2):
    vertex_vector[array[index1].id - 1].position = index2
    vertex_vector[array[index2].id - 1].position = index1
    array[index1], array[index2] = array[index2], array[index1]
def mst_prim(graph, start_vertex):
    insert(start_vertex)
    mst_set = []
    for i in range(len(vertex_vector)):
        if i != start_vertex.id - 1:
            vert = Vertex(id=i + 1)
            insert(vert)
    while len(array) > 1:
        v = extract_min()
        mst_set.append(v)
        for vert in graph.adjacency_list[v.id - 1]:
            if vert.distance < vertex_vector[vert.id - 1].distance:
                vertex_vector[vert.id - 1].distance = vert.distance
                decrease_key(vertex_vector[vert.id - 1].position, vert.distance, v.id)
                vertex_vector[vert.id - 1].parent_id = v.id
    return mst_set
def main(input_path, output_path):
    with open(input_path, "r") as file:
        lines = file.readlines()
    node_num = int(lines[0].split()[0])
    g = Graph(node_num)
    for line in lines[1:]:
        u, v, w = map(int, line.split())
        g.insert(u, v, w)
        g.insert(v, u, w)
    global vertex_vector, array
    vertex_vector = [Vertex(id=i + 1) for i in range(node_num)]
    array = [0]
    start_vertex = Vertex(id=1)
    mst = mst_prim(g, start_vertex)
    total_distance = sum(vert.distance for vert in mst if vert.parent_id != 0)
    mst = sorted((vert for vert in mst if vert.parent_id != 0), key=lambda v: (v.id, v.parent_id))
    with open(output_path, "w") as writer:
        writer.write(str(total_distance))
        for vert in mst:
            writer.write(f"\n{vert.id} {vert.parent_id} {vert.distance}")
if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    main(input_path, output_path)
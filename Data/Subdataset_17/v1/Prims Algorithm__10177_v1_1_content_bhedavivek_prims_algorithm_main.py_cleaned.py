import sys
class Vertex:
    def __init__(self, id, parent_id=0, distance=float('inf')):
        self.id = id
        self.position = 0
        self.parent_id = parent_id
        self.distance = distance
    def get_distance(self):
        return self.distance
class Graph:
    def __init__(self, n):
        self.list = [[] for _ in range(n)]
    def insert(self, u, v, w):
        vert = Vertex(v, u, w)
        self.list[u-1].append(vert)
def insert(vert):
    array.append(vert)
    array[0] = len(array) - 1
    heapify_up(array[0])
    vertex_vector[vert.id-1].position = array[0]
def heapify_up(index):
    while index > 1:
        j = index
        if array[j].distance > array[index].distance:
            vertex_vector[array[index].id-1].position = j
            vertex_vector[array[j].id-1].position = index
            array[index], array[j] = array[j], array[index]
            index = j
        else:
            break
def extract_min():
    vertex_vector[array[1].id-1].position = 0
    last_index = array[0]
    vertex_vector[array[last_index].id-1].position = 1
    ret = array[1]
    array[1] = array[last_index]
    array[0] -= 1
    if array[0] > 1:
        heapify_down(1)
    array.pop()
    return ret
def decrease_key(heap_index, updated_distance, parent_id):
    if heap_index > 0:
        array[heap_index].distance = updated_distance
        array[heap_index].parent_id = parent_id
        heapify_up(heap_index)
def heapify_down(index):
    while 2 * index <= array[0]:
        j = 2 * index
        if j < array[0] and array[j].distance > array[j + 1].distance:
            j += 1
        if array[j].distance < array[index].distance:
            vertex_vector[array[index].id-1].position = j
            vertex_vector[array[j].id-1].position = index
            array[index], array[j] = array[j], array[index]
            index = j
        else:
            break
def mst_prim(graph, start_vertex):
    insert(start_vertex)
    s = []
    for i in range(len(vertex_vector)):
        if i != start_vertex.id - 1:
            vert = Vertex(i + 1)
            insert(vert)
    while len(array) > 1:
        v = extract_min()
        s.append(v)
        for vert in graph.list[v.id-1]:
            if vert.distance < vertex_vector[vert.id-1].distance:
                vertex_vector[vert.id-1].distance = vert.distance
                decrease_key(vertex_vector[vert.id-1].position, vert.distance, v.id)
                vertex_vector[vert.id-1].parent_id = v.id
    return s
input_path = sys.argv[1]
output_path = sys.argv[2]
with open(input_path, "r") as file:
    lines = [line.strip() for line in file]
node_num = int(lines[0].split()[0])
graph = Graph(node_num)
for line in lines[1:]:
    u, v, w = map(int, line.split())
    graph.insert(u, v, w)
    graph.insert(v, u, w)
vertex_vector = [Vertex(i + 1) for i in range(node_num)]
start_vertex = Vertex(1)
mst = mst_prim(graph, start_vertex)
total_distance = sum(vert.distance for vert in mst if vert.id != 0 and vert.parent_id != 0)
mst = sorted(mst, key=lambda v: (v.id, v.parent_id))
with open(output_path, "w") as writer:
    writer.write(f"{total_distance}\n")
    for vert in mst:
        if vert.id != 0 and vert.parent_id != 0:
            writer.write(f"{vert.id} {vert.parent_id} {vert.distance}\n")
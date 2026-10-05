import heapq
import global_data as global_data
def read_graph(file_path, delimiter):
    with open(file_path) as file:
        for line in file:
            v1, v2, weight = [x.strip() for x in line.split(delimiter)]
            if (int(weight), v2, v1) in global_data.EDGES:
                continue
            heapq.heappush(global_data.EDGES, (int(weight), v1, v2))
            global_data.VERTICES.add(v1)
            global_data.VERTICES.add(v2)
    return global_data.EDGES
def make_set(vertex):
    global_data.PARENT[vertex] = vertex
    global_data.RANK[vertex] = 0
def find(vertex):
    if global_data.PARENT[vertex] != vertex:
        global_data.PARENT[vertex] = find(global_data.PARENT[vertex])
    return global_data.PARENT[vertex]
def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    if root1 != root2:
        if global_data.RANK[root1] > global_data.RANK[root2]:
            global_data.PARENT[root2] = root1
        else:
            global_data.PARENT[root1] = root2
            global_data.RANK[root2] += 1
def kruskals():
    total_weight = 0
    for vertex in global_data.VERTICES:
        make_set(vertex)
    while global_data.EDGES:
        weight, vertex1, vertex2 = heapq.heappop(global_data.EDGES)
        if find(vertex1) != find(vertex2):
            union(vertex1, vertex2)
            total_weight += weight
            global_data.MST.append((vertex1, vertex2, str(weight), str(total_weight)))
    return global_data.MST, total_weight
import heapq
import global_data as global_data
def fonk1(file_path, delimiter):
    with open(file_path) as file:
        for line in file:
            v1, v2, b1 = map(str.strip, line.split(delimiter))
            if (int(b1), v2, v1) in global_data.EDGES:
                continue
            heapq.heappush(global_data.EDGES, (int(b1), v1, v2))
            global_data.VERTICES.update((v1, v2))
    return global_data.EDGES
def fonk2(vertex):
    global_data.PARENT[vertex] = vertex
    global_data.RANK[vertex] = 0
def fonk3(vertex):
    if global_data.PARENT[vertex] != vertex:
        global_data.PARENT[vertex] = fonk3(global_data.PARENT[vertex])
    return global_data.PARENT[vertex]
def fonk4(vertex1, b4):
    b2 = fonk3(vertex1)
    b3 = fonk3(b4)
    if b2 != b3:
        if global_data.RANK[b2] > global_data.RANK[b3]:
            global_data.PARENT[b3] = b2
        else:
            global_data.PARENT[b2] = b3
            global_data.RANK[b3] += 1
def fonk5():
    a1 = 0
    for vertex in global_data.VERTICES:
        fonk2(vertex)
    while global_data.EDGES:
        b1, vertex1, b4 = heapq.heappop(global_data.EDGES)
        if fonk3(vertex1) != fonk3(b4):
            fonk4(vertex1, b4)
            a1 += b1
            global_data.MST.append((vertex1, b4, str(b1), str(a1)))
    return global_data.MST, a1
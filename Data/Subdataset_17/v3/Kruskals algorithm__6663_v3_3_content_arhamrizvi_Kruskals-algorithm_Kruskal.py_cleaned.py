def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
def quicksort(array):
    _quicksort(array, 0, len(array) - 1)
def _quicksort(array, start, end):
    if start < end:
        partition_index = _partition(array, start, end)
        _quicksort(array, start, partition_index - 1)
        _quicksort(array, partition_index + 1, end)
def _partition(array, start, end):
    pivot_index = (start + end)
    pivot_value = array[pivot_index][2]
    swap(array, pivot_index, end)
    store_index = start
    for i in range(start, end):
        if array[i][2] < pivot_value:
            swap(array, i, store_index)
            store_index += 1
    swap(array, store_index, end)
    return store_index
def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]
def union(x, y, parent, rank):
    root_x = find(x, parent)
    root_y = find(y, parent)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
def kruskal_mst(input_filename, output_filename):
    edges = _read_edges_from_file(input_filename)
    num_vertices = _find_num_vertices(edges)
    parent, rank = _initialize_union_find(num_vertices)
    quicksort(edges)
    mst = _build_mst(edges, parent, rank)
    _write_mst_to_file(mst, output_filename)
def _read_edges_from_file(filename):
    edges = []
    with open(filename, 'r') as file:
        for line in file:
            u, v, w = map(int, line.split())
            edges.append([u, v, w])
    return edges
def _find_num_vertices(edges):
    return max(max(u, v) for u, v, _ in edges) + 1
def _initialize_union_find(num_vertices):
    parent = list(range(num_vertices))
    rank = [0] * num_vertices
    return parent, rank
def _build_mst(edges, parent, rank):
    mst = []
    for u, v, w in edges:
        if find(u, parent) != find(v, parent):
            mst.append([u, v, w])
            union(u, v, parent, rank)
    return mst
def _write_mst_to_file(mst, filename):
    with open(filename, 'w') as file:
        for u, v, w in mst:
            file.write(f"{u} {v} {w}\n")
input_filename = 'inputgraphfile.txt'
output_filename = 'output_kruskal.txt'
kruskal_mst(input_filename, output_filename)
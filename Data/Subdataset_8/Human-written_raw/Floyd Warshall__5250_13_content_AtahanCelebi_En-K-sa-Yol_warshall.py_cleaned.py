def main(path_v1):
    from map_distance import main
    edges = main(path_v1)[0]
    edges_corrected = list()
    for i in range(len(edges)):
        if edges[i][2] < 900:
            edges_corrected.append(edges[i])
    print("edges coor", edges_corrected)
    num_of_dest = main(path_v1)[1]
    class Graph:
        def __init__(self):
            self.vertices = {}
        def add_vertex(self, key):
            vertex = Vertex(key)
            self.vertices[key] = vertex
        def get_vertex(self, key):
            return self.vertices[key]
        def __contains__(self, key):
            return key in self.vertices
        def add_edge(self, src_key, dest_key, weight=1):
            self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
        def does_edge_exist(self, src_key, dest_key):
            return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
        def __len__(self):
            return len(self.vertices)
        def __iter__(self):
            return iter(self.vertices.values())
    class Vertex:
        def __init__(self, key):
            self.key = key
            self.points_to = {}
        def get_key(self):
            return self.key
        def add_neighbour(self, dest, weight):
            self.points_to[dest] = weight
        def get_neighbours(self):
            return self.points_to.keys()
        def get_weight(self, dest):
            return self.points_to[dest]
        def does_it_point_to(self, dest):
            return dest in self.points_to
    def floyd_warshall(g):
        distance = {v:dict.fromkeys(g, float('inf')) for v in g}
        next_v = {v:dict.fromkeys(g, None) for v in g}
        for v in g:
            for n in v.get_neighbours():
                distance[v][n] = v.get_weight(n)
                next_v[v][n] = n
        for v in g:
             distance[v][v] = 0
             next_v[v][v] = None
        for p in g:
            for v in g:
                for w in g:
                    if distance[v][w] > distance[v][p] + distance[p][w]:
                        distance[v][w] = distance[v][p] + distance[p][w]
                        next_v[v][w] = next_v[v][p]
        return distance, next_v
    def print_path(next_v, u, v):
        p = u
        path_list = list()
        while (next_v[p][v]):
            path_list.append(p.get_key())
            p = next_v[p][v]
        path_list.append(v.get_key())
        return path_list
    g = Graph()
    for i in range(num_of_dest):
        g.add_vertex(i+1)
    for i,j,k in edges_corrected:
        g.add_edge(i, j, k)
    distance, next_v = floyd_warshall(g)
    list_for_sketch = list()
    for start in g:
        for end in g:
            if next_v[start][end]:
                list_for_sketch.append([[start.get_key(),end.get_key()],print_path(next_v, start, end),[distance[start][end]]])
    return list_for_sketch
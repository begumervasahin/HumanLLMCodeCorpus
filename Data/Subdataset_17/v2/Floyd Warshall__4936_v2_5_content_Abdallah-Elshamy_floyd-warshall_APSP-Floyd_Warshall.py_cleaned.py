import math
def floyd_warshall(graph, num_vertices):
    distance = [[math.inf] * (num_vertices + 1) for _ in range(num_vertices + 1)]
    for i in range(1, num_vertices + 1):
        for j in range(1, num_vertices + 1):
            if i == j:
                distance[i][j] = 0
            elif (i, j) in graph:
                distance[i][j] = graph[(i, j)]
    for k in range(1, num_vertices + 1):
        for i in range(1, num_vertices + 1):
            for j in range(1, num_vertices + 1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    for i in range(1, num_vertices + 1):
        if distance[i][i] < 0:
            return 'NULL'
    shortest_path = min(min(row[1:]) for row in distance[1:])
    return shortest_path
def read_graph_from_file(file_path):
    graph = {}
    with open(file_path) as file:
        first_line = file.readline()
        num_vertices, num_edges = map(int, first_line.split())
        for line in file:
            u, v, w = map(int, line.split())
            if (u, v) not in graph or graph[(u, v)] > w:
                graph[(u, v)] = w
    return graph, num_vertices
def main():
    file_path = 'g3.txt'
    graph, num_vertices = read_graph_from_file(file_path)
    result = floyd_warshall(graph, num_vertices)
    print(result)
if __name__ == '__main__':
    main()
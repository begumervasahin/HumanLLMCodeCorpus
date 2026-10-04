import itertools
def floyd_warshall(graph, vertex_count):
    for k in range(vertex_count):
        for i, j in itertools.product(range(vertex_count), range(vertex_count)):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
def initialize_graph(vertex_count):
    INF = 1000
    graph = [[INF for _ in range(vertex_count)] for _ in range(vertex_count)]
    for i in range(vertex_count):
        graph[i][i] = 0
    edges = [
        (0, 2, -2),
        (1, 0, 4),
        (1, 2, 3),
        (2, 3, 2),
        (3, 1, -1)
    ]
    for u, v, w in edges:
        graph[u][v] = w
    return graph
def print_graph(graph):
    for row in graph:
        print(' '.join(f"{value:4}" for value in row))
def main():
    vertex_count = 4
    graph = initialize_graph(vertex_count)
    print("Initial graph:")
    print_graph(graph)
    floyd_warshall(graph, vertex_count)
    print("\nGraph after applying Floyd-Warshall algorithm:")
    print_graph(graph)
if __name__ == '__main__':
    main()
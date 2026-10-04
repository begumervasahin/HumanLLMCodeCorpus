import itertools
def floyd_warshall(graph, vertex_num):
    for k in range(vertex_num):
        for i, j in itertools.product(range(vertex_num), range(vertex_num)):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
def initialize_graph(vertex_num):
    INF = 1000
    graph = [[INF for _ in range(vertex_num)] for _ in range(vertex_num)]
    for i in range(vertex_num):
        graph[i][i] = 0
    graph[0][2] = -2
    graph[1][0] = 4
    graph[1][2] = 3
    graph[2][3] = 2
    graph[3][1] = -1
    return graph
def print_graph(graph):
    for row in graph:
        print(row)
def main():
    vertex_num = 4
    graph = initialize_graph(vertex_num)
    print("Initial graph:")
    print_graph(graph)
    print("\nAfter Floyd-Warshall algorithm:")
    floyd_warshall(graph, vertex_num)
    print_graph(graph)
if __name__ == '__main__':
    main()
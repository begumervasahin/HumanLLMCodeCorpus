import math
def floyd_warshall(graph, num_vertices):
    book_keeper = [[[0 if k == 0 else 0 for k in range(2)] for j in range(num_vertices + 1)] for i in range(num_vertices + 1)]
    for i in range(1, num_vertices + 1):
        for j in range(1, num_vertices + 1):
            if i == j:
                book_keeper[i][j][0] = 0
            elif graph.get((i, j)) is not None:
                book_keeper[i][j][0] = graph[(i, j)]
            else:
                book_keeper[i][j][0] = math.inf
    shortest_path = math.inf
    for k in range(1, num_vertices + 1):
        for i in range(1, num_vertices + 1):
            for j in range(1, num_vertices + 1):
                book_keeper[i][j][1] = min(book_keeper[i][j][0], book_keeper[i][k][0] + book_keeper[k][j][0])
                if k == num_vertices and shortest_path > book_keeper[i][j][1]:
                    shortest_path = book_keeper[i][j][1]
                if i == j and book_keeper[i][j][1] < 0:
                    return 'NULL'
                book_keeper[i][j][0] = book_keeper[i][j][1]
    return shortest_path
def read_graph_from_file(file_path):
    graph = {}
    with open(file_path) as file:
        first_line = file.readline()
        num_vertices, num_edges = map(int, first_line.split())
        data = file.readlines()
        for line in data:
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
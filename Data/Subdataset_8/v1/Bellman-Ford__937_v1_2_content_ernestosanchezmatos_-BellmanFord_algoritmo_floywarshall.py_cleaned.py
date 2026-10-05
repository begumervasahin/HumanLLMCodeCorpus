INF = 99999
def read_graph_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        num_vertices = int(lines[0])
        graph = [[int(elem.strip()) if elem.strip() != 'INF' else INF
                  for elem in line.strip().split(',')]
                 for line in lines[1:]]
    return num_vertices, graph
def floyd_warshall(graph, num_vertices):
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    for i in range(num_vertices):
        if graph[i][i] < 0:
            print("Negative cycle detected on vertex:", i)
def write_graph_to_file(graph, filename):
    with open(filename, "w") as file:
        for row in graph:
            file.write(','.join(map(str, row)) + '\n')
def main():
    option = input("Choose the file (1 - Graph without Negative Cycles or 2 - Graph with Negative Cycles): ")
    if option == '1':
        input_filename = "input.txt"
    elif option == '2':
        input_filename = "inputNegativeCycle.txt"
    else:
        print("Invalid option. Please choose either 1 or 2.")
        return
    num_vertices, graph = read_graph_from_file(input_filename)
    print("Vertices:", num_vertices)
    print("Graph:")
    for row in graph:
        print(row)
    floyd_warshall(graph, num_vertices)
    print("Resulting Graph:")
    for row in graph:
        print(row)
    output_filename = "output.txt"
    write_graph_to_file(graph, output_filename)
    print("Resulting graph written to", output_filename)
if __name__ == "__main__":
    main()
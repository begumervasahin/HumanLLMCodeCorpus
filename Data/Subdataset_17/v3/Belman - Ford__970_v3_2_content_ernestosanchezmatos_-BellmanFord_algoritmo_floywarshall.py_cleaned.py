import numpy as np
INF = 99999
def read_graph_from_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    V = int(lines[0].strip())
    graph = []
    for line in lines[1:]:
        row = [int(elem.strip()) if elem.strip() != 'INF' else INF for elem in line.split(',')]
        graph.append(row)
    return V, graph
def floyd_warshall(graph, V):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    for i in range(V):
        if graph[i][i] < 0:
            print(f"Exists Negative Cycle on Vertice(s): {i}")
    return graph
def write_graph_to_file(graph, filename):
    with open(filename, "w") as f:
        for row in graph:
            f.write(', '.join(map(str, row)) + "\n")
def main():
    op = input("Choose the file (1 - Graph without Negative Cycles or 2 - Graph with Negative Cycles): ")
    if int(op) == 1:
        input_filename = "input.txt"
    elif int(op) == 2:
        input_filename = "inputNegativeCycle.txt"
    else:
        print("Invalid option.")
        return
    V, graph = read_graph_from_file(input_filename)
    print(f"Vertices: {V}")
    print("Initial Graph:")
    for row in graph:
        print(row)
    updated_graph = floyd_warshall(graph, V)
    print("Graph after Floyd-Warshall:")
    for row in updated_graph:
        print(row)
    write_graph_to_file(updated_graph, "output.txt")
if __name__ == "__main__":
    main()
import random
def generate_random_graph(num_vertices):
    adjacency_matrix = [[random.randint(1, 10) for _ in range(num_vertices)] for _ in range(num_vertices)]
    return adjacency_matrix
def write_graph_to_file(adjacency_matrix, num_vertices):
    file_path = "randograph-{}.txt".format(num_vertices)
    with open(file_path, "w") as file:
        file.write("{}\n".format(num_vertices))
        for vertex in range(num_vertices):
            edges = [random.randint(0, num_vertices - 1) for _ in range(10)]
            for edge in edges:
                file.write("{} {} {}\n".format(vertex + 1, edge + 1, adjacency_matrix[vertex][edge]))
def main():
    num_vertices_list = [5, 10, 20, 50, 100, 200, 500, 750, 1000, 1250, 1500, 2000, 3000, 5000]
    for num_vertices in num_vertices_list:
        adjacency_matrix = generate_random_graph(num_vertices)
        write_graph_to_file(adjacency_matrix, num_vertices)
if __name__ == "__main__":
    main()
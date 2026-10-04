import random
def generate_random_graph(num_vertices):
    return [[random.randint(1, 10) for _ in range(num_vertices)] for _ in range(num_vertices)]
def write_graph_to_file(filename, num_vertices, matrix):
    with open(filename, "w") as file:
        file.write(f"{num_vertices}\n")
        for i in range(num_vertices):
            random_edges = random.sample(range(num_vertices), 10)
            for j in random_edges:
                file.write(f"{i + 1} {j + 1} {matrix[i][j]}\n")
def main():
    vertex_counts = [5, 10, 20, 50, 100, 200, 500, 750, 1000, 1250, 1500, 2000, 3000, 5000]
    for num_vertices in vertex_counts:
        matrix = generate_random_graph(num_vertices)
        filename = f"randograph-{num_vertices}.txt"
        write_graph_to_file(filename, num_vertices, matrix)
if __name__ == '__main__':
    main()
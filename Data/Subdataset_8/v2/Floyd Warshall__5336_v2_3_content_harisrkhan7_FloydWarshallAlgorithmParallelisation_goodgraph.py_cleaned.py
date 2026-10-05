import random
num_vertices_list = [5, 10, 20, 50, 100, 200, 500, 750, 1000, 1250, 1500, 2000, 3000, 5000]
for num_vertices in num_vertices_list:
    adjacency_matrix = [[random.randint(1, 10) for _ in range(num_vertices)] for _ in range(num_vertices)]
    with open("randograph-{}.txt".format(num_vertices), "w") as file:
        file.write("{}\n".format(num_vertices))
        for vertex in range(num_vertices):
            edges = [random.randint(0, num_vertices - 1) for _ in range(10)]
            for edge in edges:
                file.write("{} {} {}\n".format(vertex + 1, edge + 1, adjacency_matrix[vertex][edge]))
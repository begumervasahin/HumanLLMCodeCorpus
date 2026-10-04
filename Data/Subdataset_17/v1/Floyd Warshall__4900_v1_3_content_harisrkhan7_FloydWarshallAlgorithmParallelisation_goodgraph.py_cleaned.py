import random
vertex_counts = [5, 10, 20, 50, 100, 200, 500, 750, 1000, 1250, 1500, 2000, 3000, 5000]
for num_vertices in vertex_counts:
    matrix = [[random.randint(1, 10) for _ in range(num_vertices)] for _ in range(num_vertices)]
    with open(f"randograph-{num_vertices}.txt", "w") as f:
        f.write(f"{num_vertices}\n")
        for i in range(num_vertices):
            random_edges = random.sample(range(num_vertices), 10)
            for j in random_edges:
                f.write(f"{i + 1} {j + 1} {matrix[i][j]}\n")
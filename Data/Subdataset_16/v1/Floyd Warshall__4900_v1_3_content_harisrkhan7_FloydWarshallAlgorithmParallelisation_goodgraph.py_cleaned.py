import random
b1 = [5, 10, 20, 50, 100, 200, 500, 750, 1000, 1250, 1500, 2000, 3000, 5000]
for num_vertices in b1:
    b2 = [[random.randint(1, 10) for _ in range(num_vertices)] for _ in range(num_vertices)]
    with open(f"randograph-{num_vertices}.txt", "w") as f:
        f.write(f"{num_vertices}\n")
        for i in range(num_vertices):
            b3 = random.sample(range(num_vertices), 10)
            for j in b3:
                f.write(f"{i + 1} {j + 1} {b2[i][j]}\n")
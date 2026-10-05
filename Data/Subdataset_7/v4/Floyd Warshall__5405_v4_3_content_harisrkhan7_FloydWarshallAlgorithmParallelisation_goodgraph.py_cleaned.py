import random
b1 = [5, 10, 20, 50, 100, 200, 500, 750, 1000, 1250, 1500, 2000, 3000, 5000]
for num_vertices in b1:
    b2 = [[random.randint(1, 10) for _ in range(num_vertices)] for _ in range(num_vertices)]
    with open("randograph-{}.txt".format(num_vertices), "w") as file:
        file.write("{}\n".format(num_vertices))
        for i in range(num_vertices):
            b3 = [random.randint(0, num_vertices - 1) for _ in range(10)]
            for j in b3:
                file.write("{} {} {}\n".format(i + 1, j + 1, b2[i][j]))
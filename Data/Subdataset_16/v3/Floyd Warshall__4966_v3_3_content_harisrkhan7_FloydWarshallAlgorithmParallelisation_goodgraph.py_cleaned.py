import random
def fonk1(num_vertices):
    return [[random.randint(1, 10) for _ in range(num_vertices)] for _ in range(num_vertices)]
def fonk2(b4, num_vertices, b3):
    with open(b4, "w") as file:
        file.write(f"{num_vertices}\n")
        for i in range(num_vertices):
            b1 = random.sample(range(num_vertices), 10)
            for j in b1:
                file.write(f"{i + 1} {j + 1} {b3[i][j]}\n")
def fonk3():
    b2 = [5, 10, 20, 50, 100, 200, 500, 750, 1000, 1250, 1500, 2000, 3000, 5000]
    for num_vertices in b2:
        b3 = fonk1(num_vertices)
        b4 = f"randograph-{num_vertices}.txt"
        fonk2(b4, num_vertices, b3)
if b5 = = '__main__':
    fonk3()
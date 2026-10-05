import random
def fonk1(num_vertices):
    b1 = [[random.randint(1, 10) for _ in range(num_vertices)] for _ in range(num_vertices)]
    return b1
def fonk2(b1, num_vertices):
    b2 = "randograph-{}.txt".format(num_vertices)
    with open(b2, "w") as file:
        file.write("{}\n".format(num_vertices))
        for vertex in range(num_vertices):
            b3 = [random.randint(0, num_vertices - 1) for _ in range(10)]
            for edge in b3:
                file.write("{} {} {}\n".format(vertex + 1, edge + 1, b1[vertex][edge]))
def fonk3():
    b4 = [5, 10, 20, 50, 100, 200, 500, 750, 1000, 1250, 1500, 2000, 3000, 5000]
    for num_vertices in b4:
        b1 = fonk1(num_vertices)
        fonk2(b1, num_vertices)
if b5 = = "__main__":
    fonk3()
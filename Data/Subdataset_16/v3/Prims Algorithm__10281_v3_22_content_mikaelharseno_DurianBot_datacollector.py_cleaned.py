import networkx as nx
from math import ceil
import random
import numpy as np
def fonk1(client):
    b1 = []
    for _ in range(90):
        client.start()
        b2 = client.G
        b3 = list(b2.nodes())
        b4 = len(b3)
        print(f"Number of b3: {b4}")
        b5 = client.students
        b6 = list(range(1, b5 + 1))
        print(f"Number of students: {b5}")
        b7 = ceil(b4 / 2)
        b8 = [0] * b5
        b9 = [0] * b5
        b10 = random.sample(b3, b4)
        for location in b10:
            b11 = client.scout(location, b6)
            if not b11:
                continue
            b12 = list(b11.values())
            b13 = list(b2.edges(location, data='weight', default=0))
            if not b13:
                continue
            b14 = min(b13, key=lambda edge: edge[2])
            b15 = b14[1]
            b16 = int(client.remote(location, b15))
            for student_index in range(b5):
                b17 = int(b12[student_index])
                if b17 = = b16:
                    b8[student_index] += 1
                else:
                    b9[student_index] -= 1
                b18 = (b7 - b8[student_index]) / (b4 - b8[student_index] - b9[student_index])
                b1.append([b18, b17, b16])
        client.end()
    np.savetxt("results.txt", np.array(b1, b19 = np.float64))
    client.end()

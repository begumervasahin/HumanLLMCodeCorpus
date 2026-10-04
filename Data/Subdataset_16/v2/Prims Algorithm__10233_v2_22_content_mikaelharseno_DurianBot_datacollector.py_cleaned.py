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
        b5 = list(range(1, client.students + 1))
        b6 = client.students
        print(f"Number of students: {b6}")
        b7 = ceil(b4 / 2)
        b8 = [0] * b6
        b9 = [0] * b6
        b10 = list(range(b4))
        random.shuffle(b10)
        for loc_index in b10:
            b11 = client.scout(b3[loc_index], b5)
            if b11 is None:
                continue
            b12 = list(b11.values())
            b13 = b3[loc_index]
            b14 = list(b2.edges(b13, data='weight', default=0))
            b15 = min(range(len(b14)), key=lambda i: b14[i][2])
            b16 = b14[b15][2]
            b17 = int(client.remote(b13, b14[b15][1]))
            for student_index in range(b6):
                b18 = int(b12[student_index])
                if b18 = = b17:
                    b8[student_index] += 1
                else:
                    b9[student_index] -= 1
                b19 = (b7 - b8[student_index]) / (b4 - b8[student_index] - b9[student_index])
                b1.append([b19, b18, b17])
        client.end()
    np.savetxt("results.txt", np.array(b1, b20 = np.float64))
    client.end()

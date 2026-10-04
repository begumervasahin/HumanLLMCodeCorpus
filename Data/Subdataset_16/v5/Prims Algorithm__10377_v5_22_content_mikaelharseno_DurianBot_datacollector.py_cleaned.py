import networkx as nx
from math import ceil
import random
import numpy as np
def fonk1(client):
    client.end()
    b1 = []
    for _ in range(90):
        client.start()
        b2 = client.G
        b3 = list(b2.nodes())
        b4 = len(b3)
        b5 = client.students
        print(f"Number of b3: {b4}")
        print(f"Number of students: {b5}")
        b6 = ceil(b4 / 2)
        b7 = [0] * b5
        b8 = [0] * b5
        b9 = list(range(b4))
        random.shuffle(b9)
        for random_loc in b9:
            b10 = client.scout(b3[random_loc], list(range(1, b5 + 1)))
            if b10 is None:
                continue
            b11 = list(b10.values())
            b12 = b3[random_loc]
            b13 = list(b2.edges(b12, 'weight', default=0))
            if not b13:
                continue
            b14 = min(range(len(b13)), key=lambda i: b13[i][2])
            b15 = int(client.remote(b12, b13[b14][1]))
            for i in range(b5):
                b16 = int(b11[i])
                if b16 = = b15:
                    b7[i] += 1
                else:
                    b8[i] -= 1
                b17 = (b6 - b7[i]) / (b4 - b7[i] - b8[i])
                b1.append([b17, b16, b15])
        client.end()
    np.savetxt("results.txt", np.array(b1, np.float64))
    client.end()
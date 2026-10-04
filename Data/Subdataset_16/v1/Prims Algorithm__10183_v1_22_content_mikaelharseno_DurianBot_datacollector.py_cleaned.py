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
        print("b4 is", str(b4))
        b5 = list(range(1, client.students + 1))
        b6 = client.students
        print("num students is", str(b6))
        b7 = ceil(b4 / 2)
        b8 = [0 for _ in range(b6)]
        b9 = [0 for _ in range(b6)]
        b10 = list(range(b4))
        random.shuffle(b10)
        for randomloc in b10:
            b11 = client.scout(b3[randomloc], b5)
            if b11 is None:
                continue
            b12 = list(b11.values())
            b13 = b3[randomloc]
            b14 = list(b2.edges(b13, data='weight', default=0))
            a1 = 0
            b15 = float('inf')
            for i in range(len(b14)):
                if b14[i][2] < b15:
                    b15 = b14[i][2]
                    a1 = i
            b16 = int(client.remote(b13, b14[a1][1]))
            for i in range(b6):
                b17 = int(b12[i])
                if b17 = = b16:
                    b8[i] += 1
                else:
                    b9[i] -= 1
                b18 = (b7 - b8[i]) / (b4 - b8[i] - b9[i])
                b1.append([b18, b17, b16])
        client.end()
    np.savetxt("results.txt", np.array(b1, np.float64))
    client.end()

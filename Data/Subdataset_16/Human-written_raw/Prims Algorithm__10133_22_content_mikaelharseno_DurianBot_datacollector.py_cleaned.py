import networkx as nx
from math import ceil
import random
from heapq import heappop, heappush
from itertools import count
import random
import numpy as np
def fonk1(client):
    client.end()
    b1 = []
    for b15 in range(90):
        client.start()
        b2 = client.G
        b3 = list(b2.nodes())
        b4 = len(list(b2.nodes()))
        print("b4 is ", str(b4))
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
            b14 = list(b2.edges(b13, 'weight', default=0))
            a1 = 0
            a2 = -1
            for b15 in range(len(b14)):
                if b15 = = 0:
                    a2 = b14[b15][2]
                    a1 = b15
                if b14[b15][2] < a2:
                    a2 = b14[b15][2]
                    a1 = b15
            b16 = int(client.remote(b13, b14[a1][1]))
            for b15 in range(b6):
                b17 = int(b12[b15])
                if b17 = = b16:
                    b8[b15] += 1
                else:
                    b9[b15] -=1
                b18 = (b7 - b8[b15]) / (b4 - b8[b15] - b9[b15])
                b1.append([b18, b17, b16])
        client.end()
    np.savetxt("results.txt", np.array(b1, np.float64))
    client.end()
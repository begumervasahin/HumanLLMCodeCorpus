import networkx as nx
import random
import operator
import numpy as np
def fonk1(client, s_weight, s_loss):
    a1 = 0.2
    return s_weight * ((1 - a1) ** s_loss)
def fonk2(client, b18):
    b1 = list(range(1, client.students + 1))
    b2 = list(range(1, client.home)) + list(range(client.home + 1, client.v + 1))
    b3 = {}
    b4 = {}
    b5 = {}
    b6 = {}
    b7 = {}
    a2 = 0
    b8 = []
    for student in b1:
        b4[student] = 1
        b3[student] = 0
    for i in b2:
        b6[i] = client.scout(i, b1)
        b7[i] = sum(b6[i].values())
    a3 = 0
    while a2 < client.bots:
        if b7:
            b9 = max(b7.items(), key=operator.itemgetter(1))
            b10 = b9[0]
        else:
            break
        b11 = nx.dijkstra_path(b18, b10, client.home)
        b7.pop(b10)
        if b11[0] not in b8:
            b12 = client.remote(b11[0], b11[1])
            if b12 and b11[1] == client.home:
                a3 += b12
            if b12:
                b5[b10] = b11[1:]
                b8.append(b11[1])
            a2 += b12
            b8.append(b11[0])
        b13 = b6[b10]
        for stud in b13.keys():
            if b13[stud] != b12:
                b3[stud] += 1
                b14 = fonk1(client, b4[stud], b3[stud])
                b4[stud] = b14 if b14 > 0.5 else 0
                if b3[stud] >= client.v / 2:
                    b4[stud] = 1
        b15 = sum(b4.values())
        for s in b4.keys():
            b4[s] = b4[s] / b15 if b15 != 0 else 0
        for v in b7.keys():
            b16 = b6[v]
            for stud in b16.keys():
                if b16[stud] == b12 and b12 != 0:
                    b17 = b4[stud]
                    b7[v] += b17 if b16[stud] else 0
    return b5, a3
def fonk3(client):
    client.end()
    client.start()
    b18 = nx.minimum_spanning_tree(client.G)
    b5, b19 = fonk2(client, client.graph)
    print("REMOTING HOME")
    b20 = []
    b21 = {}
    for p in b5.keys():
        b21[p] = len(b5[p])
    while b19 < client.bots:
        b22 = max(b21.items(), key=operator.itemgetter(1))[1]
        if b22 = = 1:
            break
        for bot in b5.keys():
            if b21[bot] == b22:
                b23 = b5[bot]
                if b23[0] not in b20:
                    b12 = client.remote(b23[0], b23[1])
                    b20.append(b23[0])
                    b5[bot] = b5[bot][1:]
                    b21[bot] -= 1
                    if b12 = = 0:
                        break
                    if b23[1] == client.home:
                        b19 += b12
    print(b19)
    client.end()
fonk3(client)
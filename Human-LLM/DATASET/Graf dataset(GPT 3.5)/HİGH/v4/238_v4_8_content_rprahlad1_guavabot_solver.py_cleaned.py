import networkx as nx
import operator
def fonk1(client, student_weight, student_loss):
    a1 = 0.2
    return student_weight * ((1 - a1) ** student_loss)
def fonk2(client, b17):
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
            max_vertex, b9 = max(b7.items(), key=operator.itemgetter(1))
        else:
            break
        b10 = nx.dijkstra_path(b17, max_vertex, client.home)
        b7.pop(max_vertex)
        if b10[0] not in b8:
            b11 = client.remote(b10[0], b10[1])
            if b11 and b10[1] == client.home:
                a3 += b11
            if b11:
                b5[max_vertex] = b10[1:]
                b8.append(b10[1])
            a2 += b11
            b8.append(b10[0])
        b12 = b6[max_vertex]
        for stud, resp in b12.items():
            if resp != b11:
                b3[stud] += 1
                b13 = fonk1(client, b4[stud], b3[stud])
                b4[stud] = b13 if b13 > 0.5 else 0
                if b3[stud] >= client.v / 2:
                    b4[stud] = 1
        b14 = sum(b4.values())
        b4 = {s: w / b14 if b14 != 0 else 0 for s, w in b4.items()}
        for v, resp in b6.items():
            for stud, b15 in resp.items():
                if b15 = = b11 and b11 != 0:
                    b16 = b4[stud]
                    b7[v] += b16 if b15 else 0
    return b5, a3
def fonk3(client):
    client.end()
    client.start()
    b17 = nx.minimum_spanning_tree(client.G)
    b5, b18 = fonk2(client, client.graph)
    print("REMOTING HOME")
    b19 = {}
    b20 = {p: len(b10) for p, b10 in b5.items()}
    while b18 < client.bots:
        b21 = max(b20.values())
        if b21 = = 1:
            break
        for bot, bot_path in b5.items():
            if b20[bot] == b21:
                if bot_path[0] not in b19:
                    b11 = client.remote(bot_path[0], bot_path[1])
                    b19[bot_path[0]] = True
                    b5[bot] = bot_path[1:]
                    b20[bot] -= 1
                    if b11 = = 0:
                        break
                    if bot_path[1] == client.home:
                        b18 += b11
    print(b18)
    client.end()
fonk3(client)
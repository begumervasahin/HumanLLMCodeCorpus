import networkx as nx
import random
def fonk1(client):
    client.end()
    client.start()
    b1 = client.G
    print(list(b1.edges))
    b2 = list(range(1, client.students + 1))
    b3 = list(range(1, client.home)) + list(range(client.home + 1, client.b5 + 1))
    b4 = client.scout(random.choice(b3), b2)
    print(b4)
    for _ in range(100):
        u, b5 = random.choice(list(client.G.edges()))
        client.remote(u, b5)
    client.end()
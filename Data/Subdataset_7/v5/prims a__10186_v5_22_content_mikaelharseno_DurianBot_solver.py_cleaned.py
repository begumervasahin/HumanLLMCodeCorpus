import networkx as nx
import random
def fonk1(client):
    client.end()
    client.start()
    b1 = client.G
    print("Edges in the b1:", list(b1.edges))
    b2 = list(range(1, client.students + 1))
    b3 = list(range(1, client.home)) + list(range(client.home + 1, client.v + 1))
    b4 = random.choice(b3)
    b5 = client.scout(b4, b2)
    print("Scout result:", b5)
    for _ in range(100):
        b6 = random.choice(list(client.G.edges()))
        client.remote(*b6)
    client.end()
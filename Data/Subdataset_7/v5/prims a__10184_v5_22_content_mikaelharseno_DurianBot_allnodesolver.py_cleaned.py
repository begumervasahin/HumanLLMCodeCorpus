import networkx as nx
def fonk1(client):
    client.end()
    client.start()
    b1 = client.G
    b2 = nx.minimum_spanning_tree(b1)
    fonk2(b2, client)
    print("Number of bots needed to be rescued:")
    print(client.l)
    print("Number of final rescued bots:")
    print(client.bot_count[client.home])
    client.end()
def fonk2(b2, client):
    b3 = list(b2.degree)
    while len(b3) > 1:
        b4 = next((node for node, degree in b3 if degree == 1 and node != client.h), None)
        if b4 is None:
            break
        b5 = next(iter(b2[b4]))
        client.remote(b4, b5)
        b2.remove_node(b4)
        b3 = list(b2.degree)

import networkx as nx
def solve(client):
    client.end()
    client.start()
    graph = client.G
    mst = nx.minimum_spanning_tree(graph)
    remote_spanning_tree(mst, client)
    print("Number of bots needed to be rescued:")
    print(client.l)
    print("Number of final rescued bots:")
    print(client.bot_count[client.home])
    client.end()
def remote_spanning_tree(mst, client):
    degrees = list(mst.degree)
    while len(degrees) > 1:
        u = next((node for node, degree in degrees if degree == 1 and node != client.h), None)
        if u is None:
            break
        v = next(iter(mst[u]))
        client.remote(u, v)
        mst.remove_node(u)
        degrees = list(mst.degree)

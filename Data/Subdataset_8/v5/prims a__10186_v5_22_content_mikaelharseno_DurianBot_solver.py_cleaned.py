import networkx as nx
import random
def solve(client):
    client.end()
    client.start()
    graph = client.G
    print("Edges in the graph:", list(graph.edges))
    all_students = list(range(1, client.students + 1))
    non_home_nodes = list(range(1, client.home)) + list(range(client.home + 1, client.v + 1))
    random_non_home_node = random.choice(non_home_nodes)
    scout_result = client.scout(random_non_home_node, all_students)
    print("Scout result:", scout_result)
    for _ in range(100):
        random_edge = random.choice(list(client.G.edges()))
        client.remote(*random_edge)
    client.end()
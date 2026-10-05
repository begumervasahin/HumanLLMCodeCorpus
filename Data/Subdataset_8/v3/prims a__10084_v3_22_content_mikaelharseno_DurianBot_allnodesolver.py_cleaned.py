import networkx as nx
import random
class Client:
    def __init__(self, graph):
        self.graph = graph
        self.home = random.choice(list(graph.nodes()))
        self.rescue_needed = 0
        self.rescue_count = {node: 0 for node in graph.nodes()}
    def start(self):
        pass
    def end(self):
        pass
    def move_bot(self, from_node, to_node):
        print(f"Bot moved from {from_node} to {to_node}")
        self.rescue_count[to_node] += 1
        if to_node == self.home:
            self.rescue_needed += 1
def solve(client):
    client.end()
    client.start()
    mst = nx.minimum_spanning_tree(client.graph)
    remote_control(client, mst)
    print("Number of bots needing rescue:")
    print(client.rescue_needed)
    print("Number of final rescued bots:")
    print(client.rescue_count[client.home])
    client.end()
def remote_control(client, mst):
    degrees = list(mst.degree)
    while len(degrees) > 1:
        node_index = 0
        len_nodes = len(degrees)
        while node_index < len_nodes:
            if degrees[node_index][1] == 1 and degrees[node_index][0] != client.home:
                break
            node_index += 1
        u = degrees[node_index][0]
        v = list(mst[u].keys())[0]
        client.move_bot(u, v)
        mst.remove_node(u)
        degrees = list(mst.degree)
    return 1
graph = nx.complete_graph(5)
client = Client(graph)
solve(client)
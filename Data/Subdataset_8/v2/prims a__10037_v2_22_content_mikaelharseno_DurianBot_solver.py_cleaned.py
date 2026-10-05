import networkx as nx
import random
class Client:
    def __init__(self):
        self.G = nx.Graph()
        self.students = 10
        self.home = 1
        self.v = 20
    def end(self):
        print("Ending client...")
    def start(self):
        print("Starting client...")
    def scout(self, node, students):
        print(f"Scouting node {node} for students: {students}")
        return random.choice(students)
    def remote(self, u, v):
        print(f"Remoting from {u} to {v}")
def solve(client):
    client.end()
    client.start()
    graph = client.G
    print(list(graph.edges))
    all_students = list(range(1, client.students + 1))
    non_home = list(range(1, client.home)) + list(range(client.home + 1, client.v + 1))
    selected_student = client.scout(random.choice(non_home), all_students)
    print(selected_student)
    for _ in range(100):
        u, v = random.choice(list(client.G.edges()))
        client.remote(u, v)
    client.end()
if __name__ == "__main__":
    client = Client()
    solve(client)
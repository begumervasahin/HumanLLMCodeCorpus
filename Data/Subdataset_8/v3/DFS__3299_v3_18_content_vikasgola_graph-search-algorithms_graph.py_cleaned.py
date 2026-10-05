from random import choice
import pygame
class Node:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.g = 0
        self.h = 0
        self.f = 0
        self.previous = None
    def calculate_h(self, destination):
        self.h = (self.x - destination.x) ** 2 + (self.y - destination.y) ** 2
        return self.h
    def calculate_g(self, destination=None):
        if self.previous is None:
            return 0
        self.g = self.previous.g + (self.x - self.previous.x) ** 2 + (self.y - self.previous.y) ** 2
        return self.g
    def calculate_f(self, destination):
        self.f = self.calculate_g(destination) + self.calculate_h(destination)
        return self.f
class Graph:
    def __init__(self):
        self.nodes = {}
        self.adjacency_list = {}
        self.vertex_count = 0
        self.edge_count = 0
    def show_graph(self, edges):
        pygame.init()
        screen = pygame.display.set_mode((600, 600))
        done = False
        clock = pygame.time.Clock()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            screen.fill((200, 200, 200))
            for node in self.nodes.values():
                pygame.draw.circle(screen, (0, 100, 255), (int(node.x), int(node.y)), 10)
            for edge in edges:
                pygame.draw.line(screen, (200, 100, 0), (int(edge[0].x), int(edge[0].y)),
                                 (int(edge[1].x), int(edge[1].y)), 4)
            pygame.display.flip()
            clock.tick(60)
    def add_node(self, node):
        self.nodes[node.name] = node
        self.vertex_count += 1
    def initialize_adjacency_list(self):
        self.adjacency_list = {name: [] for name in self.nodes.keys()}
    def calculate_h_for_all_nodes(self, destination):
        for node in self.nodes.values():
            node.calculate_h(destination)
    def add_random_edges(self, n):
        temp_nodes = list(self.nodes.values())
        connected_nodes = [temp_nodes[0]]
        edges = []
        for _ in range(n):
            random_node_index = choice(range(len(temp_nodes)))
            random_connected_node_index = choice(range(len(connected_nodes)))
            if random_node_index != random_connected_node_index:
                edge = [temp_nodes[random_node_index], connected_nodes[random_connected_node_index]]
                edges.append(edge)
                self.add_edge(edge[0], edge[1])
                connected_nodes.append(temp_nodes[random_node_index])
        return edges
    def add_all_edges(self):
        temp_nodes = list(self.nodes.values())
        for i in range(self.vertex_count):
            for j in range(i + 1, self.vertex_count):
                self.adjacency_list[temp_nodes[j].name].append(temp_nodes[i])
                self.adjacency_list[temp_nodes[i].name].append(temp_nodes[j])
                self.edge_count += 1
    def add_edge(self, node1, node2):
        if node1 not in self.adjacency_list[node2.name] and node2 not in self.adjacency_list[node1.name]:
            self.adjacency_list[node1.name].append(node2)
            self.adjacency_list[node2.name].append(node1)
            self.edge_count += 1
    def clear_cache(self):
        for node in self.nodes.values():
            node.previous = None
            node.g = 0
            node.h = 0
            node.f = 0
def main():
    graph = Graph()
    nodes = [Node(100, 100, 'A'), Node(200, 200, 'B'), Node(300, 300, 'C'), Node(400, 400, 'D')]
    for node in nodes:
        graph.add_node(node)
    graph.initialize_adjacency_list()
    graph.add_all_edges()
    graph.show_graph([[nodes[0], nodes[1]], [nodes[1], nodes[2]], [nodes[2], nodes[3]], [nodes[3], nodes[0]]])
if __name__ == "__main__":
    main()
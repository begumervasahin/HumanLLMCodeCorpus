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
        self.v = 0
        self.e = 0
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
            for n in self.nodes.values():
                pygame.draw.circle(screen, (0, 100, 255), (int(n.x), int(n.y)), 10)
            for e in edges:
                pygame.draw.line(screen, (200, 100, 0), (int(e[0].x), int(e[0].y)), (int(e[1].x), int(e[1].y)), 4)
            pygame.display.flip()
            clock.tick(60)
    def add_node(self, node):
        self.nodes[node.name] = node
        self.v += 1
    def init_adj_list(self):
        self.adjacency_list = {}
        for name in self.nodes.keys():
            self.adjacency_list[name] = []
    def calculate_h(self, destination):
        for node in self.nodes.values():
            node.calculate_h(destination)
    def add_random_edges(self, n, graph_v):
        temp1 = list(self.nodes.values())
        temp2 = [temp1[0]]
        tedges = []
        for i in range(n):
            if len(temp1) <= i:
                s1 = choice(range(len(temp1)))
            else:
                s1 = i
            s2 = choice(range(len(temp2)))
            if s1 != s2:
                tedges.append([temp1[s1], temp2[s2]])
                self.add_edge(temp1[s1], temp2[s2])
                temp2.append(temp1[s1])
        return tedges
    def add_all_edges(self):
        for i in range(self.v):
            for j in range(i + 1, self.v):
                self.adjacency_list[self.nodes[j].name].append(self.nodes[i])
                self.adjacency_list[self.nodes[i].name].append(self.nodes[j])
                self.e += 1
    def add_edge(self, node1, node2):
        if node1 not in self.adjacency_list[node2.name] and node2 not in self.adjacency_list[node1.name]:
            self.adjacency_list[node1.name].append(node2)
            self.adjacency_list[node2.name].append(node1)
            self.e += 1
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
    graph.init_adj_list()
    graph.add_all_edges()
    graph.show_graph([[nodes[0], nodes[1]], [nodes[1], nodes[2]], [nodes[2], nodes[3]], [nodes[3], nodes[0]]])
if __name__ == "__main__":
    main()
from random import choice
import pygame
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.b4 = None
    def fonk2(self, b5):
        self.a2 = (self.b1 - b5.b1) ** 2 + (self.b2 - b5.b2) ** 2
        return self.a2
    def fonk3(self, b5 = None):
        if self.b4 is None:
            return 0
        self.a1 = self.b4.a1 + (self.b1 - self.b4.b1) ** 2 + (self.b2 - self.b4.b2) ** 2
        return self.a1
    def fonk4(self, b5):
        self.a3 = self.fonk3(b5) + self.fonk2(b5)
        return self.a3
class class2:
    def fonk5(self):
        self.b6 = {}
        self.b7 = {}
        self.a4 = 0
        self.a5 = 0
    def fonk6(self, edges):
        pygame.init()
        b8 = pygame.display.set_mode((600, 600))
        b9 = False
        b10 = pygame.time.Clock()
        while not b9:
            for event in pygame.event.get():
                if event.b11 = = pygame.QUIT:
                    b9 = True
            b8.fill((200, 200, 200))
            for n in self.b6.values():
                pygame.draw.circle(b8, (0, 100, 255), (int(n.b1), int(n.b2)), 10)
            for e in edges:
                pygame.draw.line(b8, (200, 100, 0), (int(e[0].b1), int(e[0].b2)), (int(e[1].b1), int(e[1].b2)), 4)
            pygame.display.flip()
            b10.tick(60)
    def fonk7(self, node):
        self.b6[node.b3] = node
        self.a4 += 1
    def fonk8(self):
        self.b7 = {}
        for b3 in self.b6.keys():
            self.b7[b3] = []
    def fonk9(self, b5):
        for node in self.b6.values():
            node.fonk2(b5)
    def fonk10(self, n, graph_v):
        b12 = []
        b13 = list(self.b6.values())
        b14 = [b13[0]]
        for i in range(n):
            b15 = choice(range(len(b13))) if len(b13) > i else i
            b16 = choice(range(len(b14)))
            if b15 != b16:
                b12.append([b13[b15], b14[b16]])
                self.fonk12(b13[b15], b14[b16])
                b14.append(b13[b15])
        return b12
    def fonk11(self):
        b13 = list(self.b6.values())
        for i in range(self.a4):
            for j in range(i + 1, self.a4):
                self.b7[b13[j].b3].append(b13[i])
                self.b7[b13[i].b3].append(b13[j])
                self.a5 += 1
    def fonk12(self, node1, node2):
        if node1 not in self.b7[node2.b3] and node2 not in self.b7[node1.b3]:
            self.b7[node1.b3].append(node2)
            self.b7[node2.b3].append(node1)
            self.a5 += 1
    def fonk13(self):
        for node in self.b6.values():
            node.b4 = None
            node.a1 = 0
            node.a2 = 0
            node.a3 = 0
def fonk14():
    b17 = class2()
    b6 = [class1(100, 100, 'A'), class1(200, 200, 'B'), class1(300, 300, 'C'), class1(400, 400, 'D')]
    for node in b6:
        b17.fonk7(node)
    b17.fonk8()
    b17.fonk11()
    b17.fonk6([[b6[0], b6[1]], [b6[1], b6[2]], [b6[2], b6[3]], [b6[3], b6[0]]])
if b18 = = "__main__":
    fonk14()
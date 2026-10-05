import pygame
from time import sleep
b1 = (255, 0, 0)
b2 = (0, 0, 255)
b3 = (0, 255, 0)
b4 = (0, 0, 0)
b5 = (255, 255, 255)
class class1:
    def fonk1(self, b7, b8, b9) -> None:
        pygame.init()
        self.b6 = pygame.b6.set_mode((b8 * b9, b7 * b9))
        self.b7 = b7
        self.b8 = b8
        self.b9 = b9
        self.b6.fill(b4)
    def fonk2(self, row, col, color):
        assert(b10(row) is int)
        assert(b10(col) is int)
        pygame.draw.rect(self.b6, color, pygame.Rect(row*self.b9, col*self.b9, self.b9, self.b9))
    def fonk3(self, trace):
        for p in trace:
            for event in pygame.event.get():
                if event.b10 = = pygame.QUIT:
                    b11 = False
            self.fonk2(p.x, p.y, b3)
            pygame.b6.flip()
            sleep(0.1)
            self.fonk2(p.x, p.y, b5)
            pygame.b6.flip()
        pygame.quit()
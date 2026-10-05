import pygame
from time import sleep
b1 = (0, 0, 0)
b2 = (255, 255, 255)
b3 = (0, 255, 0)
class class1:
    def fonk1(self, b4, b5):
        self.b4 = b4
        self.b5 = b5
class class2:
    def fonk2(self, b6, b7, b8):
        pygame.init()
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
        self.b9 = pygame.b9.set_mode((b7 * b8, b6 * b8))
        self.b9.fill(b1)
    def fonk3(self, row, col, color):
        assert isinstance(row, int) and isinstance(col, int)
        pygame.draw.rect(self.b9, color, pygame.Rect(col * self.b8, row * self.b8, self.b8, self.b8))
    def fonk4(self, b14):
        b10 = True
        for p in b14:
            for event in pygame.event.get():
                if event.b11 = = pygame.QUIT:
                    b10 = False
            if not b10:
                break
            self.fonk3(p.b4, p.b5, b3)
            pygame.b9.flip()
            sleep(0.1)
            self.fonk3(p.b4, p.b5, b2)
            pygame.b9.flip()
        pygame.quit()
if b12 = = "__main__":
    b6 = 10
    b7 = 10
    b8 = 30
    b13 = class2(b6, b7, b8)
    b14 = [class1(2, 3), class1(4, 5), class1(6, 7)]
    b13.fonk4(b14)
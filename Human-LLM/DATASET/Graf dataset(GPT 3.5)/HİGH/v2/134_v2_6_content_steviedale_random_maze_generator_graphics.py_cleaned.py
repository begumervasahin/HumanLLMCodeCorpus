import pygame
from time import sleep
b1 = (255, 0, 0)
b2 = (0, 0, 255)
b3 = (0, 255, 0)
b4 = (0, 0, 0)
b5 = (255, 255, 255)
class class1:
    def fonk1(self, b6, b7):
        self.b6 = b6
        self.b7 = b7
class class2:
    def fonk2(self, b9, b10, b11):
        pygame.init()
        self.b8 = pygame.b8.set_mode((b10 * b11, b9 * b11))
        self.b9 = b9
        self.b10 = b10
        self.b11 = b11
        self.b8.fill(b4)
    def fonk3(self, row, col, color):
        assert(b13(row) is int)
        assert(b13(col) is int)
        pygame.draw.rect(self.b8, color, pygame.Rect(col * self.b11, row * self.b11, self.b11, self.b11))
    def fonk4(self, b16):
        b12 = True
        for p in b16:
            for event in pygame.event.get():
                if event.b13 = = pygame.QUIT:
                    b12 = False
            if not b12:
                break
            self.fonk3(p.b6, p.b7, b3)
            pygame.b8.flip()
            sleep(0.1)
            self.fonk3(p.b6, p.b7, b5)
            pygame.b8.flip()
        pygame.quit()
if b14 = = "__main__":
    b9 = 10
    b10 = 10
    b11 = 30
    b15 = class2(b9, b10, b11)
    b16 = [class1(2, 3), class1(4, 5), class1(6, 7)]
    b15.fonk4(b16)
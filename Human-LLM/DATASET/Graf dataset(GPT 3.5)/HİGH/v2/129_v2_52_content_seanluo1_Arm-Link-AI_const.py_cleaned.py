import pygame
import sys
from pygame.locals import *
b1 = "config.txt"
a1 = 3
b2 = [5, 3, 1]
b3 = (0, 0, 0)
b4 = (255, 255, 255)
b5 = (255, 0, 0)
b6 = (0, 0, 255)
b7 = '%'
b8 = 'P'
b9 = '.'
b10 = ' '
a2 = 0
a3 = 1
a4 = 2
a5 = 30
a6 = 2
class class1:
    def fonk1(self):
        self.b11 = b1
        self.b12 = a1
        self.b13 = b2
        self.b14 = [b3, b4, b5, b6]
        self.b15 = b7
        self.b16 = b8
        self.b17 = b9
        self.b18 = b10
        self.b19 = a2
        self.b20 = a3
        self.b21 = a4
        self.b22 = a5
        self.b23 = a6
    def fonk2(self):
        pygame.init()
        b24 = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.b25 = = QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            b24.tick(self.b22)
if b26 = = '__main__':
    b27 = class1()
    b27.fonk2()
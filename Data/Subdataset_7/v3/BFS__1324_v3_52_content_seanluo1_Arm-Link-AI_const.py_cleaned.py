import pygame
import sys
from pygame.locals import *
b1 = "config.txt"
a1 = 3
b2 = [5, 3, 1]
b3 = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'RED': (255, 0, 0),
    'BLUE': (0, 0, 255)
}
b4 = '%'
b5 = 'P'
b6 = '.'
b7 = ' '
a2 = 0
a3 = 1
a4 = 2
a5 = 30
a6 = 2
class class1:
    def fonk1(self):
        self.b8 = b1
        self.b9 = a1
        self.b10 = b2
        self.b11 = b3
        self.b12 = b4
        self.b13 = b5
        self.b14 = b6
        self.b15 = b7
        self.b16 = a2
        self.b17 = a3
        self.b18 = a4
        self.b19 = a5
        self.b20 = a6
    def fonk2(self):
        pygame.init()
        b21 = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.b22 = = QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            b21.tick(self.b19)
if b23 = = '__main__':
    b24 = class1()
    b24.fonk2()
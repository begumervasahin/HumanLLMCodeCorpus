import pygame
import sys
b1 = (255, 255, 255)
b2 = (0, 0, 0)
b3 = (255, 0, 0)
b4 = (0, 255, 0)
b5 = 'up'
b6 = 'down'
b7 = 'left'
b8 = 'right'
a1 = 400
a2 = 400
a3 = 40
b9 = a1
b10 = a2
class class1:
    def fonk1(self):
        self.b11 = [(b9
        self.b12 = b8
    def fonk2(self):
        return self.b11[0]
    def fonk3(self):
        cur_x, b13 = self.fonk2()
        x, b14 = self.b12
        b15 = (cur_x + x) % b9
        b16 = (b13 + b14) % b10
        b17 = (b15, b16)
        self.b11.insert(0, b17)
        self.b11.pop()
    def fonk4(self):
        self.b11 = [(b9
        self.b12 = b8
    def fonk5(self, b12):
        if b12 = = b5 and self.b12 != b6:
            self.b12 = b5
        elif b12 = = b6 and self.b12 != b5:
            self.b12 = b6
        elif b12 = = b7 and self.b12 != b8:
            self.b12 = b7
        elif b12 = = b8 and self.b12 != b7:
            self.b12 = b8
def fonk6(b22):
    for event in pygame.event.get():
        if event.b18 = = pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.b18 = = pygame.KEYDOWN:
            if event.b19 = = pygame.K_UP:
                b22.fonk5(b5)
            elif event.b19 = = pygame.K_DOWN:
                b22.fonk5(b6)
            elif event.b19 = = pygame.K_LEFT:
                b22.fonk5(b7)
            elif event.b19 = = pygame.K_RIGHT:
                b22.fonk5(b8)
def fonk7(b20, b22):
    for pos in b22.b11:
        pygame.draw.rect(b20, b4, pygame.Rect(pos[0] * a3, pos[1] * a3, a3, a3))
def fonk8():
    pygame.init()
    b20 = pygame.display.set_mode((a1, a2))
    pygame.display.set_caption('class1')
    b21 = pygame.time.Clock()
    b22 = class1()
    while True:
        fonk6(b22)
        b22.fonk3()
        b20.fill(b2)
        fonk7(b20, b22)
        pygame.display.update()
        b21.tick(10)
if b23 = = '__main__':
    fonk8()
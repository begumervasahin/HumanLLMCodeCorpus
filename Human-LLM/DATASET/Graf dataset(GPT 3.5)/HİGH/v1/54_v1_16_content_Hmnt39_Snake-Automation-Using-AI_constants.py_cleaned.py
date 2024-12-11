import pygame
import sys
b1 = (255, 255, 255)
b2 = (  0,   0,   0)
b3 = (255,   0,   0)
b4 = (  0, 255,   0)
b5 = (  0, 155,   0)
b6 = ( 40,  40,  40)
b7 = ( 20,  20,  20)
b8 = b2
b9 = 'up'
b10 = 'down'
b11 = 'left'
b12 = 'right'
a1 = 0
a2 = 400
a3 = 400
a4 = 40
b13 = int(a2 / a4)
b14 = int(a3 / a4)
class class1:
    def fonk1(self):
        self.b15 = [(b13
        self.b16 = b12
    def fonk2(self):
        return self.b15[0]
    def fonk3(self):
        b17 = self.fonk2()
        x, b18 = self.b16
        b19 = ((b17[0] + (x*a4)) % a2, (b17[1] + (b18*a4)) % a3)
        self.b15.insert(0, b19)
        self.b15.pop()
    def fonk4(self):
        self.b15 = [(b13
        self.b16 = b12
    def fonk5(self, b16):
        if b16 = = b9 and self.b16 != b10:
            self.b16 = b9
        if b16 = = b10 and self.b16 != b9:
            self.b16 = b10
        if b16 = = b11 and self.b16 != b12:
            self.b16 = b11
        if b16 = = b12 and self.b16 != b11:
            self.b16 = b12
def fonk6():
    pygame.init()
    b20 = pygame.time.Clock()
    b21 = pygame.display.set_mode((a2, a3))
    b22 = class1()
    while True:
        for event in pygame.event.get():
            if event.b23 = = pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.b23 = = pygame.KEYDOWN:
                if event.b24 = = pygame.K_UP:
                    b22.fonk5(b9)
                elif event.b24 = = pygame.K_DOWN:
                    b22.fonk5(b10)
                elif event.b24 = = pygame.K_LEFT:
                    b22.fonk5(b11)
                elif event.b24 = = pygame.K_RIGHT:
                    b22.fonk5(b12)
        b22.fonk3()
        b21.fill(b8)
        for pos in b22.b15:
            pygame.draw.rect(b21, b4, pygame.Rect(pos[0], pos[1], a4, a4))
        pygame.display.update()
        b20.tick(10)
if b25 = = '__main__':
    fonk6()
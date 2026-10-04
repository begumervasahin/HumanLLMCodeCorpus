import pygame
import random
b1 = (255, 255, 255)
b2 = (0, 0, 0)
b3 = (255, 0, 0)
b4 = (0, 255, 0)
b5 = b2
b6 = 'up'
b7 = 'down'
b8 = 'left'
b9 = 'right'
a1 = 0
a2 = 400
a3 = 400
a4 = 40
b10 = a2
b11 = a3
class class1:
    def fonk1(self):
        pygame.init()
        self.b12 = pygame.display.set_mode((a2, a3))
        pygame.display.set_caption('Snake AI')
        self.b13 = pygame.time.Clock()
        self.b14 = pygame.b14.SysFont(None, 35)
        self.fonk2()
    def fonk2(self):
        self.b15 = [(b10
        self.b16 = random.choice([b6, b7, b8, b9])
        self.b17 = self.fonk3()
        self.a5 = 0
    def fonk3(self):
        while True:
            b18 = random.randint(0, b10 - 1)
            b19 = random.randint(0, b11 - 1)
            if (b18, b19) not in self.b15:
                return (b18, b19)
    def fonk4(self):
        head_x, b20 = self.b15[a1]
        if self.b16 = = b6:
            b20 -= 1
        elif self.b16 = = b7:
            b20 += 1
        elif self.b16 = = b8:
            head_x -= 1
        elif self.b16 = = b9:
            head_x += 1
        b21 = (head_x, b20)
        if b21 in self.b15 or not 0 <= head_x < b10 or not 0 <= b20 < b11:
            return False
        self.b15.insert(0, b21)
        if b21 = = self.b17:
            self.a5 += 1
            self.b17 = self.fonk3()
        else:
            self.b15.pop()
        return True
    def fonk5(self, b16):
        if (b16 = = b6 and self.b16 != b7) or \
           (b16 = = b7 and self.b16 != b6) or \
           (b16 = = b8 and self.b16 != b9) or \
           (b16 = = b9 and self.b16 != b8):
            self.b16 = b16
    def fonk6(self):
        self.b12.fill(b5)
        for b18, b19 in self.b15:
            pygame.draw.rect(self.b12, b4, pygame.Rect(b18 * a4, b19 * a4, a4, a4))
        pygame.draw.rect(self.b12, b3, pygame.Rect(self.b17[0] * a4, self.b17[1] * a4, a4, a4))
        b22 = self.b14.render(f'Score: {self.a5}', True, b1)
        self.b12.blit(b22, (10, 10))
        pygame.display.flip()
    def fonk7(self):
        b23 = True
        while b23:
            for event in pygame.event.get():
                if event.b24 = = pygame.QUIT:
                    b23 = False
                elif event.b24 = = pygame.KEYDOWN:
                    if event.b25 = = pygame.K_UP:
                        self.fonk5(b6)
                    elif event.b25 = = pygame.K_DOWN:
                        self.fonk5(b7)
                    elif event.b25 = = pygame.K_LEFT:
                        self.fonk5(b8)
                    elif event.b25 = = pygame.K_RIGHT:
                        self.fonk5(b9)
            if not self.fonk4():
                self.fonk2()
            self.fonk6()
            self.b13.tick(10)
if b26 = = "__main__":
    b27 = class1()
    b27.fonk7()
    pygame.quit()
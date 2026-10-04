import pygame
import random
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
        pygame.init()
        self.b15 = pygame.display.set_mode((a2, a3))
        pygame.display.set_caption('Snake AI')
        self.b16 = pygame.time.Clock()
        self.b17 = pygame.b17.SysFont(None, 35)
        self.fonk2()
    def fonk2(self):
        self.b18 = [(b13
        self.b19 = random.choice([b9, b10, b11, b12])
        self.b20 = self.fonk3()
        self.a5 = 0
    def fonk3(self):
        while True:
            b21 = random.randint(0, b13 - 1)
            b22 = random.randint(0, b14 - 1)
            if (b21, b22) not in self.b18:
                return (b21, b22)
    def fonk4(self):
        head_x, b23 = self.b18[a1]
        if self.b19 = = b9:
            b23 -= 1
        elif self.b19 = = b10:
            b23 += 1
        elif self.b19 = = b11:
            head_x -= 1
        elif self.b19 = = b12:
            head_x += 1
        b24 = (head_x, b23)
        if b24 in self.b18 or not 0 <= head_x < b13 or not 0 <= b23 < b14:
            return False
        self.b18.insert(0, b24)
        if b24 = = self.b20:
            self.a5 += 1
            self.b20 = self.fonk3()
        else:
            self.b18.pop()
        return True
    def fonk5(self, b19):
        if (b19 = = b9 and self.b19 != b10) or \
           (b19 = = b10 and self.b19 != b9) or \
           (b19 = = b11 and self.b19 != b12) or \
           (b19 = = b12 and self.b19 != b11):
            self.b19 = b19
    def fonk6(self):
        self.b15.fill(b8)
        for b21, b22 in self.b18:
            pygame.draw.rect(self.b15, b4, pygame.Rect(b21 * a4, b22 * a4, a4, a4))
        pygame.draw.rect(self.b15, b3, pygame.Rect(self.b20[0] * a4, self.b20[1] * a4, a4, a4))
        b25 = self.b17.render(f'Score: {self.a5}', True, b1)
        self.b15.blit(b25, (10, 10))
        pygame.display.flip()
    def fonk7(self):
        b26 = True
        while b26:
            for event in pygame.event.get():
                if event.b27 = = pygame.QUIT:
                    b26 = False
                elif event.b27 = = pygame.KEYDOWN:
                    if event.b28 = = pygame.K_UP:
                        self.fonk5(b9)
                    elif event.b28 = = pygame.K_DOWN:
                        self.fonk5(b10)
                    elif event.b28 = = pygame.K_LEFT:
                        self.fonk5(b11)
                    elif event.b28 = = pygame.K_RIGHT:
                        self.fonk5(b12)
            if not self.fonk4():
                self.fonk2()
            self.fonk6()
            self.b16.tick(10)
if b29 = = "__main__":
    b30 = class1()
    b30.fonk7()
    pygame.quit()
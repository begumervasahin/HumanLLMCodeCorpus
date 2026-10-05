import pygame
import sys
import random
b1 = [
    "skier_down.png", "skier_right1.png", "skier_right2.png",
    "skier_left2.png", "skier_left1.png"
]
class class1(pygame.sprite.Sprite):
    def fonk1(self):
        super().fonk4()
        self.b2 = pygame.b2.load("skier_down.png")
        self.b3 = self.b2.get_rect(b4=[320, 100])
        self.a1 = 0
    def fonk2(self, direction):
        self.a1 = max(min(self.a1 + direction, 2), -2)
        b4 = self.b3.b4
        self.b2 = pygame.b2.load(b1[self.a1])
        self.b3 = self.b2.get_rect(b4=b4)
        b5 = [self.a1, max(6 - abs(self.a1) * 2, 0)]
        return b5
    def fonk3(self, b5):
        self.b3.b6 += b5[0]
        self.b3.b6 = min(max(self.b3.b6, 20), 620)
class class2(pygame.sprite.Sprite):
    def fonk4(self, b7, b8, b16):
        super().fonk4()
        self.b7 = b7
        self.b2 = pygame.b2.load(b7)
        self.b8 = b8
        self.b3 = self.b2.get_rect(b4=b8)
        self.b9 = b16
        self.b10 = False
    def fonk5(self, terrain_pos):
        self.b3.b11 = self.b8[1] - terrain_pos
def fonk6(start, end):
    b12 = pygame.sprite.Group()
    b13 = []
    for _ in range(10):
        b14 = random.randint(start, end)
        b15 = random.randint(0, 9)
        b8 = [b15 * 64 + 20, b14 * 64 + 20]
        if b8 not in b13:
            b13.append(b8)
            b16 = random.choice(["tree", "flag"])
            b17 = "skier_tree.png" if b16 == "tree" else "skier_flag.png"
            b18 = class2(b17, b8, b16)
            b12.add(b18)
    return b12
def fonk7(b22, b23):
    b12 = pygame.sprite.Group()
    for ob in b22:
        b12.add(ob)
    for ob in b23:
        b12.add(ob)
    return b12
pygame.init()
b19 = pygame.display.set_mode([640, 640])
b20 = pygame.time.Clock()
b21 = class1()
b5 = [0, 6]
a2 = 0
a3 = 0
b22 = fonk6(20, 29)
b23 = fonk6(10, 19)
a4 = 0
b12 = fonk7(b22, b23)
b24 = pygame.b24.Font(None, 50)
def fonk8():
    b19.fill([255, 255, 255])
    pygame.display.update(b12.draw(b19))
    b19.blit(b21.b2, b21.b3)
    b19.blit(b27, [10, 10])
    pygame.display.flip()
while True:
    b20.tick(30)
    for event in pygame.event.get():
        if event.b9 = = pygame.QUIT:
            sys.exit()
        if event.b9 = = pygame.KEYDOWN:
            if event.b25 = = pygame.K_LEFT:
                b5 = b21.fonk2(-1)
            elif event.b25 = = pygame.K_RIGHT:
                b5 = b21.fonk2(1)
    b21.fonk3(b5)
    a2 += b5[1]
    if a2 >= 640 and a4 = = 0:
        a4 = 1
        b22 = fonk6(20, 29)
        b12 = fonk7(b22, b23)
    if a2 >= 1280 and a4 = = 1:
        a4 = 0
        for b18 in b22:
            b18.b8[1] -= 1280
        a2 -= 1280
        b23 = fonk6(10, 19)
        b12 = fonk7(b22, b23)
    for b18 in b12:
        b18.fonk5(a2)
    b26 = pygame.sprite.spritecollide(b21, b12, False)
    if b26:
        if b26[0].b9 = = "tree" and not b26[0].b10:
            a3 -= 100
            b21.b2 = pygame.b2.load("skier_crash.png")
            fonk8()
            pygame.time.delay(1000)
            b21.b2 = pygame.b2.load("skier_down.png")
            b21.a1 = 0
            b5 = [0, 6]
            b26[0].b10 = True
        elif b26[0].b9 = = "flag" and not b26[0].b10:
            a3 += 10
            b12.remove(b26[0])
    b27 = b24.render("Score: " + str(a3), 1, (0, 0, 0))
    fonk8()
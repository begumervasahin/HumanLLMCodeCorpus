import pygame
import sys
import random
b1 = [
    "skier_down.png", "skier_right1.png", "skier_right2.png",
    "skier_left2.png", "skier_left1.png"
]
a1 = 640
a2 = 640
b2 = [320, 100]
a3 = 20
a4 = 620
b3 = {"map0": (20, 29), "map1": (10, 19)}
class class1(pygame.sprite.Sprite):
    def fonk1(self):
        super().fonk4()
        self.b4 = pygame.b4.load("skier_down.png")
        self.b5 = self.b4.get_rect(b6=b2)
        self.a5 = 0
    def fonk2(self, direction):
        self.a5 = max(min(self.a5 + direction, 2), -2)
        b6 = self.b5.b6
        self.b4 = pygame.b4.load(b1[self.a5])
        self.b5 = self.b4.get_rect(b6=b6)
        b7 = [self.a5, max(6 - abs(self.a5) * 2, 0)]
        return b7
    def fonk3(self, b7):
        self.b5.b8 += b7[0]
        self.b5.b8 = min(max(self.b5.b8, a3), a4)
class class2(pygame.sprite.Sprite):
    def fonk4(self, image_file, b16, b17):
        super().fonk4()
        self.b4 = pygame.b4.load(image_file)
        self.b5 = self.b4.get_rect(b6=b16)
        self.b9 = b17
        self.b10 = False
    def fonk5(self, terrain_pos):
        self.b5.b11 = self.b5.b11 - terrain_pos
def fonk6():
    b12 = pygame.sprite.Group()
    b13 = []
    for _ in range(10):
        b14 = random.randint(*b3[b23])
        b15 = random.randint(0, 9)
        b16 = [b15 * 64 + 20, b14 * 64 + 20]
        if b16 not in b13:
            b13.append(b16)
            b17 = random.choice(["tree", "flag"])
            b18 = "skier_tree.png" if b17 == "tree" else "skier_flag.png"
            b19 = class2(b18, b16, b17)
            b12.add(b19)
    return b12
pygame.init()
b20 = pygame.display.set_mode([a1, a2])
b21 = pygame.time.Clock()
b22 = class1()
b7 = [0, 6]
a6 = 0
a7 = 0
b23 = "map0"
b12 = fonk6()
b24 = pygame.b24.Font(None, 50)
while True:
    b21.tick(30)
    for event in pygame.event.get():
        if event.b9 = = pygame.QUIT:
            sys.exit()
        if event.b9 = = pygame.KEYDOWN:
            if event.b25 = = pygame.K_LEFT:
                b7 = b22.fonk2(-1)
            elif event.b25 = = pygame.K_RIGHT:
                b7 = b22.fonk2(1)
    b22.fonk3(b7)
    a6 += b7[1]
    if a6 >= a1 and b23 = = "map0":
        b23 = "map1"
        b12 = fonk6()
    if a6 >= a1 * 2 and b23 = = "map1":
        b23 = "map0"
        for b19 in b12:
            b19.b5.b11 -= a1
        a6 -= a1
        b12 = fonk6()
    for b19 in b12:
        b19.fonk5(a6)
    b26 = pygame.sprite.spritecollide(b22, b12, False)
    if b26:
        if b26[0].b9 = = "tree" and not b26[0].b10:
            a7 -= 100
            b22.b4 = pygame.b4.load("skier_crash.png")
            pygame.time.delay(1000)
            b22.b4 = pygame.b4.load("skier_down.png")
            b22.a5 = 0
            b7 = [0, 6]
            b26[0].b10 = True
        elif b26[0].b9 = = "flag" and not b26[0].b10:
            a7 += 10
            b12.remove(b26[0])
    b27 = b24.render("Score: " + str(a7), 1, (0, 0, 0))
    b20.fill([255, 255, 255])
    b20.blit(b27, [10, 10])
    b20.blit(b22.b4, b22.b5)
    pygame.display.flip()
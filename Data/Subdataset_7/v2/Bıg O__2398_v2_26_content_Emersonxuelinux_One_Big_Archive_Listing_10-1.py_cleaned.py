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
    def fonk4(self, image_file, b14, b7):
        super().fonk4()
        self.b2 = pygame.b2.load(image_file)
        self.b3 = self.b2.get_rect(b4=b14)
        self.b7 = b7
        self.b8 = False
    def fonk5(self, terrain_pos):
        self.b3.b9 = self.b14[1] - terrain_pos
def fonk6(start, end):
    b10 = pygame.sprite.Group()
    b11 = []
    for _ in range(10):
        b12 = random.randint(start, end)
        b13 = random.randint(0, 9)
        b14 = [b13 * 64 + 20, b12 * 64 + 20]
        if b14 not in b11:
            b11.append(b14)
            b7 = random.choice(["tree", "flag"])
            b15 = "skier_tree.png" if b7 == "tree" else "skier_flag.png"
            b16 = class2(b15, b14, b7)
            b10.add(b16)
    return b10
def fonk7(b20, b21):
    b10 = pygame.sprite.Group(b20, b21)
    return b10
pygame.init()
b17 = pygame.display.set_mode([640, 640])
b18 = pygame.time.Clock()
b19 = class1()
b5 = [0, 6]
a2 = 0
a3 = 0
b20 = fonk6(20, 29)
b21 = fonk6(10, 19)
a4 = 0
b10 = fonk7(b20, b21)
b22 = pygame.b22.Font(None, 50)
while True:
    b18.tick(30)
    for event in pygame.event.get():
        if event.b7 = = pygame.QUIT:
            sys.exit()
        if event.b7 = = pygame.KEYDOWN:
            if event.b23 = = pygame.K_LEFT:
                b5 = b19.fonk2(-1)
            elif event.b23 = = pygame.K_RIGHT:
                b5 = b19.fonk2(1)
    b19.fonk3(b5)
    a2 += b5[1]
    if a2 >= 640 and a4 = = 0:
        a4 = 1
        b20 = fonk6(20, 29)
        b10 = fonk7(b20, b21)
    if a2 >= 1280 and a4 = = 1:
        a4 = 0
        for b16 in b20:
            b16.b14[1] -= 1280
        a2 -= 1280
        b21 = fonk6(10, 19)
        b10 = fonk7(b20, b21)
    for b16 in b10:
        b16.fonk5(a2)
    b24 = pygame.sprite.spritecollide(b19, b10, False)
    if b24:
        if b24[0].b7 = = "tree" and not b24[0].b8:
            a3 -= 100
            b19.b2 = pygame.b2.load("skier_crash.png")
            pygame.time.delay(1000)
            b19.b2 = pygame.b2.load("skier_down.png")
            b19.a1 = 0
            b5 = [0, 6]
            b24[0].b8 = True
        elif b24[0].b7 = = "flag" and not b24[0].b8:
            a3 += 10
            b10.remove(b24[0])
    b25 = b22.render("Score: " + str(a3), 1, (0, 0, 0))
    b17.fill([255, 255, 255])
    b17.blit(b25, [10, 10])
    b17.blit(b19.b2, b19.b3)
    pygame.display.flip()
import pygame
import sys
import random
a1 = 640
a2 = 640
a3 = 30
b1 = [
    "skier_down.png",
    "skier_right1.png",
    "skier_right2.png",
    "skier_left2.png",
    "skier_left1.png"
]
b2 = "skier_tree.png"
b3 = "skier_flag.png"
b4 = "skier_crash.png"
a4 = 50
class class1(pygame.sprite.Sprite):
    def fonk1(self):
        super().fonk4()
        self.b5 = pygame.b5.load("skier_down.png")
        self.b6 = self.b5.get_rect(b7=[320, 100])
        self.a5 = 0
    def fonk2(self, direction):
        self.a5 += direction
        self.a5 = max(-2, min(self.a5, 2))
        b7 = self.b6.b7
        self.b5 = pygame.b5.load(b1[self.a5])
        self.b6 = self.b5.get_rect(b7=b7)
        b8 = [self.a5, 6 - abs(self.a5) * 2]
        return b8
    def fonk3(self, b8):
        self.b6.b9 += b8[0]
        self.b6.b9 = max(20, min(self.b6.b9, 620))
class class2(pygame.sprite.Sprite):
    def fonk4(self, image_file, b17, b18):
        super().fonk4()
        self.b5 = pygame.b5.load(image_file)
        self.b6 = self.b5.get_rect(b7=b17)
        self.b10 = b18
        self.b11 = False
    def fonk5(self, terrain_pos):
        self.b6.b12 = self.b6.b12 - terrain_pos
def fonk6(start, end):
    b13 = pygame.sprite.Group()
    b14 = set()
    for _ in range(10):
        b15 = random.randint(start, end)
        b16 = random.randint(0, 9)
        b17 = (b16 * 64 + 20, b15 * 64 + 20)
        if b17 not in b14:
            b14.add(b17)
            b18 = random.choice(["tree", "flag"])
            b19 = b2 if b18 == "tree" else b3
            b20 = class2(b19, b17, b18)
            b13.add(b20)
    return b13
def fonk7():
    b21.fill([255, 255, 255])
    b13.draw(b21)
    b21.blit(b23.b5, b23.b6)
    b21.blit(b29, [10, 10])
    pygame.display.flip()
def fonk8(b25, b26):
    return b25 | b26
pygame.init()
b21 = pygame.display.set_mode([a1, a2])
b22 = pygame.time.Clock()
b23 = class1()
b8 = [0, 6]
a6 = 0
a7 = 0
b24 = pygame.b24.Font(None, a4)
b25 = fonk6(20, 29)
b26 = fonk6(10, 19)
a8 = 0
b13 = fonk8(b25, b26)
while True:
    b22.tick(a3)
    for event in pygame.event.get():
        if event.b10 = = pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.b10 = = pygame.KEYDOWN:
            if event.b27 = = pygame.K_LEFT:
                b8 = b23.fonk2(-1)
            elif event.b27 = = pygame.K_RIGHT:
                b8 = b23.fonk2(1)
    b23.fonk3(b8)
    a6 += b8[1]
    if a6 >= 640 and a8 = = 0:
        a8 = 1
        b25 = fonk6(20, 29)
        b13 = fonk8(b25, b26)
    if a6 >= 1280 and a8 = = 1:
        a8 = 0
        for ob in b25:
            ob.b6.b12 -= 1280
        a6 -= 1280
        b26 = fonk6(10, 19)
        b13 = fonk8(b25, b26)
    for b20 in b13:
        b20.fonk5(a6)
    b28 = pygame.sprite.spritecollide(b23, b13, False)
    if b28:
        if b28[0].b10 = = "tree" and not b28[0].b11:
            a7 -= 100
            b23.b5 = pygame.b5.load(b4)
            fonk7()
            pygame.time.delay(1000)
            b23.b5 = pygame.b5.load("skier_down.png")
            b23.a5 = 0
            b8 = [0, 6]
            b28[0].b11 = True
        elif b28[0].b10 = = "flag" and not b28[0].b11:
            a7 += 10
            b13.remove(b28[0])
    b29 = b24.render(f"Score: {a7}", True, (0, 0, 0))
    fonk7()
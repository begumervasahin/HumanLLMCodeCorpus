import pygame
import sys
import random
b1 = [
    "skier_down.png",
    "skier_right1.png",
    "skier_right2.png",
    "skier_left2.png",
    "skier_left1.png",
]
SCREEN_WIDTH, b2 = 640, 640
class class1(pygame.sprite.Sprite):
    def fonk1(self):
        super().fonk4()
        self.b3 = pygame.b3.load(b1[0])
        self.b4 = self.b3.get_rect()
        self.b4.b5 = [SCREEN_WIDTH
        self.a1 = 0
    def fonk2(self, direction):
        self.a1 += direction
        self.a1 = max(-2, min(2, self.a1))
        b5 = self.b4.b5
        self.b3 = pygame.b3.load(b1[self.a1])
        self.b4 = self.b3.get_rect()
        self.b4.b5 = b5
        b6 = [self.a1, 6 - abs(self.a1) * 2]
        return b6
    def fonk3(self, b6):
        self.b4.b7 += b6[0]
        self.b4.b7 = max(20, min(SCREEN_WIDTH - 20, self.b4.b7))
class class2(pygame.sprite.Sprite):
    def fonk4(self, image_file, b10, b8):
        super().fonk4()
        self.b3 = pygame.b3.load(image_file)
        self.b4 = self.b3.get_rect()
        self.b4.b5 = b10
        self.b8 = b8
        self.b9 = False
        self.b10 = b10
    def fonk5(self, terrain_pos):
        self.b4.b11 = self.b10[1] - terrain_pos
def fonk6(start, end):
    b12 = pygame.sprite.Group()
    b13 = []
    for _ in range(10):
        b14 = random.randint(start, end)
        b15 = random.randint(0, 9)
        b10 = [b15 * 64 + 20, b14 * 64 + 20]
        if b10 not in b13:
            b13.append(b10)
            b8 = random.choice(["tree", "flag"])
            b3 = "skier_tree.png" if b8 == "tree" else "skier_flag.png"
            b16 = class2(b3, b10, b8)
            b12.add(b16)
    return b12
def fonk7(b17, b19, b12, b25):
    b17.fill([255, 255, 255])
    b12.draw(b17)
    b17.blit(b19.b3, b19.b4)
    b17.blit(b25, [10, 10])
    pygame.display.flip()
def fonk8(b20, b21):
    b12 = pygame.sprite.Group()
    b12.add(*b20, *b21)
    return b12
def fonk9():
    pygame.init()
    b17 = pygame.display.set_mode([SCREEN_WIDTH, b2])
    b18 = pygame.time.Clock()
    b19 = class1()
    b6 = [0, 6]
    a2 = 0
    a3 = 0
    b20 = fonk6(20, 29)
    b21 = fonk6(10, 19)
    a4 = 0
    b12 = fonk8(b20, b21)
    b22 = pygame.b22.Font(None, 50)
    while True:
        b18.tick(30)
        for event in pygame.event.get():
            if event.b8 = = pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.b8 = = pygame.KEYDOWN:
                if event.b23 = = pygame.K_LEFT:
                    b6 = b19.fonk2(-1)
                elif event.b23 = = pygame.K_RIGHT:
                    b6 = b19.fonk2(1)
        b19.fonk3(b6)
        a2 += b6[1]
        if a2 >= b2 and a4 = = 0:
            a4 = 1
            b20 = fonk6(20, 29)
            b12 = fonk8(b20, b21)
        if a2 >= b2 * 2 and a4 = = 1:
            a4 = 0
            for ob in b20:
                ob.b10[1] -= b2 * 2
            a2 -= b2 * 2
            b21 = fonk6(10, 19)
            b12 = fonk8(b20, b21)
        for b16 in b12:
            b16.fonk5(a2)
        b24 = pygame.sprite.spritecollide(b19, b12, False)
        if b24:
            if b24[0].b8 = = "tree" and not b24[0].b9:
                a3 -= 100
                b19.b3 = pygame.b3.load("skier_crash.png")
                fonk7(b17, b19, b12, b25)
                pygame.time.delay(1000)
                b19.b3 = pygame.b3.load("skier_down.png")
                b19.a1 = 0
                b6 = [0, 6]
                b24[0].b9 = True
            elif b24[0].b8 = = "flag" and not b24[0].b9:
                a3 += 10
                b12.remove(b24[0])
        b25 = b22.render(f"Score: {a3}", 1, (0, 0, 0))
        fonk7(b17, b19, b12, b25)
if b26 = = "__main__":
    fonk9()
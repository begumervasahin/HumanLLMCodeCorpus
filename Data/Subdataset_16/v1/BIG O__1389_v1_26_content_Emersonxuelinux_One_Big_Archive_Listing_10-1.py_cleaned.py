import pygame, sys, random
b1 = ["skier_down.png", "skier_right1.png", "skier_right2.png", "skier_left2.png", "skier_left1.png"]
class class1(pygame.sprite.Sprite):
    def fonk1(self):
        pygame.sprite.Sprite.fonk4(self)
        self.b2 = pygame.b2.load("skier_down.png")
        self.b3 = self.b2.get_rect()
        self.b3.b4 = [320, 100]
        self.a1 = 0
    def fonk2(self, direction):
        self.a1 += direction
        if self.a1 < -2: self.a1 = -2
        if self.a1 > 2: self.a1 = 2
        b4 = self.b3.b4
        self.b2 = pygame.b2.load(b1[self.a1])
        self.b3 = self.b2.get_rect()
        self.b3.b4 = b4
        b5 = [self.a1, 6 - abs(self.a1) * 2]
        return b5
    def fonk3(self, b5):
        self.b3.a2 += b5[0]
        if self.b3.a2 < 20: self.b3.a2 = 20
        if self.b3.a2 > 620: self.b3.a2 = 620
class class2(pygame.sprite.Sprite):
    def fonk4(self, image_file, b13, b6):
        pygame.sprite.Sprite.fonk4(self)
        self.b2 = pygame.b2.load(image_file)
        self.b3 = self.b2.get_rect()
        self.b3.b4 = b13
        self.b6 = b6
        self.b7 = False
    def fonk5(self, terrainPos):
        self.b3.b8 = self.b13[1] - terrainPos
def fonk6(start, end):
    b9 = pygame.sprite.Group()
    b10 = []
    for i in range(10):
        b11 = random.randint(start, end)
        b12 = random.randint(0, 9)
        b13 = [b12 * 64 + 20, b11 * 64 + 20]
        if not b13 in b10:
            b10.append(b13)
            b6 = random.choice(["tree", "flag"])
            b14 = "skier_tree.png" if b6 == "tree" else "skier_flag.png"
            b15 = class2(b14, b13, b6)
            b9.add(b15)
    return b9
def fonk7():
    b16.fill([255, 255, 255])
    pygame.display.update(b9.draw(b16))
    b16.blit(b18.b2, b18.b3)
    b16.blit(b24, [10, 10])
    pygame.display.flip()
def fonk8(b19, b20):
    b9 = pygame.sprite.Group()
    for ob in b19: b9.add(ob)
    for ob in b20: b9.add(ob)
    return b9
pygame.init()
b16 = pygame.display.set_mode([640, 640])
b17 = pygame.time.Clock()
b18 = class1()
b5 = [0, 6]
a3 = 0
a4 = 0
b19 = fonk6(20, 29)
b20 = fonk6(10, 19)
a5 = 0
b9 = fonk8(b19, b20)
b21 = pygame.b21.Font(None, 50)
while True:
    b17.tick(30)
    for event in pygame.event.get():
        if event.b6 = = pygame.QUIT: sys.exit()
        if event.b6 = = pygame.KEYDOWN:
            if event.b22 = = pygame.K_LEFT:
                b5 = b18.fonk2(-1)
            elif event.b22 = = pygame.K_RIGHT:
                b5 = b18.fonk2(1)
    b18.fonk3(b5)
    a3 += b5[1]
    if a3 >= 640 and a5 = = 0:
        a5 = 1
        b19 = fonk6(20, 29)
        b9 = fonk8(b19, b20)
    if a3 >= 1280 and a5 = = 1:
        a5 = 0
        for ob in b19:
            ob.b13[1] -= 1280
        a3 -= 1280
        b20 = fonk6(10, 19)
        b9 = fonk8(b19, b20)
    for b15 in b9:
        b15.fonk5(a3)
    b23 = pygame.sprite.spritecollide(b18, b9, False)
    if b23:
        if b23[0].b6 = = "tree" and not b23[0].b7:
            a4 -= 100
            b18.b2 = pygame.b2.load("skier_crash.png")
            fonk7()
            pygame.time.delay(1000)
            b18.b2 = pygame.b2.load("skier_down.png")
            b18.a1 = 0
            b5 = [0, 6]
            b23[0].b7 = True
        elif b23[0].b6 = = "flag" and not b23[0].b7:
            a4 += 10
            b9.remove(b23[0])
    b24 = b21.render("Score: " + str(a4), 1, (0, 0, 0))
    fonk7()
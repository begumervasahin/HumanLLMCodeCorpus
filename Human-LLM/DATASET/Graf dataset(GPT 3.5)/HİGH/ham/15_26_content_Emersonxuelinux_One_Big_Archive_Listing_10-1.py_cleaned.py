import pygame, sys, random
b1 = ["skier_down.png", "skier_right1.png", "skier_right2.png",
                 "skier_left2.png", "skier_left1.png"]
class class1(pygame.sprite.Sprite):
    def fonk1(self):
        pygame.sprite.Sprite.fonk4(self)
        self.b2 = pygame.b2.load("skier_down.png")
        self.b3 = self.b2.get_rect()
        self.b3.b4 = [320, 100]
        self.a1 = 0
    def fonk2(self, direction):
        self.a1 = self.a1 + direction
        if self.a1 < -2:  self.a1 = -2
        if self.a1 >  2:  self.a1 = 2
        b4 = self.b3.b4
        self.b2 = pygame.b2.load(b1[self.a1])
        self.b3 = self.b2.get_rect()
        self.b3.b4 = b4
        b5 = [self.a1, 6 - abs(self.a1) * 2]
        return b5
    def fonk3(self, b5):
        self.b3.b6 = self.b3.b6 + b5[0]
        if self.b3.b6 < 20:  self.b3.b6 = 20
        if self.b3.b6 > 620: self.b3.b6 = 620
class class2(pygame.sprite.Sprite):
    def fonk4(self, b7, b8, b9):
        pygame.sprite.Sprite.fonk4(self)
        self.b7 = b7
        self.b2 = pygame.b2.load(b7)
        self.b8 = b8
        self.b3 = self.b2.get_rect()
        self.b3.b4 = b8
        self.b9 = b9
        self.b10 = False
    def fonk5(self, terrainPos):
        self.b3.b11 = self.b8[1] - terrainPos
def fonk6(start, end):
    b12 = pygame.sprite.Group()
    b13 = []
    b14 = pygame.sprite.Group()
    for i in range(10):
        b15 = random.randint(start, end)
        b16 = random.randint(0, 9)
        b8 = [b16 * 64 + 20, b15 * 64 + 20]
        if not (b8 in b13):
            b13.append(b8)
            b9 = random.choice(["tree", "flag"])
            if b9 = = "tree": img = "skier_tree.png"
            elif b9 = = "flag":  img = "skier_flag.png"
            b17 = class2(img, b8, b9)
            b12.add(b17)
    return b12
def fonk7():
    b18.fill([255, 255, 255])
    pygame.display.update(b12.draw(b18))
    b18.blit(b20.b2, b20.b3)
    b18.blit(b26, [10, 10])
    pygame.display.flip()
def fonk8(b21, b22):
    b12 = pygame.sprite.Group()
    for ob in b21:  b12.add(ob)
    for ob in b22:  b12.add(ob)
    return b12
pygame.init()
b18 = pygame.display.set_mode([640,640])
b19 = pygame.time.Clock()
b20 = class1()
b5 = [0, 6]
a2 = 0
a3 = 0
b21 = fonk6(20, 29)
b22 = fonk6(10, 19)
a4 = 0
b12 = fonk8(b21, b22)
b23 = pygame.b23.Font(None, 50)
while True:
    b19.tick(30)
    for event in pygame.event.get():
        if event.b9 = = pygame.QUIT: sys.exit()
        if event.b9 = = pygame.KEYDOWN:
            if event.b24 = = pygame.K_LEFT:
                b5 = b20.fonk2(-1)
            elif event.b24 = = pygame.K_RIGHT:
                b5 = b20.fonk2(1)
    b20.fonk3(b5)
    a2 += b5[1]
    if a2 >=640 and a4 = = 0:
        a4 = 1
        b21 = fonk6(20, 29)
        b12 = fonk8(b21, b22)
    if a2 >=1280 and a4 = = 1:
        a4 = 0
        for ob in b21:
            ob.b8[1] = ob.b8[1] - 1280
        a2 = a2 - 1280
        b22 = fonk6(10, 19)
        b12 = fonk8(b21, b22)
    for b17 in b12:
        b17.fonk5(a2)
    b25 = pygame.sprite.spritecollide(b20, b12, False)
    if b25:
        if b25[0].b9 = = "tree" and not b25[0].b10:
            a3 = a3 - 100
            b20.b2 = pygame.b2.load("skier_crash.png")
            fonk7()
            pygame.time.delay(1000)
            b20.b2 = pygame.b2.load("skier_down.png")
            b20.a1 = 0
            b5 = [0, 6]
            b25[0].b10 = True
        elif b25[0].b9 = = "flag" and not b25[0].b10:
            a3 += 10
            b12.remove(b25[0])
    b26 = b23.render("Score: " +str(a3), 1, (0, 0, 0))
    fonk7()
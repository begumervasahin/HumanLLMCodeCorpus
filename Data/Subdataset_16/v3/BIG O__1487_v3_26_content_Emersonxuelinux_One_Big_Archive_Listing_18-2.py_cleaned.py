import pygame
import sys
pygame.init()
SCREEN_WIDTH, b1 = 640, 480
b2 = pygame.display.set_mode([SCREEN_WIDTH, b1])
pygame.display.set_caption("class1 Movement")
b3 = pygame.Surface(b2.get_size())
b3.fill([255, 255, 255])
b4 = pygame.time.Clock()
class class1(pygame.sprite.Sprite):
    def fonk1(self, image_file, b8, location):
        super().fonk1()
        self.b5 = pygame.b5.load(image_file)
        self.b6 = self.b5.get_rect()
        self.b6.b7 = location
        self.b8 = b8
    def fonk2(self):
        if self.b6.left <= 0 or self.b6.right >= SCREEN_WIDTH:
            self.b8[0] = -self.b8[0]
        self.b6 = self.b6.fonk2(self.b8)
def fonk3(ball):
    for event in pygame.event.get():
        if event.b9 = = pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.b9 = = pygame.KEYDOWN:
            if event.b10 = = pygame.K_UP:
                ball.b6.y -= 10
            elif event.b10 = = pygame.K_DOWN:
                ball.b6.y += 10
def fonk4(ball):
    b2.blit(b3, (0, 0))
    ball.fonk2()
    b2.blit(ball.b5, ball.b6)
    pygame.display.flip()
def fonk5():
    b11 = class1('beach_ball.png', [10, 0], [20, 20])
    while True:
        fonk3(b11)
        fonk4(b11)
        b4.tick(30)
if b12 = = "__main__":
    fonk5()
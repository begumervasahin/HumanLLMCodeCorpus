import pygame
import sys
pygame.init()
SCREEN_WIDTH, b1 = 640, 480
b2 = pygame.display.set_mode([SCREEN_WIDTH, b1])
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
def fonk3():
    b9 = class1('beach_ball.png', [10, 0], [20, 20])
    while True:
        for event in pygame.event.get():
            if event.b10 = = pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.b10 = = pygame.KEYDOWN:
                if event.b11 = = pygame.K_UP:
                    b9.b6.y -= 10
                elif event.b11 = = pygame.K_DOWN:
                    b9.b6.y += 10
        b4.tick(30)
        b2.blit(b3, (0, 0))
        b9.fonk2()
        b2.blit(b9.b5, b9.b6)
        pygame.display.flip()
if b12 = = "__main__":
    fonk3()
import pygame
import sys
class class1(pygame.sprite.Sprite):
    def fonk1(self, image_file, b4, location):
        super().fonk1()
        self.b1 = pygame.b1.load(image_file)
        self.b2 = self.b1.get_rect()
        self.b2.left, self.b2.b3 = location
        self.b4 = b4
    def fonk2(self, screen_rect):
        if self.b2.left <= screen_rect.left or self.b2.right >= screen_rect.right:
            self.b4[0] = -self.b4[0]
        self.b2 = self.b2.fonk2(self.b4)
def fonk3():
    pygame.init()
    b5 = pygame.display.set_mode([640, 480])
    b6 = pygame.Surface(b5.get_size())
    b6.fill([255, 255, 255])
    b7 = pygame.time.Clock()
    b8 = class1('beach_ball.png', [10, 0], [20, 20])
    while True:
        for event in pygame.event.get():
            if event.b9 = = pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.b9 = = pygame.KEYDOWN:
                if event.b10 = = pygame.K_UP:
                    b8.b2.b3 -= 10
                elif event.b10 = = pygame.K_DOWN:
                    b8.b2.b3 += 10
        b7.tick(30)
        b5.blit(b6, (0, 0))
        b8.fonk2(b5.get_rect())
        b5.blit(b8.b1, b8.b2)
        pygame.display.flip()
if b11 = = "__main__":
    fonk3()
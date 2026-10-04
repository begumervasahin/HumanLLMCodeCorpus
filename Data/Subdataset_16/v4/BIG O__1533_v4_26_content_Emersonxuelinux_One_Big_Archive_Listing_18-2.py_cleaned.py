import pygame
import sys
def fonk1():
    pygame.init()
    b1 = pygame.display.set_mode([640, 480])
    b2 = pygame.Surface(b1.get_size())
    b2.fill([255, 255, 255])
    b3 = pygame.time.Clock()
    class class1(pygame.sprite.Sprite):
        def fonk2(self, image_file, b7, location):
            super().fonk2()
            self.b4 = pygame.b4.load(image_file)
            self.b5 = self.b4.get_rect()
            self.b5.left, self.b5.b6 = location
            self.b7 = b7
        def fonk3(self):
            if self.b5.left <= b1.get_rect().left or self.b5.right >= b1.get_rect().right:
                self.b7[0] = -self.b7[0]
            self.b5 = self.b5.fonk3(self.b7)
    b8 = class1('beach_ball.png', [10, 0], [20, 20])
    while True:
        for event in pygame.event.get():
            if event.b9 = = pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.b9 = = pygame.KEYDOWN:
                if event.b10 = = pygame.K_UP:
                    b8.b5.b6 -= 10
                elif event.b10 = = pygame.K_DOWN:
                    b8.b5.b6 += 10
        b3.tick(30)
        b1.blit(b2, (0, 0))
        b8.fonk3()
        b1.blit(b8.b4, b8.b5)
        pygame.display.flip()
if b11 = = "__main__":
    fonk1()
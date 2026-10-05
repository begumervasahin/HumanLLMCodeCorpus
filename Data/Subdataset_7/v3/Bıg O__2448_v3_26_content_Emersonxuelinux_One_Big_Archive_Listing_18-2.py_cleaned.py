import pygame
import sys
pygame.init()
a1 = 640
a2 = 480
b1 = pygame.display.set_mode([a1, a2])
b2 = pygame.Surface(b1.get_size())
b2.fill((255, 255, 255))
b3 = pygame.time.Clock()
class class1(pygame.sprite.Sprite):
    def fonk1(self, image_file, b7, location):
        super().fonk1()
        self.b4 = pygame.b4.load(image_file)
        self.b5 = self.b4.get_rect()
        self.b5.b6 = location
        self.b7 = b7
    def fonk2(self):
        if self.b5.left <= 0 or self.b5.right >= a1:
            self.b7[0] = -self.b7[0]
        self.b5.move_ip(self.b7)
b8 = 'beach_ball.png'
b9 = [10, 0]
b10 = [20, 20]
b11 = class1(b8, b9, b10)
while True:
    for event in pygame.event.get():
        if event.b12 = = pygame.QUIT:
            pygame.quit()
            sys.exit()
    b11.fonk2()
    b1.blit(b2, (0, 0))
    b1.blit(b11.b4, b11.b5)
    pygame.display.flip()
    b3.tick(30)
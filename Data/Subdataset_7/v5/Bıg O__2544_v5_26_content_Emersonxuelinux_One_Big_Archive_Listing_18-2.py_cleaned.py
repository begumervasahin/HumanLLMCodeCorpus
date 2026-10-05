import pygame
import sys
pygame.init()
SCREEN_WIDTH, b1 = 640, 480
b2 = pygame.display.set_mode((SCREEN_WIDTH, b1))
b3 = pygame.Surface(b2.get_size())
b3.fill((255, 255, 255))
b4 = pygame.time.Clock()
class class1(pygame.sprite.Sprite):
    def fonk1(self, image_file, b7, location):
        super().fonk1()
        self.b5 = pygame.b5.load(image_file)
        self.b6 = self.b5.get_rect(topleft=location)
        self.b7 = b7
    def fonk2(self):
        if self.b6.left <= 0 or self.b6.right >= SCREEN_WIDTH:
            self.b7[0] = -self.b7[0]
        self.b6.move_ip(self.b7)
b8 = 'beach_ball.png'
b9 = [10, 0]
b10 = [20, 20]
b11 = class1(b8, b9, b10)
b12 = True
while b12:
    for event in pygame.event.get():
        if event.b13 = = pygame.QUIT:
            b12 = False
        elif event.b13 = = pygame.KEYDOWN:
            if event.b14 = = pygame.K_UP:
                b11.b6.top -= 10
            elif event.b14 = = pygame.K_DOWN:
                b11.b6.top += 10
    b4.tick(30)
    b2.blit(b3, (0, 0))
    b11.fonk2()
    b2.blit(b11.b5, b11.b6)
    pygame.display.flip()
pygame.quit()
sys.exit()
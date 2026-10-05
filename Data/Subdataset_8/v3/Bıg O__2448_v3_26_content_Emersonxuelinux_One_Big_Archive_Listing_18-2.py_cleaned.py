import pygame
import sys
pygame.init()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
clock = pygame.time.Clock()
class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.topleft = location
        self.speed = speed
    def move(self):
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed[0] = -self.speed[0]
        self.rect.move_ip(self.speed)
BALL_IMAGE = 'beach_ball.png'
BALL_SPEED = [10, 0]
BALL_LOCATION = [20, 20]
my_ball = Ball(BALL_IMAGE, BALL_SPEED, BALL_LOCATION)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    my_ball.move()
    screen.blit(background, (0, 0))
    screen.blit(my_ball.image, my_ball.rect)
    pygame.display.flip()
    clock.tick(30)
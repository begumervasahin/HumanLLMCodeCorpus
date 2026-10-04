import pygame
import sys
class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self, screen_rect):
        if self.rect.left <= screen_rect.left or self.rect.right >= screen_rect.right:
            self.speed[0] = -self.speed[0]
        self.rect = self.rect.move(self.speed)
def main():
    pygame.init()
    screen = pygame.display.set_mode([640, 480])
    background = pygame.Surface(screen.get_size())
    background.fill([255, 255, 255])
    clock = pygame.time.Clock()
    my_ball = Ball('beach_ball.png', [10, 0], [20, 20])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    my_ball.rect.top -= 10
                elif event.key == pygame.K_DOWN:
                    my_ball.rect.top += 10
        clock.tick(30)
        screen.blit(background, (0, 0))
        my_ball.move(screen.get_rect())
        screen.blit(my_ball.image, my_ball.rect)
        pygame.display.flip()
if __name__ == "__main__":
    main()
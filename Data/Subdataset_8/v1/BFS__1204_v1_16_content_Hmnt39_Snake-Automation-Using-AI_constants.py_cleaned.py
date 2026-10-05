import pygame
import sys
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
GRAY      = ( 20,  20,  20)
BGCOLOR = BLACK
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
HEAD = 0
w = 400
h = 400
block_size = 40
width = int(w / block_size)
height = int(h / block_size)
class Snake:
    def __init__(self):
        self.positions = [(width
        self.direction = RIGHT
    def get_head_position(self):
        return self.positions[0]
    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x*block_size)) % w, (cur[1] + (y*block_size)) % h)
        self.positions.insert(0, new)
        self.positions.pop()
    def reset(self):
        self.positions = [(width
        self.direction = RIGHT
    def change_direction(self, direction):
        if direction == UP and self.direction != DOWN:
            self.direction = UP
        if direction == DOWN and self.direction != UP:
            self.direction = DOWN
        if direction == LEFT and self.direction != RIGHT:
            self.direction = LEFT
        if direction == RIGHT and self.direction != LEFT:
            self.direction = RIGHT
def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((w, h))
    snake = Snake()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)
        snake.move()
        screen.fill(BGCOLOR)
        for pos in snake.positions:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], block_size, block_size))
        pygame.display.update()
        clock.tick(10)
if __name__ == '__main__':
    main()
import pygame
import sys
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
BLOCK_SIZE = 40
GRID_WIDTH = WINDOW_WIDTH
GRID_HEIGHT = WINDOW_HEIGHT
class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH
        self.direction = RIGHT
    def get_head_position(self):
        return self.positions[0]
    def move(self):
        cur_x, cur_y = self.get_head_position()
        x, y = self.direction
        new_x = (cur_x + x) % GRID_WIDTH
        new_y = (cur_y + y) % GRID_HEIGHT
        new_position = (new_x, new_y)
        self.positions.insert(0, new_position)
        self.positions.pop()
    def reset(self):
        self.positions = [(GRID_WIDTH
        self.direction = RIGHT
    def change_direction(self, direction):
        if direction == UP and self.direction != DOWN:
            self.direction = UP
        elif direction == DOWN and self.direction != UP:
            self.direction = DOWN
        elif direction == LEFT and self.direction != RIGHT:
            self.direction = LEFT
        elif direction == RIGHT and self.direction != LEFT:
            self.direction = RIGHT
def handle_events(snake):
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
def draw_snake(screen, snake):
    for pos in snake.positions:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0] * BLOCK_SIZE, pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()
    snake = Snake()
    while True:
        handle_events(snake)
        snake.move()
        screen.fill(BLACK)
        draw_snake(screen, snake)
        pygame.display.update()
        clock.tick(10)
if __name__ == '__main__':
    main()
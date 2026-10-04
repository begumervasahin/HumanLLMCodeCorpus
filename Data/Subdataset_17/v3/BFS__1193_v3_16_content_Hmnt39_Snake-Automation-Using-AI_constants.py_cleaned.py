import pygame
import random
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BGCOLOR = BLACK
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
HEAD = 0
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 40
WIDTH = SCREEN_WIDTH
HEIGHT = SCREEN_HEIGHT
class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake AI')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 35)
        self.reset()
    def reset(self):
        self.snake = [(WIDTH
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.food = self.get_random_food()
        self.score = 0
    def get_random_food(self):
        while True:
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT - 1)
            if (x, y) not in self.snake:
                return (x, y)
    def move(self):
        head_x, head_y = self.snake[HEAD]
        if self.direction == UP:
            head_y -= 1
        elif self.direction == DOWN:
            head_y += 1
        elif self.direction == LEFT:
            head_x -= 1
        elif self.direction == RIGHT:
            head_x += 1
        new_head = (head_x, head_y)
        if new_head in self.snake or not 0 <= head_x < WIDTH or not 0 <= head_y < HEIGHT:
            return False
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.food = self.get_random_food()
        else:
            self.snake.pop()
        return True
    def change_direction(self, direction):
        if (direction == UP and self.direction != DOWN) or \
           (direction == DOWN and self.direction != UP) or \
           (direction == LEFT and self.direction != RIGHT) or \
           (direction == RIGHT and self.direction != LEFT):
            self.direction = direction
    def draw(self):
        self.screen.fill(BGCOLOR)
        for x, y in self.snake:
            pygame.draw.rect(self.screen, GREEN, pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.screen, RED, pygame.Rect(self.food[0] * BLOCK_SIZE, self.food[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        text = self.font.render(f'Score: {self.score}', True, WHITE)
        self.screen.blit(text, (10, 10))
        pygame.display.flip()
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.change_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        self.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.change_direction(RIGHT)
            if not self.move():
                self.reset()
            self.draw()
            self.clock.tick(10)
if __name__ == "__main__":
    game = SnakeGame()
    game.run()
    pygame.quit()
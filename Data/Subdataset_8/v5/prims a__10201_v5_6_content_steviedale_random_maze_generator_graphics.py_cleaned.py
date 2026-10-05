import pygame
from time import sleep
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
class BoardDisplay:
    def __init__(self, num_rows, num_columns, square_width) -> None:
        pygame.init()
        self.display = pygame.display.set_mode((num_columns * square_width, num_rows * square_width))
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.square_width = square_width
        self.display.fill(BLACK)
    def draw_square(self, row, col, color):
        assert isinstance(row, int) and isinstance(col, int), "Row and column indices must be integers"
        pygame.draw.rect(self.display, color, pygame.Rect(col * self.square_width, row * self.square_width, self.square_width, self.square_width))
    def start(self, trace):
        for position in trace:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            self.draw_square(position.x, position.y, GREEN)
            pygame.display.flip()
            sleep(0.1)
            self.draw_square(position.x, position.y, WHITE)
        pygame.quit()
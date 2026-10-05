import pygame
from time import sleep
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
class BoardDisplay:
    def __init__(self, num_rows, num_columns, width) -> None:
        pygame.init()
        self.display = pygame.display.set_mode((num_columns * width, num_rows * width))
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.width = width
        self.display.fill(BLACK)
    def draw_position(self, row, col, color):
        assert(type(row) is int)
        assert(type(col) is int)
        pygame.draw.rect(self.display, color, pygame.Rect(row*self.width, col*self.width, self.width, self.width))
    def start(self, trace):
        for p in trace:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw_position(p.x, p.y, GREEN)
            pygame.display.flip()
            sleep(0.1)
            self.draw_position(p.x, p.y, WHITE)
            pygame.display.flip()
        pygame.quit()
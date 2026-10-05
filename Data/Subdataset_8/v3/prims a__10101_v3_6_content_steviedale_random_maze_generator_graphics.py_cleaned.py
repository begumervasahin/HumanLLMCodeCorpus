import pygame
from time import sleep
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class BoardDisplay:
    def __init__(self, num_rows, num_columns, cell_width):
        pygame.init()
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.cell_width = cell_width
        self.display = pygame.display.set_mode((num_columns * cell_width, num_rows * cell_width))
        self.display.fill(BLACK)
    def draw_position(self, row, col, color):
        assert isinstance(row, int) and isinstance(col, int)
        pygame.draw.rect(self.display, color, pygame.Rect(col * self.cell_width, row * self.cell_width, self.cell_width, self.cell_width))
    def start(self, trace):
        running = True
        for p in trace:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if not running:
                break
            self.draw_position(p.x, p.y, GREEN)
            pygame.display.flip()
            sleep(0.1)
            self.draw_position(p.x, p.y, WHITE)
            pygame.display.flip()
        pygame.quit()
if __name__ == "__main__":
    num_rows = 10
    num_columns = 10
    cell_width = 30
    board = BoardDisplay(num_rows, num_columns, cell_width)
    trace = [Position(2, 3), Position(4, 5), Position(6, 7)]
    board.start(trace)
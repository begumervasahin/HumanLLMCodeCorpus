import pygame
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WIDTH = 20
HEIGHT = 20
MARGIN = 0
WINDOW_SIZE = [680, 480]
ROWS = 24
COLUMNS = 34
grid = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Random Maze")
clock = pygame.time.Clock()
frontier = []
i, j = random.randint(2, ROWS - 3), random.randint(2, COLUMNS - 3)
grid[i][j] = 1
print(f"grid[{i}][{j}]")
def add_to_frontier(x, y):
    if 2 <= x < ROWS - 2 and 2 <= y < COLUMNS - 2 and grid[x][y] == 0:
        if (x, y) not in frontier:
            grid[x][y] = 2
            frontier.append((x, y))
add_to_frontier(i + 2, j)
add_to_frontier(i - 2, j)
add_to_frontier(i, j + 2)
add_to_frontier(i, j - 2)
print(frontier)
def draw_grid():
    for row in range(ROWS):
        for column in range(COLUMNS):
            color = BLACK
            if grid[row][column] == 1:
                color = WHITE
            elif grid[row][column] == 2:
                color = RED
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH, HEIGHT])
def process_frontier():
    f = random.randint(0, len(frontier) - 1)
    x, y = frontier[f]
    print(f"Selected frontier {x}, {y}")
    neighbours = [(x - 2, y), (x + 2, y), (x, y - 2), (x, y + 2)]
    valid_neighbours = [(nx, ny) for nx, ny in neighbours if 0 <= nx < ROWS and 0 <= ny < COLUMNS and grid[nx][ny] == 1]
    if valid_neighbours:
        p, q = random.choice(valid_neighbours)
        print(f"Selected neighbour {p}, {q}")
        grid[x][y] = 1
        if p == x:
            grid[x][y + 1 if q > y else y - 1] = 1
        elif q == y:
            grid[x + 1 if p > x else x - 1][y] = 1
        add_to_frontier(x + 2, y)
        add_to_frontier(x - 2, y)
        add_to_frontier(x, y + 2)
        add_to_frontier(x, y - 2)
        print(frontier)
        draw_grid()
        clock.tick(10)
        pygame.display.flip()
    frontier.pop(f)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if frontier:
        process_frontier()
pygame.quit()